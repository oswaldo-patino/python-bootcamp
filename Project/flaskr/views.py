from flask import current_app as app, make_response, render_template, redirect
from . import db
from .models import Entry

@app.route("/")
def home():
    entries = Entry.query.all()

    return render_template("home.html", feed=entries)

@app.route("/tracking/<id>")
def tracking(id: str):
    entry = Entry.query.get(id)
    entry.views += 1
    db.session.commit()
    return redirect(entry.url)

@app.errorhandler(404)
def not_found():
    return make_response(
        render_template("404.html"),
        404
     )

@app.errorhandler(400)
def bad_request():
    return make_response(
        render_template("400.html"),
        400
    )

@app.errorhandler(500)
def server_error(e):
    print(e)
    return make_response(
        render_template("500.html"),
        500
    )