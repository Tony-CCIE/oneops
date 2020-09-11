import redis


def slowlog_get():
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    return (r.slowlog_get())

if __name__ == "__main__":
    slowlog_get()
