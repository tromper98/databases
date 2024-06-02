import os.path
from copy import copy
from PIL import Image

ALLOWED_EXTENSIONS = ['jpg', 'webp']
MIN_IMAGE_SIZE = (200, 200)
MAX_IMAGE_SIZE = (800, 800)


class FileHandler:

    def __init__(self, store_path: str):
        self._store_path = store_path

    def try_save_file(self, file) -> bool:
        img = Image.open(file)
        filename = file.filename
        # Browser can send empty file with filename = empty string if file not set
        if filename == '':
            return False

        if not self.is_allowed_extension(file.filename):
            raise ValueError(f"Unsupported image extension {filename.rsplit('.', 1)[1].lower()}")

        if not self.is_image_size_acceptable(img):
            min_file_size = f'{MIN_IMAGE_SIZE[0]}x{MIN_IMAGE_SIZE[1]}'
            max_file_size = f'{MAX_IMAGE_SIZE[0]}x{MAX_IMAGE_SIZE[1]}'
            raise ValueError(f"Unsupported image size. Image size must between {min_file_size} and {max_file_size}")

        if self.is_file_exists(filename):
            raise ValueError(f"File with same nae '{filename}' already exists")

        img.save(os.path.join(self._store_path, filename))
        return True

    @staticmethod
    def is_allowed_extension(filename: str) -> bool:
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @staticmethod
    def is_image_size_acceptable(img: Image) -> bool:
        weight, height = img.size
        if (MIN_IMAGE_SIZE[0] <= weight <= MAX_IMAGE_SIZE[0]) and (MIN_IMAGE_SIZE[1] <= height <= MAX_IMAGE_SIZE[1]):
            return True
        return False

    def is_file_exists(self, filename: str) -> bool:
        return os.path.exists(os.path.join(self._store_path, filename))
