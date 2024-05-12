import requests
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import re
import json
from starlette.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")
templates = Jinja2Templates(directory="frontend")


# Function to save data to JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


# Function to load data from JSON file
def load_from_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/fetch_everything", response_class=HTMLResponse)
async def generate_gallery(request: Request, url):
    index = 1
    page_index = 1
    main_url = url
    name = main_url.split("/")[5].replace("%20", " ")
    print(f"Fetching images of {name}")
    image_urls = []
    while True:
        page_url = f'{main_url}/p{page_index}'
        response = requests.get(page_url)

        if response.status_code == 200:
            input_string = response.text
        else:
            break

        # Regular expression pattern to match the image URLs
        pattern = r"showimage\(\'([^']+)'"

        # Find all matches of the pattern in the input string
        matches = re.findall(pattern, input_string)

        # Base URL for the images
        base_url = "https://www.cfake.com/medias/photos/"

        # Create the array of image URLs
        celeb_name = main_url.split("/")[5].replace("_", " ")
        if celeb_name not in matches[0]:
            break
        for match in matches:
            if celeb_name in match:
                match = match.replace('big.php?show=', '').split('&')[0]
                image_urls.append(base_url + match)

        # Increment page index
        page_index += 1

    # Saving image_urls to storage.json
    celeb_data = {name: image_urls}
    save_to_json(celeb_data, "storage.json")

    return templates.TemplateResponse("index.html", {"request": request, "image_urls": image_urls})


@app.get("/gallery", response_class=HTMLResponse)
async def generate_gallery(request: Request):
    celeb_data = load_from_json("storage.json")
    urls = []
    for celeb_name, image_urls in celeb_data.items():
        urls.extend(image_urls)

    return templates.TemplateResponse("index.html", {"request": request, "image_urls": urls})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
