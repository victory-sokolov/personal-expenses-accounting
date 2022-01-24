import json
from fastapi import File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi import APIRouter

from utils import string_to_image, to_RGB
from recognition.recognizer import RecognizerProcessor
from config import settings
from utils import allowed_files


router = APIRouter()

async def file_upload(file: UploadFile = File(...)):
    """Save image"""
    file = file.filename
    target = settings.UPLOAD_FOLDER
    if file and allowed_files(file):
        destination = "/".join([target, file])
        file.save(destination)


@router.post('/recognize')
async def post(image: str = Form(...)):
    if image:
        img = string_to_image(image)
        cv_img = to_RGB(img)
        recognizer = RecognizerProcessor('lav')
        data = recognizer.recognize_factory(image=cv_img)
        return JSONResponse(content=data), 200

    return JSONResponse({'status': 'Cannot handle request!'}), 400




