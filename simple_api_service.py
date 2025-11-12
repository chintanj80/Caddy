from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
async def read_header(request: Request):
    value = request.headers.get("x-my-header", "no header found")
    return {"header_value": value}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9090)