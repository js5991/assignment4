'''
Created on Nov 13, 2016

@author: Jingyi Su (js5991)
'''
from Interval.Interval import *
import unittest


class Test(unittest.TestCase):

    def test_interval_valids(self):
        self.valid_test_set=['(2,10)','[-6,0]', '[3,17)', '(-6,2]','( 2,10)','[-6,0 ]', ' [3,17)', '(-6, 2] ']
        self.valid_answer_set=['(2,10)','[-6,0]', '[3,17)', '(-6,2]','(2,10)','[-6,0]', '[3,17)', '(-6,2]']
        self.assertListEqual(list(map(lambda x: str(interval(x)),self.valid_test_set)),self.valid_answer_set)

    def test_interval_error(self):
        self.error_test_set=['foo','','[,]','[2,2,3]','[,[2,4]]','[3.2,5)','(10,0)']
        for item in self.error_test_set:
            with self.assertRaises(ValueError):
                interval(item)
    
    def test_mergeIntervals_valid(self):
        self.merge_test_set=[[interval('[1,4]'), interval('[5,10)')],[interval('[1,9)'), interval('[5,14)')],[interval('[2,7)'), interval('(1,15)')]]
        self.merge_answer_set=[interval('[1,10)'),interval('[1,14)'),interval('(1,15)')]
        self.assertListEqual(list(map(lambda x: mergeIntervals(x[0], x[1]),self.merge_test_set)),self.merge_answer_set)
        
    def test_mergeIntervals_error(self):
        self.merge_error_test_set=[[interval('[1,2]'), interval('[5,10)')],[interval('[1,9)'), interval('[-2,-1)')]]
        for item in self.merge_error_test_set:
            with self.assertRaises(ValueError):
                mergeIntervals(item[0],item[1])
        
    def test_mergeOverlapping(self):
        self.mergeOverlapping_test_set=[[interval('[1,2]'), interval('[5,10]'), interval('(10,12]'), interval('[-3,-1)')],[interval('[1,9)'), interval('[-2,1)'),interval('(100,199)'), interval('[70,150)')]]
        self.mergeOverlapping_answer_set=[[interval('[-3,-1)'), interval('[1,2]'), interval('[5,12]')],[interval('[-2,9)'), interval('[70,199)')]]
        self.assertListEqual(list(map(lambda x: mergeOverlapping(x),self.mergeOverlapping_test_set)),self.mergeOverlapping_answer_set)

    def test_insert(self):
        self.insert_test_set=[[interval('[1,2]'), interval('[5,10]'), interval('(10,12]'), interval('[-3,-1]')],[interval('[1,9)'), interval('[-2,1)'),interval('(100,199)'), interval('[70,150)')]]
        self.insert_items=[interval('(-1,2]'), interval('[5,16]')]
        self.insert_answer_set=[[interval('[-3,2]'), interval('[5,12]')],[interval('[-2,16]'), interval('[70,199)')]]
        self.assertListEqual(list(map(lambda x,y: insert(x,y),self.insert_test_set,self.insert_items)),self.insert_answer_set)    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_interval_valids','test_interval_error','test_mergeIntervals_valid','test_mergeIntervals_error','test_mergeOverlapping','test_insert']
    unittest.main()