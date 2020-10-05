from modules import Module
from os.path import dirname
from modules import brute_force


class BruteForce(Module):
    """
    LuoyangShovel Brute Module

    This module uses dictionary files to brute_force force the subdomain.

    :param

    """

    def __init__(self):
        self.dict_path = [(dirname(__file__) + '/' + dic) for dic in brute_force.MODEL_CONFIG['dicts']]
        self.threadsNum = brute_force.MODEL_CONFIG['threads_num']

    def run(self):
        pass
