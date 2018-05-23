"""Mixin to integrate Elasticsearch with models.

Adapted from `Miguel Grinberg's Flask Mega Tutorial <https://blog.miguelgrinberg.com/post/
the-flask-mega-tutorial-part-xvi-full-text-search>`_

:copyright: (c) 2018 Hammy Goonan
"""

from flaskify.search import add_to_index, remove_from_index, query_index


class SearchableMixin():
    """Mixin to add Elasticsearch indexing to models."""

    @classmethod
    def search(cls, expression, page, per_page):
        """Search method."""
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)), total

    @classmethod
    def before_commit(cls, session):
        """Update index before model is committed."""
        session._changes = {
            'add': [obj for obj in session.new if isinstance(obj, cls)],
            'update': [obj for obj in session.dirty if isinstance(obj, cls)],
            'delete': [obj for obj in session.deleted if isinstance(obj, cls)]
        }

    @classmethod
    def after_commit(cls, session):
        """Update index after model is committed."""
        for obj in session._changes['add']:
            add_to_index(cls.__tablename__, obj)
        for obj in session._changes['update']:
            add_to_index(cls.__tablename__, obj)
        for obj in session._changes['delete']:
            remove_from_index(cls.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        """Reindex model."""
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)
