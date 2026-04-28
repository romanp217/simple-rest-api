# Simple REST API

A basic REST API built with **FastAPI** for managing users, products, and orders.  
Includes in-memory storage, Pydantic validation, and automatic interactive documentation.

🔗 **Live Demo**: [https://simple-rest-api-ifu8.onrender.com/docs](https://simple-rest-api-ifu8.onrender.com/docs)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-green)
![Render](https://img.shields.io/badge/Render-Deployed-brightgreen)

## 🚀 Features

- Full CRUD for **users**, **products**, and **orders** (in-memory)
- Automatic Swagger UI at `/docs`
- Request validation with Pydantic
- Error handling (e.g., invalid user/product IDs)
- Ready to deploy (includes `start.sh` for Render)

## 📖 API Endpoints

| Method | Endpoint     | Description             |
|--------|--------------|-------------------------|
| GET    | `/users`     | List all users          |
| POST   | `/users`     | Create a user           |
| GET    | `/products`  | List all products       |
| POST   | `/products`  | Create a product        |
| GET    | `/orders`    | List all orders         |
| POST   | `/orders`    | Create an order         |

Interactive documentation available at `/docs`.

## 🛠️ Local Installation

```bash
git clone https://github.com/romanp217/simple-rest-api.git
cd simple-rest-api
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
