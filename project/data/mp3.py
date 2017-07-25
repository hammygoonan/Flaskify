from .track import Track


class Mp3(Track):
    """Extract"""
    def get_title(self):
        # TIT2
        pass

    def get_artists(self):
        # TPE1
        pass

    def get_album_artists(self):
        # TPE2
        pass

    # def get_album_title(self):
    #     pass

    def get_album_year(self):
        # TDRC
        pass

    # def get_url_for(self):
    #     pass

    def get_album_pic(self):
        # APIC
        pass

    def get_track_album(self):
        # TALB
        pass

    # def get_album_name(self):
    #     pass

    def get_track_style(self):
        # TCON
        pass

    def get_track_copyright(self):
        # TCOP
        pass

    # def get_track_release_date(self):
    #     pass

    # def get_track_encoder(self):
    #     pass

    def get_track_publisher(self):
        # TPUB
        pass

    def get_track_number(self):
        # TRCK
        pass
