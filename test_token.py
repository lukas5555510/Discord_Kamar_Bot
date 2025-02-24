import os
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("KAMAR_BOT_TOKEN")
print(secret_key)