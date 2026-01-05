from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse

app=FastAPI()
 
contacts=[
    {
        'id':1,
        'name':'john',
        'phone':6084629198
    },
    {
        'id':2,
        'name':'choti',
        'phone':1234567890
    }
]

@app.post('/add/contact')
async def add_contact(request:Request):
    data=await request.json()#{'id':3,'name':'kanappa','phone':564743723}
    contacts.append(data)
    return contacts


@app.get('/contacts')
def get_all_contacts():
    return  contacts

@app.get('/contacts')
def get_contact(contact_id):
    for c in contacts:
        if c['id']==int(contact_id):
            return c
        return "no such contact"
    
@app.put('/contact')
async def update_task(request:Request):
    data=await request.json()
    for c in contacts:
        if c['id']==data['id']:
            c.update(data)
            return contacts
        return "no such contact"
    
@app.delete('/contact/{contact_id}')
def delete_contact(contact_id):
    for c in contacts:
        if c['id']==int(contact_id):
            contacts.remove(c)
            return contacts
        return "no such contact"  