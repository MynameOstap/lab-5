"""
Module: Lab 5
"""

class Room:
    """
    Represents a room with household appliances.
    """

    def __init__(self):
        """
        Initializes an empty room.
        """
        self.appliances = []

    def rearrangement(self, x_coord, y_coord, new_x_coord, new_y_coord):
        """
        Moves the coordinates of a household appliance within the room.

        Parameters:
        - x_coord (float): Current x-coordinate.
        - y_coord (float): Current y-coordinate.
        - new_x_coord (float): New x-coordinate.
        - new_y_coord (float): New y-coordinate.
        """
        for appliance in self.appliances:
            if appliance.get_coordinates() == (x_coord, y_coord):
                appliance.set_coordinates(new_x_coord, new_y_coord)
        return x_coord, y_coord, new_x_coord, new_y_coord

    def add_appliance(self, appliance):
        """
        Adds a household appliance to the room.

        Parameters:
        - appliance (Appliance): Household appliance to add.
        """
        self.appliances.append(appliance)

    def __str__(self):
        """
        Returns a string representation of the room.
        """
        return f'Room: {self.appliances}'

    def remove_appliance(self, x_coord, y_coord):
        """
        Removes a household appliance from the room based on its coordinates.

        Parameters:
        - x_coord (float): x-coordinate of the appliance.
        - y_coord (float): y-coordinate of the appliance.
        """
        for appliance in self.appliances:
            if appliance.get_coordinates() == (x_coord, y_coord):
                self.appliances.remove(appliance)


class Appliance:
    """
    Represents a general household appliance with coordinates.
    """

    def __init__(self, x_coord: float, y_coord: float):
        """
        Initializes an appliance with coordinates.

        Parameters:
        - x_coord (float): x-coordinate of the appliance.
        - y_coord (float): y-coordinate of the appliance.
        """
        self.coordinates = x_coord, y_coord

    def set_coordinates(self, x_coord, y_coord):
        """
        Sets new coordinates for the appliance.

        Parameters:
        - x_coord (float): New x-coordinate.
        - y_coord (float): New y-coordinate.
        """
        self.coordinates = x_coord, y_coord

    def get_coordinates(self):
        """
        Returns the coordinates of the appliance.
        """
        return self.coordinates


class Bed(Appliance):
    """
    Represents a household appliance - a bed.
    """

    def __init__(self, x_coord: float, y_coord: float, color: str):
        """
        Initializes a bed with coordinates and color.

        Parameters:
        - x_coord (float): x-coordinate of the bed.
        - y_coord (float): y-coordinate of the bed.
        - color (str): Color of the bed.
        """
        super().__init__(x_coord, y_coord)
        self.color = color

    def set_color(self, color: str):
        """
        Sets the color of the bed.

        Parameters:
        - color (str): New color of the bed.
        """
        self.color = color

    def get_color(self):
        """
        Returns the color of the bed.
        """
        return self.color

    def __repr__(self):
        """
        Returns a string representation of the bed.
        """
        return f'Bed xy = {self.coordinates} Color = {self.color}'


class Table(Appliance):
    """
    Represents a household appliance - a table.
    """

    def __init__(self, x_coord: float, y_coord: float, material: str):
        """
        Initializes a table with coordinates and material.

        Parameters:
        - x_coord (float): x-coordinate of the table.
        - y_coord (float): y-coordinate of the table.
        - material (str): Material of the table.
        """
        super().__init__(x_coord, y_coord)
        self.material = material

    def __repr__(self):
        """
        Returns a string representation of the table.
        """
        return f'Table xy = {self.coordinates} Material = {self.material}'

    def set_material(self, material: str):
        """
        Sets the material of the table.

        Parameters:
        - material (str): New material of the table.
        """
        self.material = material

    def get_material(self):
        """
        Returns the material of the table.
        """
        return self.material


class Carpet(Appliance):
    """
    Represents a household appliance - a carpet.
    """

    def __init__(self, x_coord: float, y_coord: float, picture: str):
        """
        Initializes a carpet with coordinates and a picture.

        Parameters:
        - x_coord (float): x-coordinate of the carpet.
        - y_coord (float): y-coordinate of the carpet.
        - picture (str): Picture on the carpet.
        """
        super().__init__(x_coord, y_coord)
        self.picture = picture

    def set_picture(self, picture: str):
        """
        Sets the picture on the carpet.

        Parameters:
        - picture (str): New picture on the carpet.
        """
        self.picture = picture

    def get_picture(self):
        """
        Returns the picture on the carpet.
        """
        return self.picture

    def __repr__(self):
        """
        Returns a string representation of the carpet.
        """
        return f'Carpet xy = {self.coordinates} Ornament = {self.picture}'

def main():
    '''
    Executes the main program.
    '''
    room = Room()
    room.add_appliance(Bed(1, 2, 'McQueen'))
    room.add_appliance(Table(4, 3, 'Trotyle'))
    room.add_appliance(Carpet(3, 6, 'Billy Harrington and Johnny Sins hugging'))
    print(room)
    room.remove_appliance(1, 2)
    print(room)
    room.rearrangement(4, 3, 8, 7)
    print(room)

if __name__ == '__main__':
    main()
