import zipfile
import os
from os.path import join
from django.core.files.base import ContentFile
from namanga.apps.engine.models import Image


def save_data_image_zip(chapter_id, path_image, data_zip):
    with zipfile.ZipFile(data_zip, 'r') as zip_ref:
        zip_contents = zip_ref.namelist()
        png_files = [f for f in zip_contents if f.endswith('.png') and not f.endswith('/')]
        for filename in png_files:
            full_path = os.path.join(path_image, filename)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with zip_ref.open(filename) as file:
                with open(full_path, 'wb') as f:
                    f.write(file.read())
            i = Image(chapter_id=chapter_id, src=full_path)
            i.save()
