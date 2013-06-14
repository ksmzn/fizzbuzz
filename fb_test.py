import unittest
import fb_main as fbm

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz_3(self):
        act = fbm.fizzbuzz(3)
        self.assertEqual("Fizz",act)

    def test_fizzbuzz_4(self):
        act = fbm.fizzbuzz(4)
        self.assertEqual("4",act)

    def test_fizzbuzz_5(self):
        act = fbm.fizzbuzz(5)
        self.assertEqual("Buzz",act)

    def test_fizzbuzz_6(self):
        act = fbm.fizzbuzz(6)
        self.assertEqual("Fizz",act)

    def test_fizzbuzz_8(self):
        act = fbm.fizzbuzz(8)
        self.assertEqual("8",act)

    def test_fizzbuzz_10(self):
        act = fbm.fizzbuzz(10)
        self.assertEqual("Buzz",act)

    def test_fizzbuzz_a(self):
        act = fbm.fizzbuzz("a")
        self.assertEqual("a",act)

    def test_fizzbuzz_0(self):
        act = fbm.fizzbuzz(0)
        self.assertEqual("0",act)

    def test_fizzbuzz_nega(self):
        act = fbm.fizzbuzz(-5)
        self.assertEqual("-5",act)


if __name__ == '__main__':
    unittest.main()

