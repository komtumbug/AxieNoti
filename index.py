import requests
import json
from types import SimpleNamespace
import numpy as np
import CreateImage as ci

def AxiePost():
    url = "https://axieinfinity.com/graphql-server-v2/graphql"
    payload = json.dumps({
  "operationName": "GetAxieBriefList",
  "query": "query GetAxieBriefList($auctionType: AuctionType, $criteria: AxieSearchCriteria, $from: Int, $sort: SortBy, $size: Int, $owner: String) {\naxies(auctionType: $auctionType, criteria: $criteria, from: $from, sort: $sort, size: $size, owner: $owner) {\n  total\n  results {\n    ...AxieBrief\n    __typename\n  }\n  __typename\n}\n      }\n\n      fragment AxieBrief on Axie {\nid\nname\nstage\nclass\nbreedCount\nimage\ntitle\ngenes\nbattleInfo {\n  banned\n  __typename\n}\nauction {\n  currentPrice\n  currentPriceUSD\n  __typename\n}\nstats {\n  ...AxieStats\n  __typename\n}\nparts {\n  id\n  name\n  class\n  type\n  specialGenes\n  __typename\n}\n__typename\n      }\n    \n      fragment AxieStats on AxieStats {\n       hp\n       speed\n       skill\n       morale\n__typename\n      }",
  "variables": {
    "auctionType": "Sale",
    "criteria": {
      "classes": [
        "Dusk"
      ],
      "parts": [
        "mouth-tiny-turtle",
        "mouth-tiny-carrot",
        "mouth-dango",
        "horn-cerastes",
        "horn-vector",
        "back-bone-sail",
        "back-rugged-sail",
        "tail-grass-snake"
      ],
      "hp": None,
      "speed": None,
      "skill": None,
      "morale": None,
      "breedCount": None,
      "pureness": [],
      "numMystic": [],
      "title": None,
      "region": None,
      "stages": [
        3,
        4
      ]
    },
    "from": 0,
    "size": 12,
    "sort": "PriceAsc",
    "owner": None
    }})
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    results = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))

    auctions = results.data.axies.results
    arrauction = []
    index = 0
    for i in auctions:
        arrauction.append(i.auction)
        print(arrauction[index])
        index +=1
    return arrauction

def LinePost():
    url = "https://notify-api.line.me/api/notify"

    payload='message=EIEI&imageFullsize=https://storage.googleapis.com/assets.axieinfinity.com/axies/7479197/axie/axie-full-transparent.png&imageThumbnail=https://storage.googleapis.com/assets.axieinfinity.com/axies/7479197/axie/axie-full-transparent.png'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer 09sUzzKu85CfrIb1O585H0eQc0s9QOK6BCYJMSJYKld'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

LinePost()