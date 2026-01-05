from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse

app=FastAPI()

@app.get('/json')
def get_details():
    data={
        'name':'john',
        "age":30
    }
    return JSONResponse(data)

# @app.get("/html")
# def get_html():
#     html= '''
#     <!DOCTYPE html>
#     <html>

#     <head>
#     <title>Page Title</title>
#     </head>

    
#     <body>

#         <h2>Login Form</h2>

#         <form action="/submit_page" method="POST">
#           <label for="username">Username:</label><br>
#           <input type="text" id="username" name="username"><br>
#           <label for="password">Password:</label><br>
#           <input type="password" id="password" name="password"><br><br>
#           <input type="submit" value="Submit">
#         </form>

    
#     </body>

#     </html>
    
#     '''
   # return HTMLResponse(html)

@app.get('/redirect')
def get_redirect():
    url="https://en.wikipedia.org/wiki/Netflix/"
    return RedirectResponse(url,status_code=302)

#read query parameter
@app.get("/submit")
def save_data(name,age):
    return JSONResponse({
        'message':f"Hello {name},your age is {age}"
    })
    
   #read path paramaeter 
@app.get("/{name}/details")
def save_data(name):
    return JSONResponse({
        'message':f"Hello {name}"
    })
    
@app.get("/submit")
def save_data(name):
    return JSONResponse({
        'message:f"Hello {name}'
    })
  
  
#Read Payload    
@app.post("/submit")
async def save_data(request:Request):
    data=await request.json()
    print(data)
    return data
        
        
        
    