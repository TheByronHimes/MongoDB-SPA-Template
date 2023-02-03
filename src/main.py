from fastapi import FastAPI

# To run container locally: docker run -d -p 8000:80 <image name>
# To build/run container with docker-compose: 
#   docker-compose up --build

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "hello world!"}