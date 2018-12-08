#from web3.auto import w3
from web3 import Web3

#import Config
#net =  Config.Net.Set()["net"]

#web3 = Web3(Web3.HTTPProvider(net))#net))
web3 = Web3(Web3.HTTPProvider("http://192.168.51.203:19999"))


class w3:
    def block(num):
        return web3.eth.getBlock(num)
        #print(web3.eth.defaultBlock)
    def blockNumber():
        print(web3.eth.blockNumber)
    def getTransaction(hashs):
        print(web3.eth.getTransaction(hashs))
    def getTransactionReceipt(hashs):
        return web3.eth.getTransactionReceipt(hashs)
    def minerList():
        for num in range(4600000, 4713993):#4713877):
            print(num)
            a = []
            a.append(w3.block(num)["miner"])
        fo = open("test.txt", "w")
        fo.write(str(a))
        fo.close()
    def getBalance(hashs):
        return web3.eth.getBalance(hashs)
    def checkAddress(hashs):
        return Web3.toChecksumAddress(hashs)

#w3.block("latest")
w3.blockNumber()
#w3.getTransaction("0xfB05FF4F0cA7940ED801AA164af81D40cB567a7F")
x = w3.getTransactionReceipt("0xaa2703c3ae5d0024b2c3ab77e5200bb2a8eb39a140fad01e89a495d73760297c")
print(x)
