import feedparser
from flask import current_app as app
from flask.cli import with_appcontext
from . import db

from .models import Channel, Entry

def save_new_entries(channel: Channel):
    """"""

    feed = feedparser.parse(channel.url)
    for entry in feed.entries:
        id = f"{channel.id}|{entry.id.replace('?p=', '').split('/')[-1]}"
        if Entry.query.filter_by(id=id).first() is None:
            new_entry = Entry(
                id = id,
                title = entry.title,
                url = entry.link,
                description = entry.summary[:500],
                channel_id = channel.id
            )
            db.session.add(new_entry)
            db.session.commit()

@app.cli.command("fetch-rss")
@with_appcontext
def fetch_entries():
    """"""
    print("Starting fetching information...")
    channels = Channel.query.all()
    for channel in channels:
        print(f"Fetching from {channel.url}...")
        save_new_entries(channel)
    print("RSS saved into database!")
