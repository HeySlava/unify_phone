from fastapi import Request, FastAPI

from phone import phone


app = FastAPI()


@app.post("/unify_phone_from_json/")
async def format_phone(request: Request) -> str:
    number = await request.json()
    return phone(number['phone'])
