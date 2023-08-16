from fastapi import APIRouter
from src.models import User
from src.config import session

app = APIRouter()


@app.get('/stock-passwords')
def get_stock_passwords():
    output = User().generate_passwords()
    session.commit()
    return output
