'''
Copyright (c) 2021 ABLECLOUD Co. Ltd
이 파일은 Wall VM을 구성할 때 필요한 서비스를 시작하는 프로그램입니다.
최초 작성일 : 2021. 09. 03
'''

#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sh import systemctl
import argparse
from ablestack import *
import json
import sys


def parseArgs():
    parser = argparse.ArgumentParser(description='Prometheus Yaml file parsing and replace targets',
                                     epilog='copyrightⓒ 2021 All rights reserved by ABLECLOUD™')

    parser.add_argument('action', choices=[
                        'start', 'stop'], help='choose one of the actions')
    parser.add_argument('--service', metavar='name', type=str,
                        nargs='*', help='want to start service name')

    return parser.parse_args()


def startServices(service):
    print(systemctl('enable', '--now', service))


def stopServices(service):
    print(systemctl('disable', '--now', service))


def main():
    args = parseArgs()

    if (args.action) == 'start':
        try:
            startServices(args.service)
            ret = createReturn(code=200, val="services are started")
            print(json.dumps(json.loads(ret), indent=4))

        except Exception as e:
            ret = createReturn(code=500, val="fail to start service")
            print(json.dumps(json.loads(ret), indent=4))

    elif (args.action) == 'stop':
        try:
            stopServices(args.service)
            ret = createReturn(code=200, val="services are stopped")
            print(json.dumps(json.loads(ret), indent=4))

        except Exception as e:
            ret = createReturn(code=500, val="fail to stop service")
            print(json.dumps(json.loads(ret), indent=4))

    return ret


if __name__ == "__main__":
    main()