import json

from googleapiclient.discovery import build

from src.utils import api_key


class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется по id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        # self.__channel_title = self._snippet['title']

    @property
    def channel_id(self) -> str:
        """Возвращает id канала"""
        return self.__channel_id

    @property
    def channel_title(self) -> str:
        """Возвращает название канала"""
        return self.__channel_title

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
    def _snippet(self) -> dict:
        return self.get_info

