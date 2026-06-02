 import unittest

import psutil

class TestMonitorAgent(unittest.TestCase):

    def test_cpu_metrics_format(self):

        cpu = psutil.cpu_percent(interval=0.1)

        self.assertIsInstance(cpu, float)


    def test_ram_metrics_bounds(self):

        ram = psutil.virtual_memory().percent

        self.assertTrue(0 <= ram <= 100)

if __name__ == '__main__':

    un

ittest.main()    
