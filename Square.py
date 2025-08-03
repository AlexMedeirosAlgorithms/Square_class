"""
This program provides functionality to define a square and calculate its area and volume. 

Code References for Class: https://realpython.com/python-classes/
"""

class Square:
    """
    Class used to represent a square.
    
    Attributes- 
        'side' : (int)
        'units' : (str)
    Methods- 
        'calculate_area' : returns (int): value of square area
        'calculate_volume' : returns (int): value of cubic volume

    Usage example:
        square = Square(1,"inches")
        square.calculate_area()
    """
    
    def __init__(self, side, units):
        """ 
        Constructs all the necessary attributes for the square object. 
        
        Parameters- 
            side : (int), the length of a side for the square
            units : (str), the units of a side for the square
        """
        self.side = side
        self.units = units

    def side(self):
        """returns (int): value of object side."""
        return self.side # return side value
    
    def units(self):
        """returns (str): units of object side."""
        return self.units # return units

    def calculate_area(self):
        """ Method to calculate the area of a square. Area = Side**2. Prints the area to display for the user. 
                returns (int): square area calculated using 'side' attribute."""

        self.area = round(self.side**2,2) # calculate the area
        print(f'Area of square = {str(self.area) + " square " + self.units}') # print area to display for the user 

        return self.area # return area

    def calculate_volume(self):
        """ Method to calculate the volume of a square. Volume = Side**3. Prints the volume to display for the user. 
                returns (int): cubic volume calculated using 'side' attribute."""

        self.volume = round(self.side**3,2) # calculate the volume
        print(f'Volume of square = {str(self.volume) + " cubic " + self.units}') # print volume to display for the user

        return self.volume # return volume
    
if __name__=="__main__":
    sq1=Square(2, "inches") # instantiate a square with side size = 2, units are "inches"

    print(f'Square side size = {sq1.side}') # print the size of side
    print(f'Square side units = {sq1.units}') # print the units of side

    area = sq1.calculate_area() # calculate the area of the square
    
    volume = sq1.calculate_volume() # calculate the volume of the square
    

