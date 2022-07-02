from fastapi import Request
from fastapi import FastAPI
from fastapi import Response

from phone import phone


app = FastAPI()


@app.post("/unify_phone_from_json")
async def format_phone(request: Request) -> Response:
    number = await request.json()
    return Response(phone(number['phone']), media_type="text/html")
