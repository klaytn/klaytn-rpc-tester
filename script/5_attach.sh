if [ "$1" = "rpc" ]; then
  cn/bin/kcn attach http://localhost:8551
elif [ "$1" = "ws" ]; then
  cn/bin/kcn attach ws://localhost:8552
else
  cn/bin/kcn attach cn/data/klay.ipc
fi