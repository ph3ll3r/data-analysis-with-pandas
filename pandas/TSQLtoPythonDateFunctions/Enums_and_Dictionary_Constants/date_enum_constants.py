from enum import Enum

"""Enums 
    1. The strptime() function in Python is used to parse and convert a string representing a date and time into a time object.
       The  StrpTime(Enum) has a variety of dictionary elements that defines strptime() sepcific template for parsing
    
    The syntax for the strptime() function is: strptime(string, format)
    
    where:
            1. string is the string to be parsed.
            2. format is the format of the string to be parsed.
            3. The format string is a string that specifies how the string should be parsed. 
                The format string can contain a variety of different characters, each of which has a different meaning. 
                For example, 
                        I) The %Y character represents the year with century and %Y character represents the year without century
                        II) The %m character represents the month
                    III) The %d character represents the day.
                        IV) The %B character represents the full month name and %b character represents the short month name (Jan)
    
    2. The DateSeparator(Enum) has various separators that can be used with a date format such as:
            slash = "\"
            hyphen = "-""
            space = " "
            none = Is set to true for the absence of using a date separator
            comma = ",""
   
"""
class StrpTime(Enum):
    yyyymmdd = 1
    mmddyyyy = 2
    yymmdd = 3
    mmddyy = 4
    mmyyyy = 5
    mmyy = 6  
    monthname_ddyyyy = 7
    shortmonth_ddyyyy = 8
    monthname_ddyy = 9
    shortmonth_ddyy = 10

class DateSeparator(Enum):
    slash = 1
    hyphen = 2
    space = 3
    none = 4
    comma = 5
