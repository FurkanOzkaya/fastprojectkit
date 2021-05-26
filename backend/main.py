import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from views.user.v1.api import router as user_api_v1
from configs.config import v1_url


app = FastAPI(
    title="Develop FastApi (Easy Implement each Project)",
    description="You can easly implement these project and start your project",
    version="0.0.1"
)

# Changing 422 Unprocessable Entity to  to 400 Bad Request
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    content = jsonable_encoder({"detail": exc.errors()})
    return JSONResponse(content=content, status_code=400)


app.include_router(user_api_v1, prefix=v1_url, tags=["Users"])


if __name__ == "__main":
    uvicorn.run(app, host="0.0.0.0", port=9000)
