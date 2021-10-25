import requests
import json
from types import SimpleNamespace
import numpy as np
import CreateImage as ci
from imgurpython import ImgurClient, client
import pyimgur


id1 = ""
id2 = ""

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
  

    results = json.loads(response.text)
    
    price =  results["data"]["axies"]["results"][0]["auction"]["currentPrice"]
    price = price[0:len(price) - 10]
    price = float(price)/100000000
    price = '{0:.2g}'.format(price)
    price1 =  results["data"]["axies"]["results"][1]["auction"]["currentPrice"]
    price1 = price1[0:len(price1) - 10]
    price1 = float(price1)/100000000
    price1 = '{0:.2g}'.format(price1)
    axie = {
      "axie01": {
        "id": results["data"]["axies"]["results"][0]["id"],
        "name": results["data"]["axies"]["results"][0]["name"],
        "class": results["data"]["axies"]["results"][0]["class"],
        "breedcount": results["data"]["axies"]["results"][0]["breedCount"],
        "image": results["data"]["axies"]["results"][0]["image"],
        "price": results["data"]["axies"]["results"][0]["auction"]["currentPriceUSD"],
        "priceeth": str(price),
        "stats": {
          "hp": results["data"]["axies"]["results"][0]["stats"]["hp"],
          "speed": results["data"]["axies"]["results"][0]["stats"]["speed"],
          "skill": results["data"]["axies"]["results"][0]["stats"]["skill"],
          "morale": results["data"]["axies"]["results"][0]["stats"]["morale"]
        },
        "parts": {
          "eyes": results["data"]["axies"]["results"][0]["parts"][0]["name"],
          "ears": results["data"]["axies"]["results"][0]["parts"][1]["name"],
          "back": results["data"]["axies"]["results"][0]["parts"][2]["name"],
          "mouth": results["data"]["axies"]["results"][0]["parts"][3]["name"],
          "horn": results["data"]["axies"]["results"][0]["parts"][4]["name"],
          "tail": results["data"]["axies"]["results"][0]["parts"][5]["name"],
        }
      },
      "axie02": {
        "id": results["data"]["axies"]["results"][1]["id"],
        "name": results["data"]["axies"]["results"][1]["name"],
        "class": results["data"]["axies"]["results"][1]["class"],
        "breedcount": results["data"]["axies"]["results"][1]["breedCount"],
        "image": results["data"]["axies"]["results"][1]["image"],
        "price": results["data"]["axies"]["results"][1]["auction"]["currentPriceUSD"],
        "priceeth": price1,
        "stats": {
          "hp": results["data"]["axies"]["results"][1]["stats"]["hp"],
          "speed": results["data"]["axies"]["results"][1]["stats"]["speed"],
          "skill": results["data"]["axies"]["results"][1]["stats"]["skill"],
          "morale": results["data"]["axies"]["results"][1]["stats"]["morale"]
        },
        "parts": {
          "eyes": results["data"]["axies"]["results"][1]["parts"][0]["name"],
          "ears": results["data"]["axies"]["results"][1]["parts"][1]["name"],
          "back": results["data"]["axies"]["results"][1]["parts"][2]["name"],
          "mouth": results["data"]["axies"]["results"][1]["parts"][3]["name"],
          "horn": results["data"]["axies"]["results"][1]["parts"][4]["name"],
          "tail": results["data"]["axies"]["results"][1]["parts"][5]["name"],
        }
      }
    }
    global id1
    id1 = results["data"]["axies"]["results"][0]["id"]
    global id2
    id2 = results["data"]["axies"]["results"][1]["id"]
    return axie



def LinePost():
    url = "https://notify-api.line.me/api/notify"
    image1 = UploadImgur1()
    image2 = UploadImgur2()
    payload=f'message=https://marketplace.axieinfinity.com/axie/{id1}&imageFullsize={image1}&imageThumbnail={image1}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer 09sUzzKu85CfrIb1O585H0eQc0s9QOK6BCYJMSJYKld'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    payload=f'message=https://marketplace.axieinfinity.com/axie/{id2}&imageFullsize={image2}&imageThumbnail={image2}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer 09sUzzKu85CfrIb1O585H0eQc0s9QOK6BCYJMSJYKld'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def UploadImgur1():
  client_id = 'ed8f553709ab4c2'
  client_secret = '13d5b3c0181d1370b382fe56f8e2984b6f8d6eac'

  PATH1 = "D:/RangsitWork/axieNotify/axie01.png"
  im = pyimgur.Imgur(client_id)
  uploaded_image = im.upload_image(PATH1, title="axie01")
  return uploaded_image.link

def UploadImgur2():
  client_id = 'ed8f553709ab4c2'
  client_secret = '13d5b3c0181d1370b382fe56f8e2984b6f8d6eac'

  PATH1 = "D:/RangsitWork/axieNotify/axie02.png"
  im = pyimgur.Imgur(client_id)
  uploaded_image = im.upload_image(PATH1, title="axie02")
  return uploaded_image.link


ci.AxieImage(AxiePost()).GenImage()
LinePost()
