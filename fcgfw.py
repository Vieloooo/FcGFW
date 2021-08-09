#!/usr/bin/env python3
"""
Author : vielo 
Date   : 2021-08-09
Purpose: Rock the Casbah
"""

import argparse
import json
import requests


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='config manager',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('function',
                        type=str,
                        metavar='optcode',
                        help='positional function')

    parser.add_argument('-u',
                        '--url',
                        help='subscribe url',
                        metavar='xxxurl',
                        type=str)

    parser.add_argument('-n',
                        '--name',
                        help='nickname for url',
                        metavar='nickname',
                        default='config',
                        type=str)

    return parser.parse_args()

#---------------------------------------------------
def fetchConfig(url,nickname):
    r= requests.get(url)
    configFileName = nickname+".jpg"
    fh = open("./configs/"+configFileName,'wb')
    fh.write(r.content)
    fh.close()
    print("fetching new subscription success")
    return configFileName
# --------------------------------------------------
def main():

    args = get_args()
    myurl = args.url
    nickname = args.name
    fc = args.function
    funcList = {"subscribe","checkout","update","rm","list"}
    if fc in funcList:
        subList = open("sublist.json",'r')
        configlist = json.load(subList)
        # defer sbuList.close 
        fetchConfig(myurl, nickname)
    else:
        print(f'function must in "{funcList}"')
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
