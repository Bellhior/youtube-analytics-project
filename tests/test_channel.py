from src.channel import Channel
import os

"""Здесь представлены тесты с использованием pytest для модуля Channel"""


def test_channel_id(channel):
    """channel_id соответствует Channel"""
    assert channel.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'


def test_title(channel):
    """title соответствует Channel"""
    assert channel.title == 'MoscowPython'


def test_description(channel):
    """description соответствует Channel"""
    assert channel.description == 'Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\n'\
                                  'Присоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)'


def test_url(channel):
    """property соответствует Channel"""
    assert channel.url == 'https://www.youtube.com/channel/UC-OVMPlMA3-' \
                          'YCIeg4z5z23A'


def test_subscribers(channel):
    """subscribers является экземпляром типа int"""
    assert isinstance(channel.subscribers, int) is True


def test_video_count(channel):
    """video_count является экземпляром типа int"""
    assert isinstance(channel.video_count, int) is True


def test_views_count(channel):
    """views_count является экземпляром типа int"""
    assert isinstance(channel.views_count, int) is True


def test_to_json(channel):
    """Тест на работоспособность метода to_json"""
    channel.to_json('channel.json')
    assert os.path.exists('channel.json')

    os.remove('channel.json')
    assert not os.path.exists('channel.json')


def test_get_service():
    """Проверка метода get_service для класса Channel"""
    service = Channel.get_service()
    assert service is not None
