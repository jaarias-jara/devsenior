import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../src')))

from negocio import VendedorBase, VendedorPremiun
import unittest
 
class TestVendedor(unittest.TestCase)
    
    def setUp(self):
        self.Vendedor_base = VendedorBase("luisito", 1000)
        self.Vendedor_premiun = VendedorPremiun("carlitos", 1000)