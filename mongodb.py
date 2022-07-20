#Doc tutorial link of motor
#https://motor.readthedocs.io/en/stable/tutorial-asyncio.html

import motor.motor_asyncio

MONGO_DETAILS = "" #server
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.data
collection = database.get_collection("movies")

print(database)
print(collection.find_one())

async def do_count():
    n = await collection.count_documents({})
    print('%s documents in collection' % n)

loop = client.get_io_loop()
loop.run_until_complete(do_count()) #for mongodb motor

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
#https://www.w3schools.com/python/python_mongodb_getstarted.asp

import pymongo

myclient = pymongo.MongoClient("") #server
mydb = myclient["data"]
mycol = mydb["movies"]

myquery = { 'name':"Psycho" }
for x in mycol.find().sort("name",-1):
  print(x) #simple mongodb
