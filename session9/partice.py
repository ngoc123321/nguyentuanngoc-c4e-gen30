import pymongo
client =pymongo.MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")
partice = client.test
a = {
    "title" : "word",
    "author" : "Ngoc",
    "content" : """
    hi everyone
"""
}
partice.posts.insert_one(a)
