"""
This module has the class to define a Customer

Author. Miguel Sanabria <masanabriap@udistrital.edu.co>

This file is part of ArcadeSeller.

ArcadeSeller is free software: you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published by the Free 
Software Foundation, either version 3 of the License, or (at your option) 
any later version.

ArcadeSeller is distributed in the hope that it will be useful, but WITHOUT 
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
ArcadeSeller. If not, see <https://www.gnu.org/licenses/>.

"""

class Customer():
    """
    This class represents the behavior of a customer in the application
    """
    def __init__(self, Name: str, Email: str, Address: str, ):
        self.__id = id
        self.__Name = Name
        self.__Email = Email
        self.__Address = Address

    def __str__(self):
        return f"Name: {self.__Name}\nEmail:{self.__Email}\nAddress: {self.__Address}\n"