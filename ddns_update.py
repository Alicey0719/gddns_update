from requests.auth import HTTPBasicAuth
import requests
import json
import datetime

def saveLog(path, msg):
    with open(path, 'a', encoding='UTF-8') as logfile:
        logfile.write(str(datetime.datetime.now()) + " : " + msg + "\n")

def getData(path):
    ## json形式のファイルを読み込む
    with open(path, 'r') as dat:
        return json.load(dat)

def main():
    ## path
    LOG_PATH = "./log.txt"
    POST_PATH = 'https://domains.google.com/nic/update'

    ## 情報をファイルから読み出す
    path = './data.json'
    dat = getData(path)
    #print(dat)

    ##送信先に要求をPOSTする
    auth = HTTPBasicAuth(dat['user']['username'], dat['user']['password'])
    params = dat['host']
    #print(params)
    res = requests.post(POST_PATH, auth=auth, params=params)
    print(res.text)

    ## Log保存
    saveLog(LOG_PATH, str(res.status_code) + ' : ' + res.text + ' : '+ res.url)
    

if __name__ == "__main__":
    main()