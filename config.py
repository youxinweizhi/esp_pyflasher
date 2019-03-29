import configparser  # 配置文件

config = configparser.ConfigParser()
"""生成configparser配置文件 ，字典的形式"""
"""第一种写法"""
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
"""第二种写法"""
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
"""第三种写法"""
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here

config['DEFAULT']['ForwardX11'] = 'yes'
"""写入后缀为.ini的文件"""
with open('example.ini', 'w') as configfile:
    config.write(configfile)

import configparser  # 配置文件

config = configparser.ConfigParser()
config.read("example.ini")

print(config.defaults())

print("所有节点==>", config.sections())
