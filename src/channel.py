import json

from googleapiclient.discovery import build

from src.utils import api_key


class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется по id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__title: str = self._items['snippet']['title']
        self.__description: str = self._items['snippet']['description']
        self.__url: str = f"https://www.youtube.com/channel/{self.__channel_id}"
        self._subscribers: int = self._items["statistics"]["subscriberCount"]
        self._videos: int = self._items["statistics"]["videoCount"]
        self._views: int = self._items["statistics"]["viewCount"]

    @property
    def channel_id(self) -> str:
        """Возвращает id канала"""
        return self.__channel_id

    @property
    def title(self) -> str:
        """Возвращает название канала"""
        return self.__title

    @property
    def description(self) -> str:
        """Возвращает описание канала"""
        return self.__description

    @property
    def url(self) -> str:
        """Возвращает url канала"""
        return self.__url

    @property
    def subscribers(self) -> int:
        """Возвращает число подпищиков"""
        return self._subscribers

    @property
    def video_count(self) -> int:
        """Возвращает число видео"""
        return self._videos

    @property
    def views_count(self) -> int:
        """Возвращает число просмотров"""
        return self._views

    def print_info(self) -> None:
        """Выводит информацию в консоль"""
        return self._print_info(self.get_info)

    @property
    def get_info(self) -> dict:
        """Выводит информацию о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        return channel

    @staticmethod
    def _print_info(channel) -> None:
        """Выводит информацию в формате JSON"""
        dict_channel = json.dumps(channel, indent=2, ensure_ascii=False)
        print(dict_channel)

    @property
    def _items(self) -> dict:
        """Прописывает путь в items"""
        return self.get_info["items"][0]

    @classmethod
    def get_service(cls) -> object:
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, filename: str) -> None:
        """Сохраняет в файл значения атрибутов экземпляра `Channel"""
        attr = {
            "id": self.__channel_id,
            "title": self.__title,
            "description": self.__description,
            "url": self.__url,
            "subscribers": self._subscribers,
            "videos": self._videos,
            "views": self._views
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(attr, f, indent=2, ensure_ascii=False)
