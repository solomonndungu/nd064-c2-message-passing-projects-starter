def register_routes(api, app, root="connection_api"):
    from controllers import api as udaconnect_connection_api

    api.add_namespace(udaconnect_connection_api, path=f"/{root}")
