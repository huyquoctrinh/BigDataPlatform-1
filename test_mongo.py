import pymongo

myclient = pymongo.MongoClient("mongodb://admin:admin123@localhost:27017/")
dblist = myclient.list_database_names()
print(dblist)

# mydb = myclient["mydatabase"]

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