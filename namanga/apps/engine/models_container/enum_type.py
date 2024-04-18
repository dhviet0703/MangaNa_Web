from enum import Enum


class EnumType(str, Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))

    def __str__(self):
        return self.value


class SystemRoleEnum(EnumType):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = 'ADMIN'
    POSTER = 'POSTER'
    USER = 'USER'


class RoleMangaEnum(EnumType):
    POSTER = 'POSTER'
    USER = 'USER'


class ManGaGenreEnum(EnumType):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    ANIME = 'Anime'
    CHUYENSINH = 'Chuyển sinh'
    CODAI = 'Cổ đại'
    COMEDY = 'Comedy'
    DEMON = 'Demons'
    DETECTIVE = 'Detective'
    DUOJINSHI = 'Doujinshi'
    DRAMA = 'Drama'
    FANTASY = 'Fantasy'
    GENDER = 'Gender'
    BENDER = 'Bender'
    HAREM = 'Harem'
    HISTORICAL = 'Historical'
    HORRON = 'Horror'
    ISEKAI = 'Isekai'
    JOSEI = 'Josei'
    MAFIA = 'Mafia'
    MAGIC = 'Magic'
    ONE_SHOT = 'One shot'
    PSYCHOLOGICAL = 'Psychological'
    ROMANCE = 'Romance'
    SCHOOL_LIFE = 'School LifeSci-fi'
    SHOUNEN = 'Shounen'
    TRUYENMAU = 'Truyện màu'
