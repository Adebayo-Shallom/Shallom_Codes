from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/api")
def home(slack_name:str = "Pamode", track:str = "backend"):
    now = datetime.now(pytz.UTC)
    utc_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    current_day = now.strftime("%A")
    return {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Adebayo-Shallom/Shallom_Codes/blob/7144bc14b2f5e18995f78f823178855c80d7c798/app.py",
        "github_repo_url": "https://github.com/Adebayo-Shallom/shallomcodes.github.io",
        "status_code": 200
    }
