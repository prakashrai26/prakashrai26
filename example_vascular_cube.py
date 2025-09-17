#!/usr/bin/env python3
"""
Example script demonstrating the PyVCAD library usage.
This script creates a vascular structure within a cube as described in the problem statement.
"""

import pyvcad

def main():
    print("Creating vascular cube with PyVCAD...")
    
    # 1. Create the cube
    cube = pyvcad.Box((0, 0, 0), 10, 10, 10)
    print(f"Created cube: {cube}")
    
    # 2. Define vascular paths (example: a simple bifurcation)
    vessels = []
    main_vessel = pyvcad.Cylinder(start=(5, 5, 0), end=(5, 5, 7), radius=0.5)
    branch1 = pyvcad.Cylinder(start=(5, 5, 7), end=(2, 8, 10), radius=0.3)
    branch2 = pyvcad.Cylinder(start=(5, 5, 7), end=(8, 2, 10), radius=0.3)
    vessels.extend([main_vessel, branch1, branch2])
    
    print(f"Created main vessel: {main_vessel}")
    print(f"Created branch 1: {branch1}")
    print(f"Created branch 2: {branch2}")
    
    # 3. Combine all vessels into one object
    vascular_structure = pyvcad.Union(vessels)
    print(f"Created vascular structure: {vascular_structure}")
    
    # 4. Optionally, subtract vessels from cube for hollow channels
    hollow_cube = pyvcad.Subtract(cube, vascular_structure)
    print(f"Created hollow cube: {hollow_cube}")
    
    # 5. Save or visualize
    scene = pyvcad.Scene()
    scene.add(hollow_cube)
    
    print(f"Created scene: {scene}")
    print(f"Scene bounds: {scene.get_bounds()}")
    
    # Save the scene
    scene.save("vascular_cube.vcad")
    
    print("Example completed successfully!")


if __name__ == "__main__":
    main()