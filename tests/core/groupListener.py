# -*- coding: utf-8 -*-

from pknyx.core.groupListener import *
import unittest

# Mute logger
from pknyx.services.logger import logging
logger = logging.getLogger(__name__)
logging.getLogger("pknyx").setLevel(logging.ERROR)


class GroupListenerTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        pass

