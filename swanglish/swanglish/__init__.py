from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings['persona.secrete'] = 'some secreate string'
    settings['persona.audiences'] = 'http://localhost:6543'

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config = Configurator(settings=settings)
    config.include('pyramid_persona')

    config.include('pyramid_jinja2')
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('swanglish', '/swanglish')
    config.add_route('translate', '/swanglish/translate')
    config.scan()
    return config.make_wsgi_app()
