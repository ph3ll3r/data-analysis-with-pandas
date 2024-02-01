from datetime import datetime
from enum import Enum
from types import MappingProxyType
from dateutil.relativedelta import relativedelta
from .enums_and_dictionary_constants.date_enum_constants import DateSeparator,StrpTime,QuarterAnchorMonth
from .enums_and_dictionary_constants.date_dictionary_constants import YYYYMMDD, YYMMDD, MMDDYYYY, MMDDYY, MMYYYY, MMYY, MONTHNAME_DDYYYY, SHORTMONTH_DDYYYY, SHORTMONTH_DDYY, MONTHNAME_DDYY,DATE_SEPARATOR,QUARTER_ANCHOR_MONTH
  
class tsql_dates() :
    
    # _all_date_formats is a private dictionary variable which is made immutable by using the MappingProxyType
    _all_date_formats = MappingProxyType(dict( \
                                                    **YYYYMMDD,**YYMMDD,**MMDDYYYY,**MMDDYY,**MMYYYY,**MMYY,  \
                                                    **MONTHNAME_DDYYYY,**SHORTMONTH_DDYYYY,**SHORTMONTH_DDYY, \
                                                    **MONTHNAME_DDYY,QUARTER_ANCHOR_MONTH \
                                                ))

    # _date_separation is a private dictionary variable which is made immutable by using the MappingProxyType
    _date_separation = MappingProxyType(DateSeparator,StrpTime,QuarterAnchorMonth)
        
    def __init__(self) -> None:
            self.month = None
            self.day = None
            self.year = None
    
    def parse_using_date_strptime_format(self,strp_time: StrpTime, date_separator: DateSeparator, orderdate:str) -> (int, int, int):
        """
            Method Overview
            
                Name: parse_using_date_strptime_format
                Purpose: To parse a date string into its constituent parts: month, day, and year.
                
                Parameters:
                    strp_time (StrpTime): Represents the expected format of the date string.
                    date_separator (DateSeparator): Indicates the separator used in the date string.
                    orderdate (str): The actual date string to be parsed.
                    
                Returns: A tuple containing the month, day, and year as integers,
                         or an error message in case of invalid input.
        
        """   
        try:
            # Determining the Separator: 
            #   separator = self._date_separation[date_separator.name]: Retrieves the character used as a separator 
            #   in the date string based on the DateSeparator enum.
            # 
            # Formatting the Date String: 
            #   date_format_info = self._all_date_formats[strp_time.name]: Retrieves the date format information based on the StrpTime enum.
            #   date_strptime_template: Determines the template to use for parsing, depending on whether a separator is used.
            #   The code then adjusts the format string to accommodate the number of separators in the date string.
            separator = self._date_separation[date_separator.name]
            date_format_info = self._all_date_formats[strp_time.name]
            date_strptime_template = date_format_info['DATE_FORMAT_NONE'] if date_separator.name == 'none' else date_format_info['DATE_FORMAT_SEPARATOR']
            number_of_separators = date_format_info['NUMBER_OF_SEPARATORS']
            
            if number_of_separators == 2:
                date_strptime_paramterized_format = date_strptime_template.format(separator, separator)
            elif number_of_separators == 1:
                date_strptime_paramterized_format = date_strptime_template.format(separator)
            else:
                date_strptime_paramterized_format = date_strptime_template
                
            # Parsing the Date:
            #   parsed_date = datetime.strptime(orderdate, date_strptime_paramterized_format): 
            #   Parses the orderdate string using the determined format.
            #   The parsed date is then broken down into month, day, and year.

            parsed_date = datetime.strptime(orderdate, date_strptime_paramterized_format)
            
            # Setting and Returning Values:
            # The month, day, and year are set as attributes of the class (self.month, self.day, self.year).
            self.month=parsed_date.month
            self.day=parsed_date.day
            self.year=parsed_date.year
            
            # The method returns a tuple containing these values.     
            return self.month, self.day, self.year
        
        #Error Handling:
        #   If a ValueError is caught, it indicates an invalid date format or value, 
        #   and an error message is returned.
        
        except ValueError:
            return "Invalid date format or value. Please check the input."

    
    
def datediff(self,strp_time: StrpTime, date_separator: DateSeparator, date_part: str, orderdate: str, deliverydate: str) -> int:
    """ 
        `datediff` function is designed to calculate the difference between two dates in various units such as years, months, days, etc. 

    Parameters:
                strp_time: StrpTime: A format specification for parsing the date strings.
                date_separator: DateSeparator: The character used to separate date components in the input strings.
                date_part: str: Specifies the unit for calculating the date difference:

                date_part (str):
                                    YY : Year, year, y, yy, or yyyy
                                    QU : Quarter, quarter, qq, q
                                    MO : Month, month, mm, m
                                    Day: dayofyear, day, dd, d
                                    WK : Week, week, wk, ww
                                    HR : Hour, hour, hh
                                    MI : Minute, minute, mi, n
                                    SS : Second, second, ss, s

                orderdate (str):    is the starting date for the date difference
                deliverydate (str): is the ending date for the date difference

    Returns:
                int: The difference between the two dates in the unit specified by date_part.
    
    1. Create an Instance of the Class:                   
        If parse_using_date_strptime_format is a regular method (not static or class method), 
        you need to create an instance of tsql_dates and then call the method on that instance.
    or 
    Make the Method Static:
        If parse_using_date_strptime_format does not need to access any instance-specific data (i.e., it doesn't use self),
        you can make it a static method. This allows you to call it directly from the class without creating an instance.
    Example:
            class tsql_dates():
                @staticmethod
                def parse_using_date_strptime_format(strp_time, date_separator, date_string):
                    # method implementation

            def datediff(strp_time, date_separator, date_part, orderdate, deliverydate):
                month, day, year = tsql_dates.parse_using_date_strptime_format(strp_time, date_separator, orderdate)
                # rest of your code

    """   
    
    # Instance Creation: The function expects an instance of tsql_dates class or a static method to parse the date strings. 
    # This is essential for converting the date strings into date components.
        # Parsing Dates: It uses parse_using_date_strptime_format method of `tsql_dates`` class to parse orderdate and deliverydate 
        # into year, month, and day components.
        # Date Conversion: The parsed components are then used to create datetime objects for both the start and end dates.
    parser = tsql_dates()
    self.month, self.day , self.year = parser.parse_using_date_strptime_format(strp_time, date_separator, orderdate)
    start_date = datetime(self.year,self.month, self.day)
    self.month, self.day , self.year = parser.parse_using_date_strptime_format(strp_time, date_separator, deliverydate)
    end_date = datetime(self.year,self.month, self.day)
    
    # Calculating Date Difference: The function calculates the difference between 
        # the two dates in various units as specified by date_part. 
        # This is achieved using the relativedelta function from the `dateutil` module.
        
    delta = relativedelta(end_date, start_date)

    # Date Part Units Handling: A dictionary date_part_units maps different units 
    # (like 'YY' for years, 'MO' for months, etc.) to corresponding lambda functions that calculate the difference in those units.
    date_part_units = {
        'YY': lambda: delta.years,
        'QU': lambda: (delta.years * 4) + (delta.months // 3),
        'MO': lambda: (delta.years * 12) + delta.months,
        'DD': lambda: (end_date - start_date).days,
        'WK': lambda: ((end_date - start_date).days // 7),
        'HR': lambda: ((end_date - start_date).total_seconds() // 3600),
        'MI': lambda: ((end_date - start_date).total_seconds() // 60),
        'SS': lambda: (end_date - start_date).total_seconds()
    }

    # Returning the Result: The function returns the result of the lambda function corresponding to the provided date_part.
    # If an unrecognized date_part is provided, it returns None.
    return date_part_units.get(date_part.upper(), lambda: None)()
    

def dateadd(self,strp_time: StrpTime, date_separator: DateSeparator, date_part: str, units_number: int, orderdate: str) -> datetime:
    """
    Function to calculate the units_number to a date based upon the date_part
    Args:
        date_part (str):    YY, QU, MO, Day, WK, HR, MI, SS
                            YY : Year, year, y, yy, or yyyy
                            QU : Quarter, quarter, qq, q
                            MO : Month, month, mm, m
                            Day: dayofyear, day, dd, d
                            WK : Week, week, wk, ww
                            HR : Hour, hour, hh
                            MI : Minute, minute, mi, n
                            SS : Second, second, ss, s

        units_number (int): Number of units to add
        orderdate (str): Starting date in 'M/D/YYYY' or 'M/D/YY' format

    Returns:
        datetime: New date after adding the specified units
    """
    parser = tsql_dates()
    self.month, self.day , self.year = parser.parse_using_date_strptime_format(strp_time, date_separator, orderdate)
    start_date = datetime(self.year,self.month, self.day)
        
    date_part_units = {
        'YY': lambda: start_date + relativedelta(years=units_number),
        'QU': lambda: start_date + relativedelta(months=units_number * 3),
        'MO': lambda: start_date + relativedelta(months=units_number),
        'DD': lambda: start_date + relativedelta(days=units_number),
        'WK': lambda: start_date + relativedelta(weeks=units_number),
        'HR': lambda: start_date + relativedelta(hours=units_number),
        'MI': lambda: start_date + relativedelta(minutes=units_number),
        'SS': lambda: start_date + relativedelta(seconds=units_number),
    }

    return date_part_units.get(date_part.upper(), lambda: None)()

def determine_quarter_and_year(self,quarter_anchor_month:QuarterAnchorMonth, strp_time: StrpTime, date_separator: DateSeparator, orderdate:str) -> str:
    """
        Function Overview
        
        determine_quarter_and_year, is designed to calculate the fiscal or calendar year and quarter based on a given date. 
        It uses several custom types and a date parsing utility to achieve this. 
        
            Purpose: To determine the fiscal or calendar year and quarter for a given date.
            
                Parameters:
                quarter_anchor_month (QuarterAnchorMonth): An enum or similar type that defines the starting month of the fiscal year.
                strp_time (StrpTime): A custom type or structure that defines the format for parsing dates.
                date_separator (DateSeparator): A custom type or structure that defines the separator used in date strings (e.g., '/', '-', etc.).
                orderdate (str): The date string to be parsed and evaluated.
                
            Returns: A string indicating the fiscal or calendar year and quarter.
        
        Date Parsing:
            a. The function begins by creating an instance of a date parser (tsql_dates()).
            b. It then parses the orderdate string into month, day, and year components using the provided strp_time format and date_separator.    
        
    """
    parser = tsql_dates()
    self.month, self.day , self.year = parser.parse_using_date_strptime_format(strp_time, date_separator, orderdate)
    
    # Quarter Data Setup:
        # Retrieves a tuple (quarter_data_tuples) that defines the mapping of months to quarters based on the quarter_anchor_month.
        # This tuple is expected to contain information about which months fall into which quarters.
    quarter_data_tuples = QUARTER_ANCHOR_MONTH[quarter_anchor_month.name]['determine_quarter_tuple']

    # Determining Year Type: 
        # The string format for the output is chosen based on the value of quarter_anchor_month.
        # If the fiscal year starts after January, a fiscal year format is used ("FY{}: Quarter {}");
        # otherwise, a calendar year format is used ("CY{}: Quarter {}").
        
    determined_quarter_string = "FY{}: Quarter {}" if quarter_anchor_month.value > 1 else "CY{}: Quarter {}"
    # `year_plus_one = self.year + 1 if (1 < self.month < 13) and (quarter_anchor_month.value > 1) else self.year: 
       # Adjusts the year based on the month and the fiscal year start month.
       
    year_plus_one = self.year + 1 if (1 < self.month < 13) and (quarter_anchor_month.value > 1) else self.year
    
    # Finding the Quarter: 
      # The quarter number is determined by finding which tuple in quarter_data_tuples the parsed month falls into.
       
    quarter_number = next((quarter for start_month,middle_month, end_month, quarter in quarter_data_tuples if self.month in [start_month,middle_month, end_month]), None)
    
   # If no quarter is found for the given month, the function returns a message indicating no quarter is available for that month.
    if quarter_number is None : return f"No quarter for month {self.month}" 
    
    # Output: 
    # The function returns a string formatted with the year (adjusted for fiscal year considerations) and the quarter number.
    return determined_quarter_string.format(year_plus_one,quarter_number)

    
    