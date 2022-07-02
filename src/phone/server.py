from fastapi import Request
from fastapi import FastAPI
from fastapi import Response
from fastapi import Form

from phone import get_formatted_phone


app = FastAPI()


@app.post("/unify_phone_from_json")
async def format_phone(request: Request) -> Response:
    number = await request.json()
    return Response(get_formatted_phone(number['phone']), media_type="text/html")


@app.post("/unify_phone_from_form")
async def format_phone_form(phone: str = Form()) -> Response:
    return Response(get_formatted_phone(phone), media_type="text/html")
