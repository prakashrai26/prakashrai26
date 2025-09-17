#!/usr/bin/env python3
"""
Simple tests to verify PyVCAD functionality.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

import pyvcad


def test_basic_shapes():
    """Test basic shape creation."""
    print("Testing basic shapes...")
    
    # Test Box creation
    box = pyvcad.Box((0, 0, 0), 10, 5, 3)
    assert box.width == 10
    assert box.height == 5
    assert box.depth == 3
    assert box.origin == (0, 0, 0)
    
    # Test Cylinder creation
    cylinder = pyvcad.Cylinder((0, 0, 0), (0, 0, 10), 2.5)
    assert cylinder.start == (0, 0, 0)
    assert cylinder.end == (0, 0, 10)
    assert cylinder.radius == 2.5
    assert abs(cylinder.length - 10.0) < 0.001
    
    print("✓ Basic shapes test passed")


def test_operations():
    """Test boolean operations."""
    print("Testing boolean operations...")
    
    # Create shapes
    box1 = pyvcad.Box((0, 0, 0), 10, 10, 10)
    box2 = pyvcad.Box((5, 5, 5), 10, 10, 10)
    cylinder = pyvcad.Cylinder((0, 0, 0), (10, 10, 10), 1.0)
    
    # Test Union
    union = pyvcad.Union([box1, box2])
    assert len(union.shapes) == 2
    assert union.operation_type == "union"
    
    # Test Subtract
    subtract = pyvcad.Subtract(box1, cylinder)
    assert subtract.base_shape == box1
    assert len(subtract.subtract_shapes) == 1
    assert subtract.operation_type == "subtract"
    
    print("✓ Boolean operations test passed")


def test_scene():
    """Test scene management."""
    print("Testing scene management...")
    
    # Create scene
    scene = pyvcad.Scene("Test Scene")
    assert scene.name == "Test Scene"
    assert len(scene) == 0
    
    # Add objects
    box = pyvcad.Box((0, 0, 0), 5, 5, 5)
    scene.add(box)
    assert len(scene) == 1
    
    # Test bounds
    bounds = scene.get_bounds()
    assert bounds == ((0, 0, 0), (5, 5, 5))
    
    print("✓ Scene management test passed")


def test_file_operations():
    """Test file save/load operations."""
    print("Testing file operations...")
    
    # Create a simple scene
    box = pyvcad.Box((1, 2, 3), 4, 5, 6)
    scene = pyvcad.Scene("File Test Scene")
    scene.add(box)
    
    # Save to file
    test_filename = "/tmp/test_scene.vcad"
    scene.save(test_filename)
    
    # Check file exists
    assert os.path.exists(test_filename)
    
    # Check file content
    with open(test_filename, 'r') as f:
        content = f.read()
        assert "File Test Scene" in content
        assert "box" in content
    
    print("✓ File operations test passed")


def test_complex_vascular_model():
    """Test the complete vascular modeling workflow."""
    print("Testing complex vascular model...")
    
    # This is the exact code from the problem statement
    cube = pyvcad.Box((0, 0, 0), 10, 10, 10)
    
    vessels = []
    main_vessel = pyvcad.Cylinder(start=(5, 5, 0), end=(5, 5, 7), radius=0.5)
    branch1 = pyvcad.Cylinder(start=(5, 5, 7), end=(2, 8, 10), radius=0.3)
    branch2 = pyvcad.Cylinder(start=(5, 5, 7), end=(8, 2, 10), radius=0.3)
    vessels.extend([main_vessel, branch1, branch2])
    
    vascular_structure = pyvcad.Union(vessels)
    hollow_cube = pyvcad.Subtract(cube, vascular_structure)
    
    scene = pyvcad.Scene()
    scene.add(hollow_cube)
    
    test_filename = "/tmp/test_vascular_cube.vcad"
    scene.save(test_filename)
    
    # Verify the model was created correctly
    assert len(vascular_structure.shapes) == 3
    assert hollow_cube.base_shape == cube
    assert len(scene) == 1
    assert os.path.exists(test_filename)
    
    print("✓ Complex vascular model test passed")


def run_all_tests():
    """Run all tests."""
    print("Running PyVCAD tests...\n")
    
    try:
        test_basic_shapes()
        test_operations()
        test_scene()
        test_file_operations()
        test_complex_vascular_model()
        
        print("\n🎉 All tests passed! PyVCAD is working correctly.")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)