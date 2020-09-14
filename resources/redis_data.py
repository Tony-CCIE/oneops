from fastapi import APIRouter
from api.redis_api import Redis

router = APIRouter()

r = Redis(host="127.0.0.1", port=6379, password="password@123")


@router.get("/redis/slowlog/")
def redis_slowlog():
    return r.get_slowlog()
