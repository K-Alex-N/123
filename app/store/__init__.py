import typing

from app.store.crm.accessor import CrmAccessor

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_accessor(app: "Application"):
    app.srm_accessor = CrmAccessor()
    app.on_startup.append(app.srm_accessor.connect)
    app.on_cleanup.append(app.srm_accessor.disconnect)