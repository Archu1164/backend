from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse


from supabase import create_client

db_url="https://wuzbkduokbsetocfiqqg.supabase.co"
db_key="sb_publishable_POuGyV7YL4ahSjbLh8kxlg__YoAhUQi"

db=create_client(db_url,db_key)
app=FastAPI()
 


@app.post('/add/contact')
async def add_contact(request:Request):
    data=await request.json()#{'id':3,'name':'kanappa','phone':564743723}
    result=db.table('contacts').insert(data).execute().data
    return "success"


@app.get('/contacts')
def get_all_contacts():
    result=db.table('contacts').select('*').execute()
    
    return result.data

@app.get('/contact/{contact_id}')
def get_contact(contact_id:int):
    result=db.table('contacts').select('*').eq('id',contact_id).execute()
    return result.data

@app.put('/contact/{contact_id}')
async def update_contact(request:Request,contact_id:int):
    data=await request.json()
    result=db.table('contacts').update(data).eq('id',contact_id).execute()
    return "updated successfully"
    
@app.delete('/contact/{contact_id}')
def delete_contact(contact_id:int):
   result=db.table('contacts').delete().eq('id',contact_id).execute()
   return "Deleted successfully"