# Simple REST API

A minimal REST API built with FastAPI, demonstrating CRUD operations for users, products, and orders.  
Data is stored in memory (for simplicity).

## Live Demo

[https://simple-rest-api.onrender.com/docs](https://simple-rest-api.onrender.com/docs)

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic

## Local Installation

```bash
git clone https://github.com/romanp217/simple-rest-api.git
cd simple-rest-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

Then open `http://127.0.0.1:8001/docs`.

## API Endpoints

| Method | Endpoint   | Description          |
|--------|------------|----------------------|
| GET    | /users     | List all users       |
| POST   | /users     | Create a new user    |
| GET    | /products  | List all products    |
| POST   | /products  | Create a product     |
| GET    | /orders    | List all orders      |
| POST   | /orders    | Create an order      |

## Deployment

Deployed on [Render](https://render.com).  
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `./start.sh`

The `start.sh` script runs:
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## License

MIT
