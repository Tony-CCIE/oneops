from fastapi import FastAPI
import uvicorn
from resources import redis_data, zabbix_data

app = FastAPI()
app.include_router(zabbix_data.router)
app.include_router(redis_data.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True, debug=True)
