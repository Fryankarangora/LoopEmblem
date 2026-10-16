# test_loopemblem.py
"""
Tests for LoopEmblem module.
"""

import unittest
from loopemblem import LoopEmblem

class TestLoopEmblem(unittest.TestCase):
    """Test cases for LoopEmblem class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LoopEmblem()
        self.assertIsInstance(instance, LoopEmblem)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LoopEmblem()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
