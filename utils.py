import os.path
import time
import pathlib
import json
import unittest
import requests
import codecs
import re
import random
import string
import sys
from websocket._core import create_connection
from datetime import datetime
from errors import ERRORS
from enum import Enum

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT_DIR = pathlib.Path(CURRENT_DIR)


class Utils(unittest.TestCase):
    class TestingStatus(Enum):
        START = 1
        FINISHED = 2
        NONE = 3

    @staticmethod
    def get_date_strings():
        """Return date information with various formats to check date."""
        local_datetime = datetime.now()
        dt = datetime(
            local_datetime.year,
            local_datetime.month,
            local_datetime.day,
            local_datetime.hour,
            local_datetime.minute,
            local_datetime.second,
        )
        timestamp = time.mktime(dt.timetuple())
        return (local_datetime, dt, timestamp)

    @staticmethod
    def get_log_filename_with_path():
        """Create log file whenever test is executed and returns path, directory name, and log file name."""

        _, _, timestamp = Utils.get_date_strings()

        log_directory_name = datetime.fromtimestamp(int(timestamp)).strftime("%Y%m%d%H%M%S")

        log_path = f"./reports/{log_directory_name}"
        pathlib.Path(log_path).mkdir(parents=True, exist_ok=True)

        log_file_name = f"{log_path}/klaytn.log"

        return log_path, log_directory_name, log_file_name

    @staticmethod
    def get_request_id():
        """Returns a random integer (1 ~ 99) to be used as request id when call API."""
        return random.randint(1, 100)

    @staticmethod
    def save_result_data(log_path, file_name, data):
        """If result value is big like blockdump, store it as a file."""

        # Check path of log and if there is no directory, create a directory.
        pathlib.Path(log_path).mkdir(parents=True, exist_ok=True)

        # Appoint path and file name to store.
        path = f"{log_path}/{file_name}"
        with open(path, "wt") as f:
            f.write(f"{data}")

    @staticmethod
    def convert_to_hex(message):
        """Change string, int data to hex data."""
        hex_data = ""

        if isinstance(message, str):
            hex_data = "0x" + "".join("{:02x}".format(ord(c)) for c in str(message))

        if isinstance(message, int):
            hex_data = hex(message)

        if isinstance(message, dict):
            message = json.dumps(message)
            hex_data = "0x" + "".join("{:02x}".format(ord(c)) for c in str(message))

        return hex_data

    @staticmethod
    def convert_hex_to_string(hex_data):
        """Convert hex data to string."""

        hex_data = Utils.strip_hex_prefix(hex_data)

        string_data = codecs.decode(hex_data, "hex").decode("utf-8", "ignore")

        # replace null character
        string_data = string_data.replace("\x00", "")
        string_data = string_data.replace("\x16", "")

        return string_data

    @staticmethod
    def is_hex(s):
        """Returns true if given string is a hexadecimal."""
        s = Utils.strip_hex_prefix(s)
        return all(c in string.hexdigits for c in s)

    @staticmethod
    def strip_hex_prefix(s):
        """Remove hex prefix and returns hexadecimal without prefix."""
        if len(s) >= 2:
            if s[:2] == "0x" or s[:2] == "0X":
                return s[2:]
            else:
                return s
        return s

    @staticmethod
    def left_pad64(hex_data):
        """Pad zeros and returns 64-length hexadecimal."""
        hex_data = Utils.strip_hex_prefix(hex_data)
        return "{:0>64}".format(hex_data)

    @staticmethod
    def get_config():
        """Read config.json and return parsed json data."""

        with open(f"{PROJECT_ROOT_DIR}/config.json") as f:
            data = json.load(f)

        return data

    @staticmethod
    def call_rpc(endpoint, method, params, log_file, save_result=False, port=8551):
        if endpoint is None or endpoint == "":
            endpoint = Utils.get_config().get("endpoint")
        host = f"http://{endpoint}:{port}"
        headers = {"Content-Type": "application/json"}

        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": [],
            "id": Utils.get_request_id(),
        }
        if params is not None:
            payload["params"] = params

        response = requests.post(host, data=json.dumps(payload), headers=headers, timeout=300)
        if response.status_code != 200:
            return f"Error: Unexpected response {response}"

        Utils.write_log(
            log_file,
            method,
            host,
            payload,
            response.text,
            save_file=save_result,
        )

        response_json = json.loads(response.text)
        result = response_json.get("result")
        error = response_json.get("error")

        return result, error

    @staticmethod
    def call_ws(endpoint, method, params, log_file, save_result=False, port=8552):
        host = f"ws://{endpoint}:{port}"
        if params == None:
            params = []
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": Utils.get_request_id(),
        }

        ws = create_connection(host)
        ws.send(json.dumps(payload))
        response = ws.recv()
        ws.close()

        response_json = json.loads(response)
        result = response_json.get("result")
        error = response_json.get("error")

        Utils.write_log(
            log_file,
            method,
            host,
            payload,
            response,
            save_file=save_result,
            service="ws",
        )
        return result, error

    @staticmethod
    def get_console_result_with_index(screenshot, command, log_file, save_result=False, columns=0):
        klaytn_list, command_index = Utils.parse_command(screenshot, command, columns)

        # Make a string from command_index to last line and remove white spaces.
        result_string = " ".join(klaytn_list[command_index:]).replace(" ", "")

        # There is no quotation at key of returned json result from klaytn console.
        # Use regular expressions to change it to valid json string.
        valid_json = re.sub(r"(?<={|,)([a-zA-Z][a-zA-Z0-9]*)(?=:)", r'"\1"', result_string)

        try:
            result = json.loads(valid_json)
        except:
            result = valid_json

        if command == "> exit":
            result = None

        Utils.write_console_log(log_file, command_index, command, result, save_file=save_result)
        return result

    @staticmethod
    def parse_command(screenshot, command, columns):
        command = f"> {command}"

        # Split screenshot by lines and convert it to the array and remove ''.
        # Maximum lines of screenshot is 9999.
        klaytn_list = list(filter(None, screenshot.splitlines()))

        # Check the last line of an array and remove when it is '>' (waiting command status).
        last_index = len(klaytn_list) - 1
        if klaytn_list[last_index] == ">":
            del klaytn_list[-1]

        # Checks the index of klaytn command at the last of array.
        # If command is longer than terminal's width(columns), find after cutting it out.
        if columns == 0:
            command_index = last_index - klaytn_list[::-1].index(command)
        else:
            command_index = last_index - klaytn_list[::-1].index(command[:columns])

        return klaytn_list, command_index

    @staticmethod
    def get_console_sub_command(screenshot, command, logfile, save_result=False, columns=0):
        klaytn_list, command_index = Utils.parse_command(screenshot, command, columns)
        Utils.write_console_log(logfile, command_index, command, None, save_file=save_result)
        return command

    @staticmethod
    def write_head_or_tail_log(
        log_file_name,
        testing_status,
        testing_unit="",
    ):
        with open(log_file_name, "at") as f:
            if testing_status == Utils.TestingStatus.START:
                log_string = f"------------ Testing Start ({testing_unit}) ------------- \n\n"
            elif testing_status == Utils.TestingStatus.FINISHED:
                log_string = f"------------ Testing Finished ({testing_unit}) ------------ \n\n"
            print(log_string)
            f.write(f"\n{log_string}")

    @staticmethod
    def write_log(
        log_file_name,
        method,
        host,
        data,
        result_text,
        file_name="",
        save_file=False,
        service="rpc",
    ):
        """
        Write start of testing at log file.
        If result data size is big like debug_dumpBlock, that will be stored as file.
        """
        if save_file and (file_name != "" and file_name is not None):
            with open(file_name, "w") as f:
                f.write(result_text)

        with open(log_file_name, "at") as f:
            if service == "rpc":
                curl_string = f'curl -H "Content-Type: application/json" --data "{str(json.dumps(data))}" {host}'
            else:
                curl_string = f'["{host}"]\n{str(json.dumps(data))}'

            log_string = f"[{str(datetime.now())}] [{method}]\n" f"{curl_string}\n"
            try:
                result_json = json.loads(result_text)
                log_string += f"{json.dumps(result_json, indent=4, sort_keys=True)} \n\n"
            except ValueError as e:
                log_string += f"{result_text} \n\n"

            print(log_string)

            f.write(f"\n{log_string}")

    @staticmethod
    def write_console_log(
        log_file_name,
        search_index,
        command,
        result,
        testing_status,
        testing_unit="",
        save_file=False,
    ):
        """
        Write start of testing at log file.
        If result data size is big like debug_dumpBlock, that will be stored as file.
        """

        if save_file:
            result = {"Utils_Message": "Output data was saved at a specific file."}

        with open(log_file_name, "at") as f:
            if testing_status == Utils.TestingStatus.START:
                log_string = f"------------ Testing Start ({testing_unit}) ------------- \n\n"
            elif testing_status == Utils.TestingStatus.FINISHED:
                log_string = f"------------ Testing Finished ({testing_unit}) ------------ \n\n"
            else:
                log_string = (
                    f"[IDX:{str(search_index)}] [{str(datetime.now())}] \n"
                    f"{command} \n"
                    f"{json.dumps(result, indent=4, sort_keys=True)} \n\n"
                )
            f.write(log_string)

        print(log_string)
        time.sleep(2)

    @staticmethod
    def waiting_count(frontString, second, rearString):
        """
        Lets count number while waiting.
        ex) Utils.waitingCount('Waiting for', 5, 'seconds until writing in block a transaction.')
        """
        for i in range(second, -1, -1):
            sys.stdout.write(f"\r{frontString} {i} {rearString}")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\n\n")

    @staticmethod
    def to_peb(klay):
        """Convert unit KLAY to Peb."""
        peb = 0
        if isinstance(klay, float):
            peb = int(klay * 1000000000000000000.0)

        if isinstance(klay, int):
            peb = klay * 1000000000000000000

        return peb

    @staticmethod
    def check_error(target_instance, expected_error_key, error):
        """
        Check whether given error is expected error or not by using expected_error_key.
        target_instance must inherit unittest.TestCase class.
        """
        expected_error_code, expected_error_message = ERRORS[expected_error_key]
        target_instance.assertEqual(expected_error_code, error.get("code"), error)
        target_instance.assertIn(expected_error_message, error.get("message"), error)
