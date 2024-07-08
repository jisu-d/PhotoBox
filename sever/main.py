from fastapi import FastAPI

from collage_img import creative_collage_images
from print_img import printImgs

app = FastAPI()

from pydantic import BaseModel

from starlette.middleware.cors import CORSMiddleware

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

class MADE_DATE(BaseModel):
    title: str
    select_imgs: list[str]

class PRINTOUT_INFO(BaseModel):
    printoutNum: int
    path: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/createCollage")
def read_root(data: MADE_DATE):
    collageData = creative_collage_images(data)
    return {
        "img_name": collageData[0],
        'collage_img': collageData[1]
    }


@app.post("/printImgs")
def read_root(data: PRINTOUT_INFO):
    printImgs(data.printoutNum, data.path)
    return {
        'msg': 'success'
    }