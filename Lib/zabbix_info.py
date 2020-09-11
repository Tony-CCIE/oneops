import requests
import json


# 登录，获取 token 值
url = 'http://10.157.27.56/zabbix/api_jsonrpc.php'
post_headers = {'Content-Type': 'application/json'}
post_data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "*",
        "password": "*"
    },
    "id": 1
}

result = requests.post(url, data=json.dumps(post_data), headers=post_headers)
token = result.json()["result"]

# 所有已配置主机的ID，主机名和接口
def host_ip():
    url = 'http://10.157.27.56/zabbix/api_jsonrpc.php'
    post_headers = {'Content-Type': 'application/json'}
    post_data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid", "host"],
            "selectInterfaces": ["ip"]
        },
        "id": 1,
        "auth": token
    }
    result = requests.post(url, data=json.dumps(post_data), headers=post_headers)
    return (result.json()["result"])

# system.cpu.util[,idle] 每分钟 CPU 使用率
# vm.memory.size[available]  使用内存（单位为Bit)
# net.if.in[eth0] bps 网口 in 流量
# net.if.out[eth0] 网口 out 流量

def cpu_usage(hostid):
    url = 'http://10.157.27.56/zabbix/api_jsonrpc.php'
    post_headers = {'Content-Type': 'application/json'}
    post_data = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": "extend",
            "hostids": hostid,
            "search": {
                "key_": "system.cpu.util[,idle]"
            }
        },
        "id": 1,
        "auth": token
    }
    r = requests.post(url, data=json.dumps(post_data), headers=post_headers)
    r = json.loads(r.text)
    r_result = r['result']
    if len(r_result):
        return (r_result[0]['lastvalue'] + "%")
    else:
        return ("result: []")

def memory_usage(hostid="10184"):
    url = 'http://10.157.27.56/zabbix/api_jsonrpc.php'
    post_headers = {'Content-Type': 'application/json'}
    post_data = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": "extend",
            "hostids": hostid,
            "search": {
                "key_": "vm.memory.size[available]"
            }
        },
        "id": 1,
        "auth": token
    }
    r = requests.post(url, data=json.dumps(post_data), headers=post_headers)
    r = json.loads(r.text)
    r_result = r['result']
    if len(r_result):
        return ('{:.2f} GB'.format(float(r_result[0]['lastvalue'])/1024/1024/1024))
    else:
        return ("result:[]")


def net_in(hostid):
    url = 'http://10.157.27.56/zabbix/api_jsonrpc.php'
    post_headers = {'Content-Type': 'application/json'}
    post_data = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": "extend",
            "hostids": hostid,
            "search": {
                "key_": ["net.if.in[eth0]"]
            }
        },
        "id": 1,
        "auth": token
    }
    r = requests.post(url, data=json.dumps(post_data), headers=post_headers)
    r = json.loads(r.text)
    r_result = r['result']
    if len(r_result):
        return ('{:.2f} Kbps'.format(float(r_result[0]['lastvalue'])/1000))
    else:
        return "result:[]"


def net_out(hostid):
    url = 'http://10.157.27.56/zabbix/api_jsonrpc.php'
    post_headers = {'Content-Type': 'application/json'}
    post_data = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": "extend",
            "hostids": hostid,
            "search": {
                "key_": "net.if.out[eth0]"
            }
        },
        "id": 1,
        "auth": token
    }
    r = requests.post(url, data=json.dumps(post_data), headers=post_headers)
    r = json.loads(r.text)
    r_result = r['result']
    if len(r_result):
        return ('{:.2f} Kbps'.format(float(r_result[0]['lastvalue'])/1000))
    else:
        return "result:[]"

if __name__ == "__main__":
   # cpu_usage(),\
   memory_usage(),\
   # ping(),
   host_ip()
   #  net_in()
