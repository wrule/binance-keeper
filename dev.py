#!/opt/homebrew/bin/python3
import yaml
import requests
from binance.spot import Spot

secret = yaml.safe_load(open('.secret.yaml', 'r'))

def main():
  print('你好，世界')
  # r = requests.get('https://www.baidu.com')
  # print(r.status_code)
  client = Spot(secret['APIKEY'], secret['APISECRET'])
  # Get account information
  print(client.account())


if __name__ == '__main__':
  main()
