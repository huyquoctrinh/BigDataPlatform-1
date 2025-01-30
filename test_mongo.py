import pymongo

myclient = pymongo.MongoClient("mongodb://admin:admin123@localhost:27017/")
dblist = myclient.list_database_names()

def insert_record(
    collection_name: str,
    update: dict
):
    mydb = myclient["mimic-data"]
    collection = mydb[collection_name]
    collection.insert_one(update)

# print(dblist)
# myclient.create_database("mimic-data")

mydb = myclient["mimic-data"]
list_collection = mydb.list_collection_names()
print(list_collection)
list_record = mydb["audio_metadata"]
# print(list_record)
for x in list_record.find():
    print(x)

# mock_data = {
#     'audio_id': "001",
#     'filename': "123.wav",
#     'save_url': "http://minio:9000/mimic-data/123.wav",
#     'db_rate': "6",
#     'status': "normal",
#     'device': "fan",
# }

# insert_record("audio_metadata", mock_data)

# users_collections = mydb["users"]
# print(mydb.list_collection_names())

# for x in users_collections.find():
#     print(x)

# # dblist = myclient.list_database_names()
# # print(dblist)
# # users_collections = myclient.users


# mock_data ={
#     "email": "mock@gmail.com",
#     "full_name": "Trinh Quoc Huy",
#     "user_type": "premium",
#     "paid": True,
#     "created_at": "2021-01-01",
# }

# users_collections.insert_one(mock_data)