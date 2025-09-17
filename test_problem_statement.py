#!/usr/bin/env python3
"""
Test script with the exact code from the problem statement.
"""

import pyvcad

# 1. Create the cube
cube = pyvcad.Box((0, 0, 0), 10, 10, 10)

# 2. Define vascular paths (example: a simple bifurcation)
vessels = []
main_vessel = pyvcad.Cylinder(start=(5, 5, 0), end=(5, 5, 7), radius=0.5)
branch1 = pyvcad.Cylinder(start=(5, 5, 7), end=(2, 8, 10), radius=0.3)
branch2 = pyvcad.Cylinder(start=(5, 5, 7), end=(8, 2, 10), radius=0.3)
vessels.extend([main_vessel, branch1, branch2])

# 3. Combine all vessels into one object
vascular_structure = pyvcad.Union(vessels)

# 4. Optionally, subtract vessels from cube for hollow channels
hollow_cube = pyvcad.Subtract(cube, vascular_structure)

# 5. Save or visualize
scene = pyvcad.Scene()
scene.add(hollow_cube)
scene.save("vascular_cube.vcad")

print("Problem statement code executed successfully!")