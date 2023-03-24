"""Main API routes"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import Database

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
    plant = {}
    match type:
        case "echeveria":
            plant = Database.get_product(1)
        case "snakeplant":
            plant = Database.get_product(2)
        case "moneytree":
            plant = Database.get_product(3)
        case "pothos":
            plant = Database.get_product(4)
        case "cactus":
            plant = Database.get_product(5)
        case "airplant":
            plant = Database.get_product(6)
    print(plant)
    return templates.TemplateResponse("product.html", {"request": request, "img": type, "plant": plant})

@app.get('/cart/', response_class=HTMLResponse)
def get_cart(request: Request):
    """Shop page"""
    return templates.TemplateResponse("cart.html", {"request": request})

@app.get('/contact/', response_class=HTMLResponse)
def get_contact(request: Request):
    """Shop page"""
    return templates.TemplateResponse("contact.html", {"request": request})
