from fastapi import Cookie
from fastapi import FastAPI
from fastapi import Form
from fastapi import Request
from fastapi import Response

from phone import get_formatted_phone


app = FastAPI()


@app.post("/unify_phone_from_json")
async def format_phone(request: Request) -> Response:
    number = await request.json()
    return Response(get_formatted_phone(number['phone']), media_type="text/html")

@app.post("/unify_phone_from_form")
async def format_phone_form(phone: str = Form()) -> Response:
    return Response(get_formatted_phone(phone), media_type="text/html")

@app.get("/unify_phone_from_query")
async def format_phone_query(phone: str) -> Response:
    return Response(get_formatted_phone(phone), media_type="text/html")

@app.get("/unify_phone_from_cookies")
async def format_phone_cookie(phone: str = Cookie()) -> Response:
    return Response(get_formatted_phone(phone), media_type="text/html")
