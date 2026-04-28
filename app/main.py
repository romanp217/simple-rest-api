from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Simple REST API", description="A basic API for users, products, and orders", version="1.0.0")

# --- In-memory databases ---
users_db = []
products_db = []
orders_db = []

# --- Pydantic models (validation) ---
class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

class Order(BaseModel):
    id: Optional[int] = None
    user_id: int
    product_id: int
    quantity: int

# --- Helper to get next ID ---
def next_id(db: List) -> int:
    return max([item.id for item in db], default=0) + 1

# --- Users endpoints ---
@app.get("/users", response_model=List[User])
def get_users():
    return users_db

@app.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    user.id = next_id(users_db)
    users_db.append(user)
    return user

# --- Products endpoints ---
@app.get("/products", response_model=List[Product])
def get_products():
    return products_db

@app.post("/products", response_model=Product, status_code=201)
def create_product(product: Product):
    product.id = next_id(products_db)
    products_db.append(product)
    return product

# --- Orders endpoints ---
@app.get("/orders", response_model=List[Order])
def get_orders():
    return orders_db

@app.post("/orders", response_model=Order, status_code=201)
def create_order(order: Order):
    # basic validation: user and product exist (optional but good practice)
    user_exists = any(u.id == order.user_id for u in users_db)
    product_exists = any(p.id == order.product_id for p in products_db)
    if not user_exists or not product_exists:
        raise HTTPException(status_code=400, detail="Invalid user_id or product_id")
    order.id = next_id(orders_db)
    orders_db.append(order)
    return order
