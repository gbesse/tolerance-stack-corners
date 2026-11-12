import unittest,copy,json
from tolerance_stack_corners import run
DEMO={'terms': [{'id': 'shaft', 'coefficient': 1, 'nominal': 10, 'half_width': 0.2}, {'id': 'hole', 'coefficient': -1, 'nominal': 9, 'half_width': 0.1}]}
class DomainTests(unittest.TestCase):
 def test_negative_coefficient_corner(self):
  x=run(DEMO);self.assertAlmostEqual(x['interval'][0],.7);self.assertAlmostEqual(x['interval'][1],1.3);self.assertEqual(x['extreme_witnesses'][1]['at_minimum'],9.1)
 def test_uniform_not_three_sigma_guarantee(self):
  x=run(DEMO);self.assertAlmostEqual(x['independent_uniform_std'],(.05/3)**.5);self.assertFalse(x['guaranteed_by_std'])
 def test_zero_half_width(self):
  x=run({'terms':[{'id':'fixed','coefficient':2,'nominal':3,'half_width':0}]});self.assertEqual(x['interval'],[6,6])
