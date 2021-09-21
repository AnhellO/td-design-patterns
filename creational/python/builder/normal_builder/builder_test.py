import unittest

from builder import *

class BuilderTest(unittest.TestCase):
    def test_create_car_without_builder(self):
        car = Car(5, 'standard', 10, True)

        self.assertEqual(5, car.seats)
        self.assertEqual('standard', car.engine)
        self.assertEqual(10, car.trip_computer)
        self.assertEqual(True, car.gps)
        
    def test_simple_car_creation_with_builder_but_without_director(self):
        builder = CarBuilder()
        builder.set_seats(5)
        builder.set_engine('standard')
        builder.set_trip_computer(10)
        builder.set_gps(True)
        car = builder.get_result()

        self.assertEqual(5, car.seats)
        self.assertEqual('standard', car.engine)
        self.assertEqual(10, car.trip_computer)
        self.assertEqual(True, car.gps)

if __name__ == "__main__":
    unittest.main()
