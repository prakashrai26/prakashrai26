"""
Basic geometric shapes for 3D modeling.
"""

import math
from typing import Tuple, List


class Shape:
    """Base class for all geometric shapes."""
    
    def __init__(self):
        self.position = (0, 0, 0)
        self.type = "shape"
    
    def __repr__(self):
        return f"{self.__class__.__name__}()"


class Box(Shape):
    """A rectangular box/cube shape."""
    
    def __init__(self, origin: Tuple[float, float, float], width: float, height: float, depth: float):
        """
        Create a box shape.
        
        Args:
            origin: (x, y, z) coordinates of the box origin
            width: Width of the box (x-direction)
            height: Height of the box (y-direction) 
            depth: Depth of the box (z-direction)
        """
        super().__init__()
        self.origin = origin
        self.width = width
        self.height = height
        self.depth = depth
        self.type = "box"
        self.position = origin
    
    def __repr__(self):
        return f"Box(origin={self.origin}, width={self.width}, height={self.height}, depth={self.depth})"
    
    def get_bounds(self) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
        """Get the bounding box of this shape."""
        x, y, z = self.origin
        return (
            (x, y, z),
            (x + self.width, y + self.height, z + self.depth)
        )


class Cylinder(Shape):
    """A cylindrical shape."""
    
    def __init__(self, start: Tuple[float, float, float], end: Tuple[float, float, float], radius: float):
        """
        Create a cylinder shape.
        
        Args:
            start: (x, y, z) coordinates of the cylinder start point
            end: (x, y, z) coordinates of the cylinder end point
            radius: Radius of the cylinder
        """
        super().__init__()
        self.start = start
        self.end = end
        self.radius = radius
        self.type = "cylinder"
        self.position = start
        
        # Calculate cylinder properties
        dx = end[0] - start[0]
        dy = end[1] - start[1] 
        dz = end[2] - start[2]
        self.length = math.sqrt(dx*dx + dy*dy + dz*dz)
        
        if self.length > 0:
            self.direction = (dx/self.length, dy/self.length, dz/self.length)
        else:
            self.direction = (0, 0, 1)
    
    def __repr__(self):
        return f"Cylinder(start={self.start}, end={self.end}, radius={self.radius})"
    
    def get_bounds(self) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
        """Get the bounding box of this shape."""
        x1, y1, z1 = self.start
        x2, y2, z2 = self.end
        r = self.radius
        
        return (
            (min(x1, x2) - r, min(y1, y2) - r, min(z1, z2) - r),
            (max(x1, x2) + r, max(y1, y2) + r, max(z1, z2) + r)
        )