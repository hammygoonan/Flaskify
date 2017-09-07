from project.data.track import Track


mp3_file_path = 'DJ Mustard/Ketchup - HotNewHipHop/08. DJ Mustard - LadyKilla Feat. Cocc Pi' +\
                'stol Cree.mp3'
mp3_file_path_with_year = 'David Bowie/David Bowie - The Rise And Fall Of Ziggy Stardust An' +\
                          'd The Spiders From Mars/09 - Ziggy Stardust.mp3'


def test_mp3_get_title():
    mp3 = Track.get_details(mp3_file_path)
    assert 'LadyKilla Feat. Cocc Pistol Cree' == mp3.get_title()


def test_mp3_get_artists():
    mp3 = Track.get_details(mp3_file_path)
    assert 'DJ Mustard' == mp3.get_artists()


def test_mp3_get_album_artists():
    mp3 = Track.get_details(mp3_file_path)
    assert 'DJ Mustard' == mp3.get_album_artists()


def test_mp3_get_album_year():
    mp3 = Track.get_details(mp3_file_path_with_year)
    assert 1972 == mp3.get_album_year()


def test_get_track_album():
    mp3 = Track.get_details(mp3_file_path)
    assert 'Ketchup' == mp3.get_track_album()


def test_get_track_number():
    mp3 = Track.get_details(mp3_file_path)
    assert 8 == mp3.get_track_number()


def test_get_track_genre():
    mp3 = Track.get_details(mp3_file_path)
    assert ['Hip-Hop'] == mp3.get_track_genre()


def test_get_track_publisher():
    mp3 = Track.get_details(mp3_file_path)
    assert ['HotNewHipHop.com'] == mp3.get_track_publisher()
