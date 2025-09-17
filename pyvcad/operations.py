"""
Boolean operations for combining and modifying shapes.
"""

from typing import List, Union as TypingUnion
from .shapes import Shape


class Operation(Shape):
    """Base class for boolean operations."""
    
    def __init__(self, shapes: TypingUnion[Shape, List[Shape]]):
        super().__init__()
        if isinstance(shapes, Shape):
            self.shapes = [shapes]
        elif isinstance(shapes, list):
            self.shapes = shapes
        else:
            raise ValueError("shapes must be a Shape or list of Shapes")
        
        self.type = "operation"
    
    def get_bounds(self):
        """Get the combined bounding box of all shapes."""
        if not self.shapes:
            return ((0, 0, 0), (0, 0, 0))
        
        all_bounds = [shape.get_bounds() for shape in self.shapes]
        
        min_x = min(bounds[0][0] for bounds in all_bounds)
        min_y = min(bounds[0][1] for bounds in all_bounds)
        min_z = min(bounds[0][2] for bounds in all_bounds)
        
        max_x = max(bounds[1][0] for bounds in all_bounds)
        max_y = max(bounds[1][1] for bounds in all_bounds)
        max_z = max(bounds[1][2] for bounds in all_bounds)
        
        return ((min_x, min_y, min_z), (max_x, max_y, max_z))


class Union(Operation):
    """Combines multiple shapes into a single object."""
    
    def __init__(self, shapes: TypingUnion[Shape, List[Shape]]):
        """
        Create a union of shapes.
        
        Args:
            shapes: A single shape or list of shapes to union together
        """
        super().__init__(shapes)
        self.operation_type = "union"
    
    def __repr__(self):
        return f"Union({len(self.shapes)} shapes)"


class Subtract(Operation):
    """Subtracts one or more shapes from a base shape."""
    
    def __init__(self, base_shape: Shape, subtract_shapes: TypingUnion[Shape, List[Shape]]):
        """
        Create a subtraction operation.
        
        Args:
            base_shape: The shape to subtract from
            subtract_shapes: The shape(s) to subtract from the base
        """
        super().__init__([])  # Don't pass shapes to parent yet
        self.base_shape = base_shape
        
        if isinstance(subtract_shapes, Shape):
            self.subtract_shapes = [subtract_shapes]
        elif isinstance(subtract_shapes, list):
            self.subtract_shapes = subtract_shapes
        else:
            raise ValueError("subtract_shapes must be a Shape or list of Shapes")
        
        # Combine all shapes for bounds calculation
        self.shapes = [self.base_shape] + self.subtract_shapes
        self.operation_type = "subtract"
    
    def __repr__(self):
        return f"Subtract(base={self.base_shape}, subtract={len(self.subtract_shapes)} shapes)"
    
    def get_bounds(self):
        """Get the bounding box of the base shape (conservative estimate)."""
        return self.base_shape.get_bounds()


class Intersect(Operation):
    """Finds the intersection of multiple shapes."""
    
    def __init__(self, shapes: TypingUnion[Shape, List[Shape]]):
        """
        Create an intersection of shapes.
        
        Args:
            shapes: A single shape or list of shapes to intersect
        """
        super().__init__(shapes)
        self.operation_type = "intersect"
    
    def __repr__(self):
        return f"Intersect({len(self.shapes)} shapes)"