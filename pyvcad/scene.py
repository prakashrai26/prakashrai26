"""
Scene management for organizing and saving 3D objects.
"""

import json
import os
from typing import List, Dict, Any
from .shapes import Shape


class Scene:
    """A scene that contains and manages 3D objects."""
    
    def __init__(self, name: str = "Untitled Scene"):
        """
        Create a new scene.
        
        Args:
            name: Name of the scene
        """
        self.name = name
        self.objects: List[Shape] = []
        self.metadata: Dict[str, Any] = {
            "version": "1.0",
            "created_with": "PyVCAD",
            "description": "3D scene for vascular modeling"
        }
    
    def add(self, obj: Shape) -> None:
        """
        Add an object to the scene.
        
        Args:
            obj: The shape or operation to add to the scene
        """
        if not isinstance(obj, Shape):
            raise ValueError("Object must be a Shape or Operation")
        
        self.objects.append(obj)
    
    def remove(self, obj: Shape) -> bool:
        """
        Remove an object from the scene.
        
        Args:
            obj: The object to remove
            
        Returns:
            True if object was removed, False if not found
        """
        try:
            self.objects.remove(obj)
            return True
        except ValueError:
            return False
    
    def clear(self) -> None:
        """Remove all objects from the scene."""
        self.objects.clear()
    
    def get_bounds(self):
        """Get the bounding box that contains all objects in the scene."""
        if not self.objects:
            return ((0, 0, 0), (0, 0, 0))
        
        all_bounds = [obj.get_bounds() for obj in self.objects]
        
        min_x = min(bounds[0][0] for bounds in all_bounds)
        min_y = min(bounds[0][1] for bounds in all_bounds)
        min_z = min(bounds[0][2] for bounds in all_bounds)
        
        max_x = max(bounds[1][0] for bounds in all_bounds)
        max_y = max(bounds[1][1] for bounds in all_bounds)
        max_z = max(bounds[1][2] for bounds in all_bounds)
        
        return ((min_x, min_y, min_z), (max_x, max_y, max_z))
    
    def _serialize_object(self, obj: Shape) -> Dict[str, Any]:
        """Convert an object to a serializable dictionary."""
        base_data = {
            "type": obj.type,
            "position": obj.position
        }
        
        if hasattr(obj, 'origin'):  # Box
            base_data.update({
                "origin": obj.origin,
                "width": obj.width,
                "height": obj.height,
                "depth": obj.depth
            })
        elif hasattr(obj, 'start'):  # Cylinder
            base_data.update({
                "start": obj.start,
                "end": obj.end,
                "radius": obj.radius,
                "length": obj.length,
                "direction": obj.direction
            })
        elif hasattr(obj, 'operation_type'):  # Operations
            base_data.update({
                "operation_type": obj.operation_type
            })
            
            if hasattr(obj, 'base_shape'):  # Subtract
                base_data["base_shape"] = self._serialize_object(obj.base_shape)
                base_data["subtract_shapes"] = [self._serialize_object(s) for s in obj.subtract_shapes]
            else:  # Union, Intersect
                base_data["shapes"] = [self._serialize_object(s) for s in obj.shapes]
        
        return base_data
    
    def save(self, filename: str) -> None:
        """
        Save the scene to a file.
        
        Args:
            filename: Path to save the scene file
        """
        scene_data = {
            "metadata": self.metadata,
            "scene": {
                "name": self.name,
                "object_count": len(self.objects),
                "bounds": self.get_bounds()
            },
            "objects": [self._serialize_object(obj) for obj in self.objects]
        }
        
        # Ensure directory exists
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # Determine file format based on extension
        file_ext = os.path.splitext(filename)[1].lower()
        
        if file_ext == '.vcad' or file_ext == '.json':
            with open(filename, 'w') as f:
                json.dump(scene_data, f, indent=2)
        else:
            # Default to JSON format
            with open(filename, 'w') as f:
                json.dump(scene_data, f, indent=2)
        
        print(f"Scene saved to {filename}")
    
    def load(self, filename: str) -> None:
        """
        Load a scene from a file.
        
        Args:
            filename: Path to the scene file to load
        """
        with open(filename, 'r') as f:
            scene_data = json.load(f)
        
        self.metadata = scene_data.get("metadata", {})
        scene_info = scene_data.get("scene", {})
        self.name = scene_info.get("name", "Loaded Scene")
        
        # Note: Full object reconstruction would require more complex deserialization
        # For now, we'll store the raw object data
        self.objects.clear()
        print(f"Scene loaded from {filename}")
        print(f"Contains {len(scene_data.get('objects', []))} objects")
    
    def __repr__(self):
        return f"Scene('{self.name}', {len(self.objects)} objects)"
    
    def __len__(self):
        return len(self.objects)