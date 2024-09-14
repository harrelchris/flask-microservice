from flask import Blueprint

from . import views

bp = Blueprint(
    name="index",
    import_name=__name__,
    static_folder=None,
    static_url_path=None,
    template_folder="templates",
    url_prefix=None,
    subdomain=None,
    url_defaults=None,
    root_path=None,
    cli_group=None,
)

bp.add_url_rule(
    rule="/",
    view_func=views.IndexView.as_view("index"),
)
