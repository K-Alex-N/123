import typing

from app.store.crm.accessor import CrmAccessor

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_accessors(app: "Application"):
    app.crm_accessor = CrmAccessor()
    # print('  setup_accessors 1 app.srm_accessor', app.crm_accessor)
    app.on_startup.append(app.crm_accessor.connect)
    # print('  !!!!!!! type(app.srm_accessor) =', type(app.crm_accessor))
    # print('  !!!!!!! type(app.srm_accessor.app) =', type(app.crm_accessor.app))
    # print('  setup_accessors 2 = app.on_startup.append(app.srm_accessor.connect)')
    app.on_cleanup.append(app.crm_accessor.disconnect)
    # print('  setup_accessors 3 = app.on_cleanup.append(app.srm_accessor.disconnect)')

