#!/usr/bin/env python3
# Student ID: bpjogi

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__
                            time_to_sec, format_time,
                            change_time, sum_times
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        '''return a string representation for the object self'''
        return  f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
    
    def __repr__(self):
        '''return a string representation for the object self'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'
    
    def __add__(self, t2):
        return self.sum_times(t2)
    
    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'
 
    def sum_times(self, t2):
        """Add two time objects and return the sum as a new Time object."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds % 86400)  # Ensure time stays within a 24-hour format

    def change_time(self, seconds):
        """Modify a time object by adding/subtracting seconds."""
        time_seconds = self.time_to_sec()
        nt = sec_to_time((time_seconds + seconds) % 86400)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second 

    def time_to_sec(self):
        '''Convert a time object to a single integer representing the 
        number of seconds from midnight.'''
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check for the validity of the time object attributes:
        24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0 """
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

def sec_to_time(seconds):
    '''Convert a given number of seconds to a time object in 
       hour, minute, second format.'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
