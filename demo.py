import pymongo

class mongo:
    def test():
        #for backup setting
        backclient = pymongo.MongoClient("mongodb://192.168.51.202:27017")
        backdb = backclient["tb"]
        backcol = backdb["tb"]
        #for target setting
        targetclient = pymongo.MongoClient("mongodb://192.168.51.212:27017")
        targetdb = targetclient["tb"]
        targetcol = targetdb["tb"]
        backfile = backcol.find()
        for file in backfile:
            print(file)
            targetcol.insert_one(file)
mongo.test()

