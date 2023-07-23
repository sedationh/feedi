import datetime

import sqlalchemy as sa

from feedi.database import db

# TODO consider adding explicit support for url columns


class Feed(db.Model):
    """
    TODO
    """
    __tablename__ = 'feeds'
    id = sa.Column(sa.Integer, primary_key=True)

    name = sa.Column(sa.String, unique=True)
    url = sa.Column(sa.String)
    icon_url = sa.Column(sa.String)

    # FIXME select from known enums
    parser_type = sa.Column(sa.String, nullable=False)

    created = sa.Column(sa.TIMESTAMP, nullable=False, default=datetime.datetime.utcnow)
    updated = sa.Column(sa.TIMESTAMP, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    last_fetch = sa.Column(sa.TIMESTAMP)

    entries = sa.orm.relationship("Entry", back_populates="feed")

    def __repr__(self):
        return f'<Feed {self.name}>'


class Entry(db.Model):
    """
    TODO
    """
    __tablename__ = 'entries'
    __table_args__ = (sa.UniqueConstraint("feed_id", "remote_id"),)

    id = sa.Column(sa.Integer, primary_key=True)

    feed_id = sa.orm.mapped_column(sa.ForeignKey("feeds.id"))
    feed = sa.orm.relationship("Feed", back_populates="entries")
    remote_id = sa.Column(sa.String, nullable=False)

    title = sa.Column(sa.String, nullable=False)
    title_url = sa.Column(sa.String, nullable=False)
    username = sa.Column(sa.String)
    user_url = sa.Column(sa.String)
    avatar_url = sa.Column(sa.String)

    body = sa.Column(sa.String, doc="The content to be displayed in the feed. HTML is supported. For article entries, it would be an excerpt of the full article conent.")
    entry_url = sa.Column(sa.String, doc="The URL of this entry in the source. For link aggregators this would be the comments page.")
    content_url = sa.Column(sa.String, doc="The URL where the full content can be fetched or read. For link aggregators this would be the article redirect url.")
    media_url = sa.Column(sa.String, doc="URL of a media attachement or preview.")

    created = sa.Column(sa.TIMESTAMP, nullable=False, default=datetime.datetime.utcnow)
    updated = sa.Column(sa.TIMESTAMP, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    remote_created = sa.Column(sa.TIMESTAMP, nullable=False)
    remote_updated = sa.Column(sa.TIMESTAMP)

    def __repr__(self):
        return f'<Entry {self.feed_id}/{self.remote_id}>'