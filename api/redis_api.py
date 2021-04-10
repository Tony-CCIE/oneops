import redis


class Redis:
    def __init__(self, host, port, password, db=0):
        self.client = redis.StrictRedis(host=host, port=port, password=password)

    def get_key(self, key):
        if self.client.exists(key):
            return self.client.get(key)
        else:
            return None

    def get_SlowLog(self):
        return self.client.slowlog_get()

    def cluster_name(self):
        return self.client.info()['role']


if __name__ == "__main__":
    c = Redis(host="127.0.0.1", port=6379, password="password@123")
    print(c.get_key("hello"))
    print(c.get_SlowLog())
    print(c.cluster_name())
