# -*- coding: utf-8 -*-
import logging
from pprint import pprint

from pyramid.settings import asbool
from pyramid.settings import aslist

from pycallgraph import Config
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

BOOL_VALUES = ('1', 'y', 'yes', 't', 'true',
               '0', 'n', 'no', 'f', 'false', 'none')

log = logging.getLogger(__name__)


def pycallgraph_config_from_settings(settings, prefix='pycallgraph.'):
    config = Config()

    filter_exclude = settings.pop('pycallgraph.trace_filter.exclude', None)
    if filter_exclude is not None:
        config.trace_filter.exclude = aslist(filter_exclude )

    filter_include = settings.pop('pycallgraph.trace_filter.include', None)
    if filter_include is not None:
        config.trace_filter.include = aslist(filter_include )

    for k, v in settings.items():
        if k.startswith(prefix):
            if v in BOOL_VALUES:
                v = asbool(v)
            setattr(config, k[len(prefix):], v)

    if config.debug:
        conf = config.__dict__
        conf.pop('parser')
        conf['trace_filter'] = config.trace_filter.__dict__
        conf['trace_grouper'] = config.trace_grouper.__dict__
        pprint(conf)

    return config


class Tween(object):
    def __init__(self, handler, settings):
        self.handler = handler
        self.config = pycallgraph_config_from_settings(settings)

    def __call__(self, request):
        graphviz = GraphvizOutput()
        graphviz.output_file = 'callgraph{}.png'.format(
            request.path.replace('/', '.'))
        with PyCallGraph(output=graphviz, config=self.config):
            return self.handler(request)


def tween_factory(handler, registry):
    return Tween(handler, registry.settings.copy())


def includeme(config):
    config.add_tween('pyramid_pycallgraph.tween_factory')


