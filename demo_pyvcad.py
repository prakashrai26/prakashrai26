#!/usr/bin/env python3
"""
Demonstration of PyVCAD library capabilities.
"""

import pyvcad
import json

def main():
    print("🚀 PyVCAD Library Demonstration")
    print("=" * 50)
    
    # 1. Basic shapes
    print("\n1. Creating basic shapes:")
    cube = pyvcad.Box((0, 0, 0), 10, 10, 10)
    cylinder = pyvcad.Cylinder((5, 5, 0), (5, 5, 10), 2.0)
    
    print(f"   Cube: {cube}")
    print(f"   Cylinder: {cylinder}")
    print(f"   Cube bounds: {cube.get_bounds()}")
    print(f"   Cylinder bounds: {cylinder.get_bounds()}")
    
    # 2. Boolean operations
    print("\n2. Boolean operations:")
    union = pyvcad.Union([cube, cylinder])
    subtract = pyvcad.Subtract(cube, cylinder)
    
    print(f"   Union: {union}")
    print(f"   Subtract: {subtract}")
    
    # 3. Complex vascular model (problem statement)
    print("\n3. Creating vascular model (from problem statement):")
    
    # Create the cube
    vascular_cube = pyvcad.Box((0, 0, 0), 10, 10, 10)
    
    # Define vascular paths (simple bifurcation)
    vessels = []
    main_vessel = pyvcad.Cylinder(start=(5, 5, 0), end=(5, 5, 7), radius=0.5)
    branch1 = pyvcad.Cylinder(start=(5, 5, 7), end=(2, 8, 10), radius=0.3)
    branch2 = pyvcad.Cylinder(start=(5, 5, 7), end=(8, 2, 10), radius=0.3)
    vessels.extend([main_vessel, branch1, branch2])
    
    print(f"   Main vessel: {main_vessel}")
    print(f"   Branch 1: {branch1}")
    print(f"   Branch 2: {branch2}")
    
    # Combine all vessels
    vascular_structure = pyvcad.Union(vessels)
    print(f"   Vascular structure: {vascular_structure}")
    
    # Create hollow channels
    hollow_cube = pyvcad.Subtract(vascular_cube, vascular_structure)
    print(f"   Hollow cube: {hollow_cube}")
    
    # 4. Scene management
    print("\n4. Scene management:")
    scene = pyvcad.Scene("Vascular Demo Scene")
    scene.add(hollow_cube)
    
    print(f"   Scene: {scene}")
    print(f"   Scene bounds: {scene.get_bounds()}")
    
    # 5. File operations
    print("\n5. Saving scene:")
    filename = "/tmp/demo_vascular_model.vcad"
    scene.save(filename)
    
    # Display file content (first few lines)
    with open(filename, 'r') as f:
        content = json.load(f)
    
    print(f"   File saved: {filename}")
    print(f"   Metadata: {content['metadata']}")
    print(f"   Scene info: {content['scene']}")
    print(f"   Objects count: {len(content['objects'])}")
    
    print("\n✅ PyVCAD demonstration completed successfully!")
    print("\nThe library supports:")
    print("   • Basic 3D shapes (Box, Cylinder)")
    print("   • Boolean operations (Union, Subtract)")
    print("   • Scene management and organization")
    print("   • File I/O in JSON-based .vcad format")
    print("   • Vascular modeling workflows")


if __name__ == "__main__":
    main()