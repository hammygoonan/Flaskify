import os
import pytest
from flask import current_app
from project.data.track import Track
from project.data.mp3 import Mp3
from project.data.mp4 import Mp4
from project.data.m4a import M4a
from project.data.flac import Flac
from project.data.ogg import Ogg


def test_factory_returns_mp3_class():
    mp3_file_path = 'DJ Mustard/Ketchup - HotNewHipHop/08. DJ Mustard - LadyKilla Feat. Coc' +\
                    'c Pistol Cree.mp3'
    mp3 = Track.get_details(mp3_file_path)
    assert isinstance(mp3, Mp3)


def test_factory_returns_flac_class():
    flac_file = 'Animal Collective/Merriweather Post Pavilion/01 - In the Flowers.flac'
    flac = Track.get_details(flac_file)
    assert isinstance(flac, Flac)


def test_factory_returns_m4a_class():
    m4a = Track.get_details('Amon Tobin/Dark Jovian/01 Dark Jovian.m4a')
    assert isinstance(m4a, M4a)


def test_factory_returns_mp4_class():
    mp4 = Track.get_details('Amon Tobin/Dark Jovian/01 Dark Jovian.m4a')
    assert isinstance(mp4, Mp4)


def test_factory_returns_ogg_class():
    ogg = Track.get_details('Fugazi/13 songs/fugazi - 01 - waiting room.ogg')
    assert isinstance(ogg, Ogg)


def test_get_path_for_absolute_path(app):
    """Test correct file is returned if path provided is absolute."""
    mp4 = Track.get_details(
        os.path.join(current_app.config['MUSIC_DIR'], 'Amon Tobin/Dark Jovian/01 Dark Jovian.m4a')
    )
    assert isinstance(mp4, Mp4)


def test_error_if_filetype_not_supported():
    with pytest.raises(Exception):
        Track.get_details('test.abc')
