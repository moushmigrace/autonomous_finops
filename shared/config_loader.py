from dotenv import load_dotenv
import os

load_dotenv()

PROMETHEUS_URL = os.getenv("PROMETHEUS_URL")