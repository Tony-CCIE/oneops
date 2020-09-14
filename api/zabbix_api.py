from pyzabbix import ZabbixAPI


class Zabbix:
    def __init__(self, url, user, password):
        self.zb = ZabbixAPI(url)
        self.zb.login(user, password)

    def get_token(self):
        # auth = self.zb.login(user, password)
        return self.zb.auth

    def hosts_all(self):
        data = self.zb.host.get(output=["hostid", "host"], selectInterfaces=["ip"])
        return data

    def host(self, host_id):
        data = self.zb.host.get(output=["host"], hostids=host_id)
        return data[0]['host']

    def ip(self, host_id):
        data = self.zb.host.get(output=["ip"], hostids=host_id, selectInterfaces=["ip"])
        return data[0]["interfaces"][0]["ip"]

    def cpu_idle(self, host_id):
        data = self.zb.item.get(output="extend", hostids=host_id, search={"key_": "system.cpu.util[,idle]"})
        if len(data):
            return (data[0]["lastvalue"] + ' %')
        else:
            return data

    def memory_usage(self, host_id):
        data = self.zb.item.get(output="extend", hostids=host_id, search={"key_": "vm.memory.size[available]"})
        if len(data):
            return ('{:.2f} GB'.format(float(data[0]["lastvalue"]) / 1024 / 1024 / 1024))
        else:
            return data

    def net_in(self, host_id):
        data = self.zb.item.get(output="extend", hostids=host_id, search={"key_": "net.if.in[eth0]"})
        if len(data):
            return ('{:.2f} Kbps'.format(float(data[0]["lastvalue"]) / 1000))
        else:
            return data

    def net_out(self, host_id):
        data = self.zb.item.get(output="extend", hostids=host_id, search={"key_": "net.if.out[eth0]"})
        if len(data):
            return ('{:.2f} Kbps'.format(float(data[0]["lastvalue"]) / 1000))
        else:
            return data


# if __name__ == "__main__":
#     z1 = Zabbix()
#     print(z1.hosts_all())
#     print(z1.host())
#     print(z1.ip())
#     print(z1.cpu_usage())
#     print(z1.memory_usage())
#     print(z1.net_in())
#     print(z1.net_out())

# @router.get("/zabbix/token/")

# @router.get("/zabbix/host/list/")

# @router.get("/zabbix/{host_id}/cpu/")

# @router.get("/zabbix/{host_id}/memory/")

# @router.get("/zabbix/{host_id}/net_in/")

# @router.get("/zabbix/{host_id}/net_out/")

