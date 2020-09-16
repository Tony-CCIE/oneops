from fastapi import APIRouter
from api.rabbitmq_api import RabbitMQ

router = APIRouter()

ra = RabbitMQ(host_name="127.0.0.1")


@router.get("/rabbitmq/healthchecks/node", tags=["rabbitmq"])
def check_node():
    return ra.healthchecks_nodes()

