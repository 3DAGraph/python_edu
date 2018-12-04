import pymongo

class mongo:
    def test():
        myclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
        mydb = myclient["tb"]
        mycol = mydb["tb"]
        mycol.insert_one({"miner":"123"})
        x = mycol.find()
        for d in x:
            print(d)

mongo.test()

