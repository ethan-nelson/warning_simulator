from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError


@view_config(route_name='simulation_splash', renderer='../templates/simulation_splash.jinja2')
def simulation_splash(request):
    return {'simulation': request.matchdict['id']}


@view_config(route_name='simulation_warn', renderer='../templates/simulation_warn.jinja2')
def simulation_warn(request):
    return {'simulation': request.matchdict['id']}
