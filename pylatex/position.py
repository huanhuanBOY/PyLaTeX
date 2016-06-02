# -*- coding: utf-8 -*-

from .base_classes import Environment
from .package import Package
from .utils import NoEscape, line_break


class Position(Environment):
    r""" Base class for positioning environments
    """
    packages = [Package('ragged2e')]


class Center(Position):
    r""" Centered environment """


class Flushleft(Position):
    r""" Left-aligned environment """


class Flushright(Position):
    r""" Right-aligned environment """


class Minipage(Environment):
    r""" A class that allows the creation of minipages within document pages """
    
    def __init__(self, width=1):
        r""" Instantiates a minipage within the current environment
	
            Args
            ----
            width: float
                width with respect to the text width of the page
        """

        arguments = [ NoEscape(str(width) + r'\textwidth') ]

        super().__init__(arguments = arguments)
