import unittest
import piglatin as pl

class TestParseCommandLine(unittest.TestCase):
   
    def test_noinput(self):
       self.assertEqual(pl.parseCommandLine([],''))
       self.assertEqual(pl.parseCommandLine(['filename'],''))
"""
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
"""

if __name__ == '__main__':
    unittest.main()
