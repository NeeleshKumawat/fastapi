from fastapi import FastAPI, Depends

app = FastAPI()

def common_logic():
    return {"message": "This is common logic"}

@app.get("/home")
def home(data= Depends(common_logic)):
    return data
