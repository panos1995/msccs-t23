from DB import DB
from Reader import Reader
from twitter_api import twitter_api
from MongoCollection import MongoCollection
import json

#traincollection = MongoCollection('Training')
#trainlabelid=traincollection.return_ids_list()
#print(repr(len(trainlabelid))+'--ok')
coll=MongoCollection('Training_token')
#coll.find_text_by_id('243374590288592896')
coll.return_train_dic()
#Tweet=MongoCollection('Tweets')

#dic={}
#for id in trainlabelid:
#   dic.setdefault(id,[]).append([[traincollection.return_catmatrix_by_id(id)]])#Tweet.return_tokenizers_by_id(id)
#print('total documents:'+repr(len(dic)))

#twitter=twitter_api("IHpSjYd5AuCdDRZTaGiMOwHUJ", "FNUvxez9N9vBzY72HiZcukHQqVqO0ZiV498qyaYDxaV5nKFSgu",traincollection)
#coll.insert(twitter.list_from_ids(trainlabelid))







