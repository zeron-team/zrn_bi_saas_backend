import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mi_secreto_super_secreto')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/bi_saas')
