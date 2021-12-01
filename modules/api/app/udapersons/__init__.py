from app.udapersons.models import Person  # noqa
from app.udapersons.schemas import PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from app.udapersons.controllers import api as udapersons_api

    api.add_namespace(udapersons_api, path=f"/{root}")
