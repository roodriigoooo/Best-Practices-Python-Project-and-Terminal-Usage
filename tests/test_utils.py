import unittest
import sys
import logging
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from src.utils import interactive_visualization, advanced_text_analysis

# Disable logging during unit tests
logging.disable(logging.CRITICAL)

class TestUtils(unittest.TestCase):

    def test_interactive_visualization_scatter(self):
        interactive_visualization([1, 2, 3, 4], chart_type='scatter')
        self.assertTrue(os.path.exists('interactive_chart.html'))
        os.remove('interactive_chart.html')  # Clean up

    def test_interactive_visualization_line(self):
        interactive_visualization([1, 2, 3, 4], chart_type='line')
        self.assertTrue(os.path.exists('interactive_chart.html'))
        os.remove('interactive_chart.html')  # Clean up

    def test_interactive_visualization_invalid_type(self):
        with self.assertRaises(ValueError):
            interactive_visualization([1, 2, 3], chart_type='bar')

    def test_advanced_text_analysis(self):
        text = "Machine learning provides systems the ability to automatically learn and improve from experience."
        result = advanced_text_analysis(text)
        self.assertIsInstance(result['polarity'], float)
        self.assertIsInstance(result['subjectivity'], float)
        self.assertIsInstance(result['keywords'], list)
        self.assertTrue(len(result['keywords']) > 0)

    def test_advanced_text_analysis_empty(self):
        with self.assertRaises(ValueError):
            advanced_text_analysis("")

if __name__ == '__main__':
        unittest.main()