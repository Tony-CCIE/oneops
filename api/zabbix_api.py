from pyzabbix import ZabbixAPI


class Zabbix:
    def __init__(self, url, user, password):
        self.zb = ZabbixAPI(url)
        self.zb.login(user, password)

    def get_token(self):
        # auth = self.zb.login(user, password)
        return self.zb.auth

    def host(self, host_id):
        data = self.zb.host.get(output=["host"], hostids=host_id)
        return data[0]['host']


if __name__ == "__main__":
    z1 = Zabbix(url='http://10.157.27.56/zabbix/api_jsonrpc.php', user="*", password="password@123")


