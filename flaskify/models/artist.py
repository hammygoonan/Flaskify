"""Artist Model."""


class Artist():
    """Artist Model."""

    def __init__(self, name):
        """Initialise Model."""
        self.id = id(self)
        self.name = name

    def serialise(self):
        return self.__dict__
