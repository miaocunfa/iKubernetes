#!/usr/bin/python
# encoding: utf-8

"""
The Script for Auto Create Deployment Yaml.

File:               auto_create_deploy_yaml
User:               miaocunfa
Create Date:        2020-06-10
Create Time:        17:06
"""

import os

tag = "0.0.1-SNAPSHOT"
mould_file = "info-mould-deploy.yaml"

services = {
    'info-gateway':           ['9999'],
    'info-admin':                 ['7777'],
    'info-config':                ['8888'],
    'info-message-service':       ['8555', '9666'],
    'info-auth-service':          ['8666'],
    'info-scheduler-service':     ['8777'],
    'info-uc-service':            ['8800'],
    'info-ad-service':            ['8801'],
    'info-community-service':     ['8802'],
    'info-groupon-service':       ['8803'],
    'info-hotel-service':         ['8804'],
    'info-nearby-service':        ['8805'],
    'info-news-service':          ['8806'],
    'info-store-service':         ['8807'],
    'info-payment-service':       ['8808'],
    'info-agent-service':         ['8809'],
    'info-consumer-service':      ['8090'],
}

#isMould = os.path.exists(mould)
isMould = os.path.isfile(mould_file)

if isMould:
    for service_name, service_ports in services:
        with open(mould_file, 'r') as mould_object:
        mould_contents = mould_object.read()

        print(mould_contents)
