## Hi there 👋

![C](https://img.shields.io/badge/C-%2300599C.svg?style=plastic&logo=c&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54) ![MATLAB](https://img.shields.io/badge/MATLAB-%23e16737.svg?style=plastic&logo=mathworks&logoColor=white) ![SOLIDWORKS](https://img.shields.io/badge/SOLIDWORKS-%23ed1c24.svg?style=plastic&logo=solidworks&logoColor=white)

## PyVCAD - Python Vascular Computer-Aided Design Library

A Python library for creating 3D geometric objects and performing boolean operations for vascular modeling and design.

### Features

- **Basic 3D Shapes**: Create boxes, cylinders, and other geometric primitives
- **Boolean Operations**: Union, subtraction, and intersection operations
- **Scene Management**: Organize and manage 3D objects in scenes
- **File I/O**: Save and load scenes in JSON-based .vcad format
- **Vascular Modeling**: Specifically designed for medical and biological applications

### Quick Start

```python
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
```

### Installation

```bash
python setup.py install
```

Or run the example directly:

```bash
python example_vascular_cube.py
```

![](https://github-readme-stats.vercel.app/api?username=prakashrai26&show_icons=true&theme=dark&hide_border=false&include_all_commits=true&count_private=true)

[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/prakashbantawarai) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/[bimal-thapa-magar-6582b0256](https://www.linkedin.com/in/prakashrai1999/)) [![Email](https://img.shields.io/badge/Email-Here-red?style=plastic&logo=gmail)](mailto:prakash.bantawa484@gmail.com) <img src="https://visitor-badge.laobi.icu/badge?page_id=prakashrai26.prakashrai26&title=Profile%20Views" alt="Profile Views"/>
