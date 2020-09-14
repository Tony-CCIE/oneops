
from urllib import request
import logging
import json


class RabbitMQ:

    def __init__(self, user_name="guest", password="guest", host_name="", port=15672, protocol='http'):
        self.user_name = user_name
        self.password = password
        self.host_name = host_name
        self.port = port
        self.protocol = protocol

    def call_api(self, path):
        url = "{0}://{1}:{2}/api/{3}".format(self.protocol, self.host_name, self.port, path)
        password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, url, self.user_name, self.password)
        handler = request.HTTPBasicAuthHandler(password_mgr)
        logging.debug("Issue a rabbit API call to get data on" + path)
        return json.loads(request.build_opener(handler).open(url).read())

    def healthchecks_nodes(self):
        status = self.call_api("healthchecks/node")
        return status

# if __name__ == "__main__":
#     ra = RabbitMQ(host_name="127.0.0.1")
#     print(ra.healthchecks_nodes())

