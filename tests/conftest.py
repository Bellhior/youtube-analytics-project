import pytest

from src.channel import Channel

"""Использование фикстуры"""


@pytest.fixture
def channel():
    """Возвращает заданный id"""
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')
