# -*- coding: utf-8 -*-


from configs.config_common import ConfigCommon


class ConfigDevelopment(object):

    ## sqlalchemy url
    sqlalchemy_url = 'postgresql+psycopg2://yourtype@localhost/yourtype'
    configs = {"encoding": "utf-8", "echo": True}


