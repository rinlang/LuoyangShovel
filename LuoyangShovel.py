#!/usr/bin/python3
# -*- coding: utf-8 -*-


import fire
from conf import config
import common
import time


class LuoyangShovel(object):
    """


    """
    def __init__(self, target=""):
        self.target = target

    def run(self):
        """
        Luoyang Shovel running entrance

       :return:
        """
        print(common.LUOYANG_SHOVEL_BANNER)
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        for module in config['modules']:
            if module['enable']:
                imp_module = 'modules.'+module[]
                imp_class =

    @staticmethod
    def version():
        print(common.LUOYANG_SHOVEL_BANNER)
        exit(0)


if __name__ == "__main__":
    fire.Fire(LuoyangShovel)
