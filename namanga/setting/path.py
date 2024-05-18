from os.path import join, dirname


class Config:
    TEMPLATES_PTH = join(join(dirname(__file__), 'fe_namanga'), 'templates')
    DIR_IMAGE_MANGA_PTH = join(TEMPLATES_PTH, 'image_manga')
    DIR_IMAGE_AVATAR_PTH = join(TEMPLATES_PTH, 'image_avatar')


cfg = Config()
