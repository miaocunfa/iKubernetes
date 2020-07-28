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
from ruamel.yaml import YAML

yaml = YAML()

def create_service_yaml(service_name, tag, ports):

    service_mould_file = "mould/info-service-mould.yaml"
    isServiceMould = os.path.isfile(service_mould_file)

    if isServiceMould:
        # read Service-mould yaml convert json
        with open(service_mould_file, encoding='utf-8') as yaml_obj:
            service_data = yaml.load(yaml_obj)

        # Update jarName
        service_data['metadata']['name'] = service_name
        service_data['metadata']['labels']['serviceName'] = service_name
        service_data['metadata']['labels']['tag'] = tag
        service_data['spec']['selector']['serviceName'] = service_name

        # Update port
        new_spec_ports = []
        for port in ports:
            port = int(port)
            portname = 'port' + str(port)
            new_port = {'name': portname, 'port': port, 'targetPort': port}
            new_spec_ports.append(new_port)
        service_data['spec']['ports'] = new_spec_ports

        # json To service yaml
        save_file = tag + '/' + service_name + '_svc.yaml'
        with open(save_file, mode='w', encoding='utf-8') as yaml_obj:
            yaml.dump(service_data, yaml_obj)

        print(save_file + ": Success!")
    else:
        print("Service Mould File is Not Exist!")


def create_deploy_yaml(service_name, tag):

    cpuRequest = "50m"
    memoryRequest = "100Mi"
    cpuLimit = "500m"
    memoryLimit = "1000Mi"

    deploy_mould_file = "mould/info-deploy-mould.yaml"
    isDeployMould = os.path.isfile(deploy_mould_file)

    if isDeployMould:
        with open(deploy_mould_file, encoding='utf-8') as yaml_obj:
            deploy_data = yaml.load(yaml_obj)

        # Update jarName
        deploy_data['metadata']['name'] = service_name
        deploy_data['metadata']['labels']['serviceName'] = service_name
        deploy_data['spec']['selector']['matchLabels']['serviceName'] = service_name
        deploy_data['spec']['template']['metadata']['labels']['serviceName'] = service_name  

        # Update containers
        image = "reg.test.local/library/" + service_name + ":" + tag
        #resources = { "requests": {"cpu": cpuRequest, "memory": memoryRequest }, "limits": {"cpu": cpuLimit, "memory": memoryLimit } }
        resources = { "requests": {"memory": memoryRequest }, "limits": {"memory": memoryLimit } }
        new_containers = [{'name': service_name, 'image': image, 'resources': resources}]
        deploy_data['spec']['template']['spec']['containers'] = new_containers

        # Update affinity
        matchExpressions = [{'key': 'serviceName', 'operator': 'In', 'values': [service_name]}]
        deploy_data['spec']['template']['spec']['affinity']['podAntiAffinity']['preferredDuringSchedulingIgnoredDuringExecution'][0]['podAffinityTerm']['labelSelector']['matchExpressions'] = matchExpressions

        # json To service yaml
        save_file = tag + '/' + service_name + '_deploy.yaml'
        with open(save_file, mode='w', encoding='utf-8') as yaml_obj:
            yaml.dump(deploy_data, yaml_obj)

        print(save_file + ": Success!")
    else:
        print("Deploy Mould File is Not Exist!")


def create_basic_yaml(service_name, tag):

    cpuRequest = "50m"
    memoryRequest = "100Mi"
    cpuLimit = "500m"
    memoryLimit = "1000Mi"

    basic_mould_file = "mould/info-basic-mould.yaml"
    isbasicMould = os.path.isfile(basic_mould_file)

    if isbasicMould:
        with open(basic_mould_file, encoding='utf-8') as yaml_obj:
            basic_data = yaml.load(yaml_obj)

        # Update jarName
        basic_data['metadata']['name'] = service_name
        basic_data['metadata']['labels']['serviceName'] = service_name
        basic_data['spec']['selector']['matchLabels']['serviceName'] = service_name
        basic_data['spec']['template']['metadata']['labels']['serviceName'] = service_name  

        # Update containers
        image = "reg.test.local/library/" + service_name + ":" + tag
        #resources = { "requests": {"cpu": cpuRequest, "memory": memoryRequest }, "limits": {"cpu": cpuLimit, "memory": memoryLimit } }
        resources = { "requests": {"memory": memoryRequest }, "limits": {"memory": memoryLimit } }
        new_containers = [{'name': service_name, 'image': image, 'resources': resources}]
        basic_data['spec']['template']['spec']['containers'] = new_containers

        # Update affinity
        matchExpressions = [{'key': 'serviceName', 'operator': 'In', 'values': [service_name]}]
        basic_data['spec']['template']['spec']['affinity']['podAntiAffinity']['preferredDuringSchedulingIgnoredDuringExecution'][0]['podAffinityTerm']['labelSelector']['matchExpressions'] = matchExpressions

        # json To service yaml
        save_file = tag + '/basic/' + service_name + '_basic_deploy.yaml'
        with open(save_file, mode='w', encoding='utf-8') as yaml_obj:
            yaml.dump(basic_data, yaml_obj)

        print(save_file + ": Success!")
    else:
        print("basic Mould File is Not Exist!")


services = {
	'info-gateway': {
		'ports': ['9999'],
		'isBasic': '1',
	},
	'info-admin': {
		'ports': ['7777'],
		'isBasic': '1',
	},
	'info-config': {
		'ports': ['8888'],
		'isBasic': '1',
	},
	'info-message-service': {
		'ports': ['8555', '9666'],
		'isBasic': '0',
	},
	'info-auth-service': {
		'ports': ['8666'],
		'isBasic': '0',
	},
	'info-scheduler-service': {
		'ports': ['8777'],
		'isBasic': '0',
	},
	'info-uc-service': {
		'ports': ['8800'],
		'isBasic': '0',
	},
	'info-ad-service': {
		'ports': ['8801'],
		'isBasic': '0',
	},
	'info-community-service': {
		'ports': ['8802'],
		'isBasic': '0',
	},
	'info-groupon-service': {
		'ports': ['8803'],
		'isBasic': '0',
	},
	'info-hotel-service': {
		'ports': ['8804'],
		'isBasic': '0',
	},
	'info-nearby-service': {
		'ports': ['8805'],
		'isBasic': '0',
	},
	'info-news-service': {
		'ports': ['8806'],
		'isBasic': '0',
	},
	'info-store-service': {
		'ports': ['8807'],
		'isBasic': '0',
	},
	'info-payment-service': {
		'ports': ['8808'],
		'isBasic': '0',
	},
	'info-agent-service': {
		'ports': ['8809'],
		'isBasic': '0',
	},
	'info-consumer-service': {
		'ports': ['8090'],
		'isBasic': '0',
	},
}

prompt = "\n请输入要生成的tag: "
answer = input(prompt)
print("")

if os.path.isdir(answer):
    raise SystemExit(answer + ': is Already exists!')
else:
    tag = answer
    os.makedirs(tag)
    os.makedirs(tag + '/basic')
    for service_name in services.keys():
        if services[service_name]['isBasic'] == '1':
            create_service_yaml(service_name, tag, services[service_name]['ports'])
            create_basic_yaml(service_name, tag)
        else:
            create_service_yaml(service_name, tag, services[service_name]['ports'])
            create_deploy_yaml(service_name, tag)

#create_deploy_yaml('info-message-service', '0.0.2')
#create_service_yaml('info-message-service', '0.0.2', ['8555', '9666'])
#create_basic_yaml('info-gateway', '0.0.2')
