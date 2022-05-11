rm -rf cn/data/klay/chaindata/ network-local/cn/data/klay/LOCK network-local/cn/data/klay/transactions.rlp
cn/bin/kcn init --datadir cn/data genesis.json
./cn/bin/kcnd start
