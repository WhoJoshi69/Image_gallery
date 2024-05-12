from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from typing import List
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")
templates = Jinja2Templates(directory="frontend")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/gallery", response_class=HTMLResponse)
async def generate_gallery(request: Request):
    urls = [
        "https://images3.alphacoders.com/859/thumb-1920-859804.png",
        "https://letsenhance.io/static/66c1b6abf8f7cf44c19185254d7adb0c/28ebd/AiArtBefore.jpg",
        "https://images8.alphacoders.com/840/thumb-1920-840020.png",
        "https://us.123rf.com/450wm/virtosmedia/virtosmedia2302/virtosmedia230216771/198356916-portrait-of-a-sphinx-cat-in-a-royal-suit.jpg?ver=6",
        "https://img.freepik.com/photos-premium/portrait-du-chat-sphynx-deguise-pharaon-pour-costume-fete-animaux-compagnie-ancienne-egypte_655090-829014.jpg",
        "https://img.freepik.com/photos-premium/portrait-chat-sphynx-portant-toge-romaine-pour-reconstitution-historique-pet-costume-festif-photo_655090-829009.jpg",
        "https://deepai.org/static/images/cyberpunkdolphin.png",
        "https://i.pinimg.com/originals/35/d1/fb/35d1fb5c199f4784bb4a8ed25eb49252.gif",
        "https://i.pinimg.com/550x/00/a9/10/00a910f0a5229554db7530007467d7ad.jpg",
        "https://img.freepik.com/photos-premium/portrait-chat-sphynx-portant-toge-romaine-pour-reconstitution-historique-pet-costume-festif-photo_655090-829009.jpg"
    ]

    return templates.TemplateResponse("index.html", {"request": request, "image_urls": urls})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
