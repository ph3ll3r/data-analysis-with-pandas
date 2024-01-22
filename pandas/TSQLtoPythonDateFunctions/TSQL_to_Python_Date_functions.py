 
    # EE
from datetime import datetime
from enum import Enum
from types import MappingProxyType
from TSQLtoPythonDateFunctions.Enums_and_Dictionary_Constants.date_enum_constants import DateSeparator,StrpTime
from TSQLtoPythonDateFunctions.Enums_and_Dictionary_Constants.date_dictionary_constants import YYYYMMDD, YYMMDD, MMDDYYYY, MMDDYY, MMYYYY, MMYY, MONTHNAME_DDYYYY, SHORTMONTH_DDYYYY, SHORTMONTH_DDYY, MONTHNAME_DDYY,DATE_SEPARATOR
  
class TSQL_to_Python_Date_functions() :
    # _all_date_formats is a private dictionary variable which is made immutable by using the MappingProxyType
    all_date_formats = MappingProxyType(dict( \
                                                    **YYYYMMDD,**YYMMDD,**MMDDYYYY,**MMDDYY,**MMYYYY,**MMYY,  \
                                                    **MONTHNAME_DDYYYY,**SHORTMONTH_DDYYYY,**SHORTMONTH_DDYY, \
                                                    **MONTHNAME_DDYY \
                                                ))

    # _date_separation is a private dictionary variable which is made immutable by using the MappingProxyType
    date_separation = MappingProxyType(DateSeparator,StrpTime)
        
    def __init__(self) -> None:
            self.mm = None
    
 
    def get_month_day_and_year(self,orderdate) -> (int, int, int):  
        #
        ########************  No longer used *********########
        #
        # List of possible date formats
        date_formats = ['%y%m%d', '%Y%m%d', '%m/%d/%Y','%m/%d/%y', '%Y-%m-%d','%y-%m-%d','%d-%m-%Y', '%d/%m/%Y']

        for fmt in date_formats:
            try:
                # Try parsing the date with the current format
                parsed_date = datetime.strptime(orderdate, fmt)
                return parsed_date.month, parsed_date.day, parsed_date.year
            except ValueError:
                # If parsing fails, try the next format
                continue
        # If none of the formats work, raise an error
        raise ValueError("Date format not recognized")
    
    
    def parse_using_date_strptime_format(self,strp_time: StrpTime, date_separator: DateSeparator, orderdate:str) -> (int, int, int):
        
        """Parse a date string into month, day, and year components.

        Args:
            strp_time (StrpTime): The format of the date string.
            date_separator (DateSeparator): The separator used in the date string.
            orderdate (str): The date string to parse.

        Returns:
            tuple: A tuple containing the month, day, and year as integers.
        """    
    separator = date_separation[date_separator.name]
    date_format_info = all_date_formats[strp_time.name]
    date_strptime_template = date_format_info['DATE_FORMAT_NONE'] if date_separator.name == 'none' else date_format_info['DATE_FORMAT_SEPARATOR']
    number_of_separators = date_format_info['NUMBER_OF_SEPARATORS']

    if number_of_separators == 2:
        date_strptime_paramterized_format = date_strptime_template.format(separator, separator)
    elif number_of_separators == 1:
        date_strptime_paramterized_format = date_strptime_template.format(separator)
    else:
        date_strptime_paramterized_format = date_strptime_template
        
    parsed_date = datetime.strptime(orderdate, date_strptime_paramterized_format)
    
    return parsed_date.month, parsed_date.day, parsed_date.year
    