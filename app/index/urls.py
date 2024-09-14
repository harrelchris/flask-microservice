from flask import Blueprint

from . import views

bp = Blueprint(
    name="index",
    import_name=__name__,
    template_folder="templates",
    url_prefix="/",
)

bp.add_url_rule(
    rule="/",
    view_func=views.IndexView.as_view("index"),
)
