from fastapi import FastAPI

app=FastAPI()
@app.get("/details")
def get_details():
    
    return{
        "name":"john",
        "age":30
    }