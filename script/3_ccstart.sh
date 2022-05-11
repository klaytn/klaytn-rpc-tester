cn/bin/kcnd start
pn/bin/kpnd start
en/bin/kend start

# 3-1. with http
# bin/kcn --datadir data --nodiscover --nodekey homi-output/keys/nodekey1 --networkid 940625 --rpc --rpcapi admin,debug,klay,miner,net,personal,rpc,txpool,web3 --unlock 0,1,2,3,4,5,6,7,8,9,10 --ws --wsapi admin,klay,debug,miner,net,txpool,personal,web3 --password conf/pwd.txt --port 0 --rpccorsdomain https://remix.ethereum.org
# 3-2. with fasthttp
# bin/kcn --datadir data --nodiscover --nodekey homi-output/keys/nodekey1 --networkid 940625 --rpc --rpcapi admin,debug,klay,miner,net,personal,rpc,txpool,web3 --unlock 0,1,2,3,4,5,6,7,8,9,10 --ws --wsapi admin,klay,debug,miner,net,txpool,personal,web3 --password conf/pwd.txt --port 0 --srvtype fasthttp --rpcvhosts '*'
# 3-3. with --cypress
# bin/kcn --datadir data --nodiscover --nodekey homi-output/keys/nodekey1 --rpc --rpcapi admin,debug,klay,miner,net,personal,rpc,txpool,web3 --unlock 0,1,2,3,4,5,6,7,8,9,10 --ws --wsapi admin,klay,debug,miner,net,txpool,personal,web3 --password conf/pwd.txt --port 0 --rpccorsdomain https://remix.ethereum.org --cypress
# 3-4. without passwd
# bin/kcn --datadir data --nodiscover --nodekey homi-output/keys/nodekey1 --networkid 940625 --rpc --rpcapi admin,debug,klay,miner,net,personal,rpc,txpool,web3 --ws --wsapi admin,klay,debug,miner,net,txpool,personal,web3 --unlock 0 --password conf/pwd2.txt --port 0 --rpccorsdomain https://remix.ethereum.org

