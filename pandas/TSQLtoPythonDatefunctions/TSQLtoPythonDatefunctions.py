class TSQLtoPythonDatefunctions() :
    
    from datetime import datetime,date

    def __init__(self) -> None:
        pass
    
    def get_month_day_and_year(self,orderdate) -> (int, int, int):
        """_summary_

        Args:
            orderdate (_type_): _description_
            int (_type_): _description_
            int (_type_): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """    
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