# encoding: utf-8
"""

"""
__author__ = 'Richard Smith'
__date__ = '02 Jun 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'


from abc import ABC, abstractmethod
from asset_extractor.core import AssetExtractor


class BaseInputPlugin(ABC):

    @abstractmethod
    def run(self, extractor: AssetExtractor):
        pass