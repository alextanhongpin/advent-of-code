import unittest
from main_07 import bag_contained_by, bag_contains

class TestBagContains(unittest.TestCase):
  def test_bag_contains(self):
    rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split('\n')
    n = bag_contained_by(rules)
    self.assertEqual(n, 4)

  def test_bag_has(self):
    rules = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".split('\n')
    n = bag_contains(rules)
    self.assertEqual(n, 126)


if __name__ == '__main__':
  unittest.main()