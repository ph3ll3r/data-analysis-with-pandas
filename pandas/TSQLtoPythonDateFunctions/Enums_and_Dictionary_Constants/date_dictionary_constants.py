"""Dictionary 
    1. The strptime() function in Python is used to parse and convert a string representing a date and time into a time object.
       The  StrpTime(Enum) has a variety of dictionary elements that defines strptime() sepcific template for parsing

        The following are code snippets to retreive the information from the dictionaries:
        
                        separator = _date_separation[date_separator.name]
                        date_format_info = _all_date_formats[strp_time.name]
        
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
    
    2. The DateSeparator has various separators that can be used with a date format such as:
            DATE_SEPARATOR = {
                'slash': '/',
                'hyphen': '-',
                'space': ' ',
                'comma': ',',
                'none': ''    Is set to true for the absence of using a date separator
}   
"""


DATE_SEPARATOR = {
    'slash': '/',
    'hyphen': '-',
    'space': ' ',
    'comma': ',',
    'none': ''
}

YYYYMMDD = {
    'yyyymmdd': {
        'DESCRIPTION': 'Year with century, month and day',
        'NUMBER_OF_SEPARATORS': 2,
        'DATE_FORMAT_SEPARATOR': '%Y{}%m{}%d',
        'DATE_FORMAT_NONE': '%Y%m%d'
    }
}

YYMMDD = {
    'yymmdd': {
        'DESCRIPTION': 'Year without century, month and day',
        'NUMBER_OF_SEPARATORS': 2,
        'DATE_FORMAT_SEPARATOR': '%y{}%m{}%d',
        'DATE_FORMAT_NONE': '%y%m%d'
    }
}

MMDDYYYY = {
    'mmddyyyy': {
        'DESCRIPTION': 'Month, day, and year with century',
        'NUMBER_OF_SEPARATORS': 2,
        'DATE_FORMAT_SEPARATOR': '%m{}%d{}%Y',
        'DATE_FORMAT_NONE': '%m%d%Y'
    }
}

MMDDYY = {
    'mmddyy': {
        'DESCRIPTION': 'Month, day, and year without century',
        'NUMBER_OF_SEPARATORS': 2,
        'DATE_FORMAT_SEPARATOR': '%m{}%d{}%y',
        'DATE_FORMAT_NONE': '%m%d%y'
    }
}

MMYYYY = {
    'mmyyyy': {
        'DESCRIPTION': 'Month, no days and year with century',
        'NUMBER_OF_SEPARATORS': 1,
        'DATE_FORMAT_SEPARATOR': '%m{}%Y',
        'DATE_FORMAT_NONE': '%m%Y'
    }
}

MMYY = {
    'mmyy': {
        'DESCRIPTION': 'Month, no days and year without century',
        'NUMBER_OF_SEPARATORS': 1,
        'DATE_FORMAT_SEPARATOR': '%m{}%y',
        'DATE_FORMAT_NONE': '%m%y'
    }
}

MONTHNAME_DDYYYY = {'monthname_ddyyyy': 
                {
                    'DESCRIPTION': 'full month name, day and Year with century,',
                    'NUMBER_OF_SEPARATORS': 1,
                    'DATE_FORMAT_SEPARATOR': '%B %d{} %Y',
                    'DATE_FORMAT_NONE': '%B %d %Y'
                }
            }

SHORTMONTH_DDYYYY = {'shortmonth_ddyyyy': 
                {
                    'DESCRIPTION': 'short month name, day and Year with century,',
                    'NUMBER_OF_SEPARATORS': 1,
                    'DATE_FORMAT_SEPARATOR': '%b %d{}%Y',
                    'DATE_FORMAT_NONE': '%b %d %Y'
                }
            }

MONTHNAME_DDYY = {'monthname_ddyy': 
                {
                    'DESCRIPTION': 'full month name, day and Year without century,',
                    'NUMBER_OF_SEPARATORS': 1,
                    'DATE_FORMAT_SEPARATOR': '%B %d{} %y',
                    'DATE_FORMAT_NONE': '%B %d %y'
                }
            }

SHORTMONTH_DDYY = {'shortmonth_ddyy': 
                {
                    'DESCRIPTION': 'short month name, day and Year without century,',
                    'NUMBER_OF_SEPARATORS': 1,
                    'DATE_FORMAT_SEPARATOR': '%b %d{} %y',
                    'DATE_FORMAT_NONE': '%b %d %y'
                }
            }
