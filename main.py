from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from resources import redis_data, zabbix_data, rabbitmq_data

app = FastAPI()
app.include_router(zabbix_data.router)
app.include_router(redis_data.router)
app.include_router(rabbitmq_data.router)

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello_world():
    return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True, debug=True)
