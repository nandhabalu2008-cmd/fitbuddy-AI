import sys
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from app.database import Base, engine
    from app.routes import router
else:
    from .database import Base, engine
    from .routes import router

load_dotenv()
Base.metadata.create_all(bind=engine)

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="FitBuddy - AI Fitness Plan Generator")

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static",
)

app.state.templates = Jinja2Templates(directory=BASE_DIR / "templates")
app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)
