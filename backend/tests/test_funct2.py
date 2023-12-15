import sys
import pandas as pd
import unittest
from fastapi.testclient import TestClient

traffic = pd.read_csv("/app/app/updated_bologna.csv")
traffic['Date'] = pd.to_datetime(traffic['Date'], format='%d/%m/%Y', errors='coerce')


sys.path.append('/app')  # Add the path to the project's base directory

# From app.main import forecasted_visitors_per_area
from app.mymodules.funct2 import traffic_per_area,highest_affluence,lowest_affluence


class TestCall(unittest.TestCase):

    def test_traffic_per_area(self):
       '''
       Test the traffic_per_area function.
       Arrange to 01-10 date, considered as valid
       '''
       result = traffic_per_area(traffic,"01-10")
       result_dc = result.to_dict(orient='dict')
       self.assertEqual(result_dc,{'Area': {0: '2 Torri (Inizio Portico Via Zamboni)', 1: 'Facoltà Di Giurisprudenza', 2: 'Palazzo Poggi', 3: 'Piazza Puntoni (Via Zamboni)', 4: 'Piazza Rossini (Palazzo Malvezzi)', 5: 'Piazza Scaravilli', 6: 'Piazza Verdi', 7: 'Porta San Donato', 8: 'Via Del Guasto', 9: 'Via San Giacomo'}, 'Forcasted_Visitors': {0: 1462, 1: 1616, 2: 1407, 3: 679, 4: 1834, 5: 1174, 6: 2071, 7: 2546, 8: 821, 9: 1735}})


    def test_highest_affluence(self):
       '''
       Test the highest_affluence function.
       Arrange to 01-10 date, considered as valid, taking as input the output from traffic_per_area function
       '''
       
       result = traffic_per_area(traffic,"01-10")
       result_h = highest_affluence(result)

       self.assertEqual(result_h,"The Area with the highest tourism affluence is Porta San Donato with 2546 Forcasted Visitors")


    def test_lowest_affluence(self):
       '''
       Test the lowest_affluence function.
       Arrange to 01-10 date, considered as valid, taking as input the output from traffic_per_area function
       '''
       result = traffic_per_area(traffic,"01-10")
       result_l = lowest_affluence(result)
       self.assertEqual(result_l,"The Area with the lowest tourism affluence is Piazza Puntoni (Via Zamboni) with 679 Forcasted Visitors")


    def test_invalid_date(self):
       '''
       Test traffic_per_are function in case an invalid date is choosen 
       Arrenage to 00-00, considered as invialid since not present in traffic["Date"]
       '''
       result_inv = traffic_per_area(traffic,"00-00")

       self.assertEqual(result_inv,"No data available for the given date.")
    

if __name__ == '__main__':
    unittest.main()
