"""
PyVCAD - Python Vascular Computer-Aided Design Library
A library for creating 3D geometric objects and performing boolean operations
for vascular modeling and design.
"""

from .shapes import Box, Cylinder
from .operations import Union, Subtract
from .scene import Scene

__version__ = "0.1.0"
__all__ = ["Box", "Cylinder", "Union", "Subtract", "Scene"]