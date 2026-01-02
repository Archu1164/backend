from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse

app=FastAPI()
 
persons=[
    {
        'account_id':1,
        'name':'john',
        'balance':400
    },
    {
        'account_id':2,
        'name':'kamal',
        'balance':600
    }
]

#get all persons
@app.get("/persons")
def get_all_persons():
    return persons

#get person by account_id
@app.get("/person/{account_id}")
def get_person_by_id(account_id:int):
    for p in persons:
        if p['account_id']==account_id:
            return p
    return "no such data"

#get person by name
@app.get("/person/name/{name}")
def get_person_by_name(name:str):
    result=[p for p in persons if name.lower() in p['name'].lower()]
    return result

#Credit amount to an account_id
@app.post("/credit")
async def credit_amount(request:Request):
    data=await request.json()
    for p in persons:
        if p['account_id']==data['account_id']:
            p['balance']+=data['amount']
            return p
        return{"message":"account not found"}
    
# Withdraw amount from an account_id
@app.post("/withdraw")
async def withdraw_amount(request:Request):
    data=await request.json()
    for p in persons:
        if p['account_id']==data['account_id']:
            p['balance']-=data['amount']
            return p
    return "account not found"

## Transfer amount from one acc to another acc

@app.post("/transfer")
async def transfer_amount(request:Request):
    data=await request.json()
    for p in persons:
        if p['account_id']==data['from_account']:
            p['balance']-=data['amount']
            
        if p['account_id']==data['to_account']:
            p['balance']+=data['amount']    
            
    return {"message":"transfer done","persons":persons}
