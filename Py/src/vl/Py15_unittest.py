
####################################################
# Unittests
#

# Pruefling, ggf importieren
def my_function(m):
    if m==0: return 10
    if m==1: return 20
    if m==2: return -1
    return 0

import unittest
 
# erster Testfall fuer my_function
#     Zusammenfassung gleichartiger Tests
class Test_my_function(unittest.TestCase):   # abgeleitet von TestCase
    
    def setUp(self):
        # wird vor jeder Testmethode ausgeführt
        self.data = [0, 1,  2,  3]
        self.soll = [10, 20, 1,  0]
    
    # ggf tearDown()
    # siehe auch setUpClass(), tearDownClass()
    
    # Praefix 'test' muss sein
    def test_special_case(self):
        m = 1
        self.assertEqual(my_function(m), 20)
    
    def test_all_values(self):
        for i in range(len(self.data)):
            self.assertEqual(my_function(self.data[i]), self.soll[i])

# Noch ein Testfall
class another_Test_my_function(unittest.TestCase):
    
    def test_myfunc(self):
        self.assertEqual(my_function(-1), 0)

# ausfuehren in Eclipse mit Run as / python unit-test
# oder manuell im Interpreter:

# alle Testmethoden aus der Testklasse einer Suite hinzufuegen
# suite = unittest.TestLoader().loadTestsFromTestCase(Test_my_function)
# bestimmte Testmethode einer Testklasse ergaenzen 
# suite.addTest(another_Test_my_function('test_my_function'))
# Suite ausfuehren
# unittest.TextTestRunner(verbosity=2).run(suite)

