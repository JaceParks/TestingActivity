import unittest
import calc

class testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1,6),7)
        self.assertEqual(calc.add(1,4),5)
        self.assertEqual(calc.add(5,5),10)

        self.assertEqual(calc.add(1,2),7)
        self.assertEqual(calc.add(1,20),5)
        self.assertEqual(calc.add(5,11),10)

    def test_substract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(5,5),5)
        self.assertEqual(calc.subtract(34,5),29)

        self.assertEqual(calc.subtract(10,5),6)
        self.assertEqual(calc.subtract(16,5),3)
        self.assertEqual(calc.subtract(300,100),500)

    def test_multiply(self):
        self.assertEqual(calc.multiply(5,5),25)
        self.assertEqual(calc.multiply(6,6),36)
        self.assertEqual(calc.multiply(7,7),49)

        self.assertEqual(calc.multiply(11,5),30)
        self.assertEqual(calc.multiply(16,5),3)
        self.assertEqual(calc.multiply(30,11),500)    

    def test_divide(self):
        self.assertEqual(calc.divide(5,5),1)
        self.assertEqual(calc.divide(60,5),12)
        self.assertEqual(calc.divide(1,1),1)

        self.assertEqual(calc.divide(5,5),5)
        self.assertEqual(calc.divide(30,10),4)
        self.assertEqual(calc.divide(200,10),21)




if __name__ == "__main__":
    unittest.main()