# -*-coding:utf-8-*-
import requests
import json
import urllib
import sqlite3
import time
def baidu_main():
    # https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=8511458
    # https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22348180
    # https://baike.baidu.com/starflower/api/starflowerrank?lemmaid = 1296433
    # https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=21506312
    # https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22414884
    # https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22348656
    # https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22293630
    # https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22351766
    # https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22375735
    urllist = ['https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=8511458',
               'https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22348180',
               'https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=1296433',
               'https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=21506312',
               'https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22414884',
               'https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22348656',
               'https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22293630',
               'https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22351766',
               'https://baike.baidu.com/starflower/api/starflowerrank?lemmaid=22375735',
               ]
    totalsore = []
    rank = []
    oriScore = []
    name = []
    for url in urllist:
        contents = urllib.urlopen(url).read()
        dir = json.loads(contents)
        totalsore.append(dir['totalScore'])
        rank.append(dir['thisWeek']['rank'])
        oriScore.append(int(dir['thisWeek']['oriScore']))
        name.append(dir["thisWeek"]['name'])
        # print(name)
       # print(totalsore,rank,oriScore)
    for t1 in totalsore:
        print t1
    print "_______"
    for t2 in rank:
        print t2
    print "_______"
    for t3 in oriScore:
        print t3
    print "_______"

def baidu_main2():
    urllist = ['https://baike.baidu.com/api/lemmapv?id=660f43d993afcce233fef145&r=0.7615193231413899',
               'https://baike.baidu.com/api/lemmapv?id=eff6467766dd8dc6dea07b20&r=0.13412410841730682',
               'https://baike.baidu.com/api/lemmapv?id=45bd8fd322fcb8b5b6d8106d&r=0.6895997189153935',
               'https://baike.baidu.com/api/lemmapv?id=0c0eaf1e1cf1994eb72e1c0f&r=0.9572715087586983',
               'https://baike.baidu.com/api/lemmapv?id=9a70359202d5793f51cdea2c&r=0.9942565501914258',
               'https://baike.baidu.com/api/lemmapv?id=114318e91b4e9eefe7939721&r=0.6826534175503027',
               'https://baike.baidu.com/api/lemmapv?id=d967b90381d7df4f4b39820a&r=0.2858301244740986',
               'https://baike.baidu.com/api/lemmapv?id=f39dc6c748af794179767936&r=0.03287641633525995',
               'https://baike.baidu.com/api/lemmapv?id=045b9b90b28d27880832d8cb&r=0.45941982277929316',
               ]
    name = []
    for url in urllist:
        contents = urllib.urlopen(url).read()
        dir = json.loads(contents)
        name.append(dir["pv"])
        # print(name)
    # print(totalsore,rank,oriScore)
    for t1 in name:
        print t1
baidu_main()
baidu_main2()