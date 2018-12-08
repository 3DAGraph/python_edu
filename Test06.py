import threading
import binascii
import pymongo
import json
import sys


#from contract.Sol import Solidity
#from transaction.sign import Sign
#from contract.contract import Contract
#from lib.Web3 import w3
from web3 import Web3, HTTPProvider

#w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/"))
#w3 = Web3(Web3.HTTPProvider("http://192.168.51.203:19999"))
from test import *

def block_data():
    myclient = pymongo.MongoClient("mongodb://192.168.51.212:27017")
    mydb = myclient["TestDB06"]
    mycol = mydb["ETHblockinfo06"]

    for i in range(5000001,5100000):
        print(i)
        transactionArray = []
        blockResult = w3.block(i)
        #print("block:",blockResult)
        for tx in blockResult["transactions"]:
            txResult = binascii.hexlify(tx).decode() 
            print("txResult:",txResult)
        
            transactionResult = w3.getTransactionReceipt(txResult)
            
            transactionJson={
                        'blockHash':binascii.hexlify(transactionResult["blockHash"]).decode(),
                        'blockNumber':transactionResult["blockNumber"],
                        'contractAddress':transactionResult["contractAddress"],
                        'cumulativeGasUsed':transactionResult["cumulativeGasUsed"],
                        'from':transactionResult["from"],
                        'gasUsed':transactionResult["gasUsed"],
                        'logs':transactionResult["logs"],
                        'logsBloom':binascii.hexlify(transactionResult["logsBloom"]).decode(),
                        #'root':transactionResult["root"],
                        'to':transactionResult["to"],
                        'transactionHash':binascii.hexlify(transactionResult["transactionHash"]).decode(),
                        'transactionIndex':transactionResult["transactionIndex"]
                        }
            #print(transactionJson)
            transactionArray.append(transactionJson)#{"transactions":transactionJson})
        if(len(transactionArray)>0):
            mycol.insert_many(transactionArray)

def insertBlock():
    myclient = pymongo.MongoClient("mongodb://192.168.51.212:27017")
    mydb = myclient["TestDB06"]
    #mycol = mydb["ETHBlock06"]
    mycol = mydb["b1"]
    for i in range(5000001,5000050):
        blockResult = w3.block(i)
        #print(blockResult)
        trans = []
        for r in blockResult["transactions"]:
            trans.append(binascii.hexlify(r).decode())
        unc = []
        for r in blockResult["transactions"]:
            unc.append(binascii.hexlify(r).decode())

        block = {
                'number':blockResult['number'],
                'timestamp':blockResult['timestamp'],
                'transactions':trans,#blockResult['transactions'],
                'uncles':unc,#blockResult['uncles'],
                'hash':blockResult['hash'],
                'miner':blockResult['miner']
        }
        #print(i)
        #db.blockInfo.find().sort({"number":-1}).limit(1)
        try:
            mycol.insert(block)
        except:
            print("error key")


def insertTransactionData():
    myclient = pymongo.MongoClient("mongodb://192.168.51.212:27017")
    mydb = myclient["TestDB06"]
    #blockinfo = mydb["ETHBlock06"]
    #transinfo = mydb["ETHtransactioninfo06"]
    blockinfo = mydb["b1"]
    transinfo = mydb["b2"]
    for i in range(5000001,5000050):
        print(i)
        transactionArray = []
        blockResult = blockinfo.find_one({"number":i})
        #print(blockResult)

        for tx in blockResult["transactions"]:
            transactionResult = w3.getTransactionReceipt(tx)
            trans = {
                'blockHash':binascii.hexlify(transactionResult["blockHash"]).decode(),
                'blockNumber':transactionResult["blockNumber"],
                'contractAddress':transactionResult["contractAddress"],
                'cumulativeGasUsed':transactionResult["cumulativeGasUsed"],
                'from':transactionResult["from"],
                'gasUsed':transactionResult["gasUsed"],
                'logs':transactionResult["logs"],
                'logsBloom':binascii.hexlify(transactionResult["logsBloom"]).decode(),
                #'status':transactionResult["status"],
                'to':transactionResult["to"],
                'transactionHash':binascii.hexlify(transactionResult["transactionHash"]).decode(),
                'transactionIndex':transactionResult["transactionIndex"]
            }
            try:
                transinfo.insert(trans)
            except:
                print("exist key")
            
#def main():
if __name__ == '__main__':

    t1 = threading.Thread(target=insertBlock())
    t1.start()

    t2 = threading.Thread(target=insertTransactionData())
    t2.start()

    #block_data()
    insertBlock()
    insertTransactionData()

#main()

