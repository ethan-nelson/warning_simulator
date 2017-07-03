def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('simulation_splash', '/simulation/{id:\d+}/splash')
    config.add_route('simulation_warn', '/simulation/{id:\d+}/warn')
