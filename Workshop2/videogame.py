"""
This module has the class to define a Videogame

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
from abc import ABC, abstractmethod

class Videogame(ABC):
    """
    This abstract class reperesents the behavior of a Videogame
    """

    @abstractmethod
    def __str__(self):
        pass

class hd_videogame(Videogame):
    """
    This class represents the behavior of an HD Videogame
    """
    def __init__(self, name: str, storytelling_creator: str, graphics_creator: str, category: str, hd_price: int, year: str):
        self.__name = name
        self.__storytelling_creator = storytelling_creator
        self.__graphics_creator = graphics_creator
        self.__category = category
        self.__hd_price = 10000
        self.__year = year
    
    def __str__(self) -> str:
        return f"Name: {self.__name} \n Story Creator: {self.__storytelling_creator} \n Graphics Creator: {self.__graphics_creator} \n\
              Category: {self.__category} \n Price: {self.__hd_price} \n Year: {self.__year}"

class standard_videogame(Videogame):
    """
    This class represents the behavior of an Standard Videogame
    """
    def __init__(self,  name: str, storytelling_creator: str, graphics_creator: str, category: str, standard_price: int, year: str):
        self.__name = name
        self.__storytelling_creator = storytelling_creator
        self.__graphics_creator = graphics_creator
        self.__category = category
        self.__standard_price = 4000
        self.__year = year
    
    def __str__(self) -> str:
        return f"Name: {self.__name} \n\
              Story Creator: {self.__storytelling_creator} \n\
                  Graphics Creator: {self.__graphics_creator} \n\
                      Category: {self.__category} \n Price: {self.__standard_price} \n\
                          Year: {self.__year}"
    
class videogame_factory:
    """
    This class work as a factory to create the videogames
    """

    @staticmethod
    def create_vg(vg_type: int, name: str, storytelling_creator: str, graphics_creator: str, category: str, year: str) -> Videogame:
        """
        This static method allows to create a videogame depending on its type

        Args:
        vg_type(str): Type of the videogmae (HD or Standard)

        Returns:
        Videogame: A videogame that contains the data entered
        """

        if vg_type == 1:
            return hd_videogame(name, storytelling_creator, graphics_creator, category, 10000, year)
        elif vg_type == 2:
            return standard_videogame(name, storytelling_creator, graphics_creator, category, 4000, year)