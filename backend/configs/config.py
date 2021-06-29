import os


MONGO_HOST = os.getenv("MONGO_HOST", "127.0.0.1")
MONGO_PORT = os.getenv("MONGO_PORT", 27017)
v1_url = "/api/v1"
DATABASE_NAME = os.getenv("DATABASE_NAME", "fastprojectkit")
COLLECTION_NAME_USER = os.getenv("COLLECTION_NAME_USER", "user")
SECRET_KEY = os.getenv("SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
ADMIN_ACCESS_LEVEL = os.getenv("ADMIN_ACCESS_LEVEL", 99)  # Which access level will define as admin
