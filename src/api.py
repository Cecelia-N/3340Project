"""Main API routes"""
from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import Database, name_to_id

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
Database.start_db()

@app.get('/', response_class=HTMLResponse)
def get_index(request: Request):
    """Home page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/shop/', response_class=HTMLResponse)
def get_shop(request: Request):
    """Shop page"""
    return templates.TemplateResponse("shop.html", {"request": request})

@app.get('/product/{type}', response_class=HTMLResponse)
def get_product(request: Request, type: str):
    """Product page"""
    plant = Database.get_product(name_to_id(type))
    return templates.TemplateResponse("product.html", {"request": request, "type": type, "plant": plant})

@app.get('/checkout/', response_class=HTMLResponse)
def get_cart(request: Request):
    """Shop page"""
    return templates.TemplateResponse("checkout.html", {"request": request})

@app.get('/contact/', response_class=HTMLResponse)
def get_contact(request: Request):
    """Shop page"""
    return templates.TemplateResponse("contact.html", {"request": request})

@app.post('/checkout/')
async def process_order(request: Request):
    """Order processing"""
    body = await request.json()
    print(f"Order recieved\nName: {body['name']}\nEmail: {body['email']}\nPhone: {body['phone']}")
    items = {
        "echeveria": body['echeveria'], 
        "snakeplant": body['snakeplant'], 
        "moneytree": body['moneytree'], 
        "pothos": body['pothos'],
        "cactus": body['cactus'],
        "airplant": body['airplant'],
    }
    for name, amount_str in items.items():
        amount = int(amount_str)
        if amount > 0:
            print(f"{name}: {amount}")
            for i in range(0, amount):
                Database.sell(name_to_id(name))
