import unittest
import sys

def sum(a,b):
    return a+b
 
class ModuleTest1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testsum1(self):
        self.assertEqual(sum(1,2),3)
        
    def testsum2(self):
        self.assertEqual(sum(1,-1),0)

    def whatIfNotGood(self):
        self.assertEqual(sum(1,-1),10)
 
if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    for testmethod in ('testsum1', 'testsum2'): #, 'whatIfNotGood'):
        testSuite.addTest(ModuleTest1(testmethod))
    
    runner = unittest.TextTestRunner()
    result = runner.run(testSuite)
    sys.exit(not result.wasSuccessful())
