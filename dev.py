#!/opt/homebrew/bin/python3
import yaml

secret = yaml.safe_load(open('.secret.yaml', 'r'))

def main():
  print('你好，世界')

if __name__ == '__main__':
  main()
