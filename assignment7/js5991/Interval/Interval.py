'''
Created on Nov 13, 2016

@author: Jingyi Su (js5991)
'''

class interval(object):
    
    def __init__(self, int_str):
        '''
        Constructor
        '''
        self.inputstr=int_str.strip()
        lower_sign=['(','[']
        upper_sign=[')',']']
        
        if int_str=='':
            raise ValueError('Invalid Input: Need an input')
        if self.inputstr[0] not in lower_sign or self.inputstr[-1] not in upper_sign:
            raise ValueError ('Invalid Input: Need an interval with bounds')
        try:
            self.num_range=list(map(int,self.inputstr[1:-1].split(",")))
            if len(self.num_range)!=2:
                raise ValueError('Invalid Input: Two bounds are needed')
            
            self.lower_inclusive=self.num_range[0]+1-lower_sign.index(self.inputstr[0])
            self.upper_inclusive=self.num_range[1]-1+upper_sign.index(self.inputstr[-1])
            if self.lower_inclusive>self.upper_inclusive:
                raise ValueError ('Invalid Input: Need logical upper and lower bounds')
                    
            self.lower=(self.inputstr[0],self.num_range[0])
            self.upper=(self.inputstr[-1],self.num_range[1])
            
        except ValueError: 
            raise ValueError('Invalid Input: Need interger inputs')
        
    def __repr__(self, *args, **kwargs):
        '''
        this function prints interval object
        '''
        return str(self.lower[0])+str(self.lower[1])+","+str(self.upper[1])+str(self.upper[0])
    
    def __eq__(self,other):
        '''
        This function check whether two intervals are the same despite the differences in formatting
        '''
        #Two intervals should be equal if the included lowest&highest bounds are the same
        #E.g. [2,5]=(1,6)=(1,5]=[2,6)
        if not isinstance(other, interval):
            return False
        if self.lower_inclusive==other.lower_inclusive and self.upper_inclusive==other.upper_inclusive:
            return True
        else: return False

def mergeable (int1, int2):
    '''
    This function checks whether two interval objects are mergeable. It takes two arguments, both are interval objects.
    '''
    if (int1.lower_inclusive<int2.lower_inclusive and int1.upper_inclusive+1<int2.lower_inclusive) or (int2.lower_inclusive<int1.lower_inclusive and int2.upper_inclusive+1<int1.lower_inclusive):
        return False
    return True

def mergeIntervals(int1, int2):
    '''
    This function merges the two interval objects if possible. It takes two arguments, both are interval objects.
    '''
    #Check whether the intervals are mergeable
    if mergeable(int1, int2)==False:
            raise ValueError ('Cannot Merge Intervals: Two intervals are not overlapped or adjacent')
        
    #Merge interval by re-define the interval bounds
    if int1.lower_inclusive<=int2.lower_inclusive:
        new_lower=int1.lower
    else: new_lower=int2.lower
    
    if int1.upper_inclusive>=int2.upper_inclusive:
        new_upper=int1.upper
    else: new_upper=int2.upper
    
    #define the merged interval
    newintervalstr=str(new_lower[0])+str(new_lower[1])+","+str(new_upper[1])+str(new_upper[0])
    return interval(newintervalstr)

def mergeOverlapping(intervals):
    '''
    This function merges all the overlapping and adjacent intervals from a list of intervals.It takes one argument of a list of interval objects, and returns the merged list.
    '''
    #sort interval list based on lower bound
    intervals.sort(key= lambda x: x.lower_inclusive)
    
    #merge all mergeable intervals
    result=[intervals[0]]
    for i in range(1, len(intervals)):
        if mergeable(result[-1],intervals[i]):
            result[-1]=mergeIntervals(result[-1],intervals[i])
        else:
            result.append(intervals[i])      
    return result

def insert(intervals, newint):
    '''
    This function inserts one new interval in to the existing list of non-overlapping intervals, and merges the results when possible.
    '''
    intervals.append(newint)
    return mergeOverlapping(intervals)


        
            
        