if [ $# -eq 0 ]; then
  echo "Warning: no arguments"
  exit 0
fi
# 지정해서 바꿔주기
cd ~/project/klaytn
PROJECT_DIR=~/project/network-local
cp build/bin/kcn ${PROJECT_DIR}/cn/bin/kcn_$1
cp build/bin/kpn ${PROJECT_DIR}/pn/bin/kpn_$1
cp build/bin/ken ${PROJECT_DIR}/en/bin/ken_$1

