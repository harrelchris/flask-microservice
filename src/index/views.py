from flask import render_template
from flask.views import View


class IndexView(View):
    init_every_request = False
    methods = ["GET"]

    def dispatch_request(self):
        return render_template("index.html")
