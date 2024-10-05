"""
This module has the class to define an Arcade Machine

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
from videogame import videogame_factory



class Arcade(ABC):
    """
    This class represents the behavior of an arcade machine.
    """
    @abstractmethod
    def add_videogame(self, Videogame: videogame_factory):
        """
        This method adds a videogame to the machine that is being buyed

        Args:
        Videogame(Videogame): data of the videogame to be added
        """

    @abstractmethod
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def get_baseprice(self) -> float:
        """
        Shows the base price of a Racing Arcade Machine
        """
    
    @abstractmethod
    def set_baseprice(self, price: float):
        """
        Sets the base price of an Arcade Machine
        """

    @abstractmethod
    def get_weight(self) -> float:
        """
        Shows the base price of an Arcade Machine
        """
    
    @abstractmethod
    def set_weight(self, weight: float):
        """
        Sets the weight of an Arcade Machine
        """

    @abstractmethod
    def get_power(self) -> float:
        """
        Shows the power consumption of an Arcade Machine
        """
    
    @abstractmethod
    def set_power(self, power: float):
        """
        Sets the power consumption of an Arcade Machine
        """

class DanceRevolution(Arcade):
    """
    This class represents the behavior of a dance revolution arcade machine.
    """
    def __init__(self, material:str):
        self.__difficulties = "Easy, Medium, Hard, Extreme"
        self.__arrow_cardinalities = "arrow_cardinalities"
        self.__controls_price = 80000
        self.__material = material
        self.__dimensions = "150cm x 54cm"
        self.__weight = 80
        self.__power_con = 85
        self.__memory = "16 GB"
        self.__processors = "i7 3rd Gen"
        self.__base_price = 350000
        self.__videogames = []

    def add_videogame(self, Videogame: videogame_factory):
        self.__videogames.append(Videogame)

    def __str__(self):
        if self.__material == 1:
            self.__material = "Wood"
        elif self.__material == 2:
            self.__material = "Aluminium"
        elif self.__material == 3:
            self.__material = "Carbon Fiber"
        return f"Material: {self.__material}\nDimensions: {self.__dimensions}\nWeight: {self.__weight}\n\
            Power Consumption: {self.__power_con}\nMemory: {self.__memory}\nProccesor: {self.__processors}\n\
                Base Price: {self.__base_price}\nControls Price: {self.__controls_price}\n\
                    Difficulties: {self.__difficulties}\nArrow Cardinalities: {self.__arrow_cardinalities}"
    
    def get_baseprice(self) -> float:
        return self.__base_price
    
    def set_baseprice(self, price: float):
        self.__base_price = price

    def get_weight(self) -> float:
        return self.__weight
    
    def set_weight(self, weight: float):
        self.__weight = weight

    def get_power(self) -> float:
        return self.__power_con
    
    def set_power(self, power: float):
        self.__power_con = power

class ClassicalArcade(Arcade):
    """
    This class represents the behavior of a classical arcade machine.
    """
    def __init__(self, material:str, make_vibration: str, sound_record_alert: str):
        self.__make_vibration = make_vibration
        self.__arrow_sound = sound_record_alert
        self.__material = material
        self.__dimensions = "150cm x 54cm"
        self.__weight = 80
        self.__power_con = 85
        self.__memory = "8 GB"
        self.__processors = "i5 3rd Gen"
        self.__base_price = 300000
        self.__videogames = []

    def add_videogame(self, Videogame: videogame_factory):
        self.__videogames.append(Videogame)

    def __str__(self):
        if self.__material == 1:
            self.__material = "Wood"
        elif self.__material == 2:
            self.__material = "Aluminium"
        elif self.__material == 3:
            self.__material = "Carbon Fiber"
        return f"Material: {self.__material}\nDimensions: {self.__dimensions}\nWeight: {self.__weight}\n\
            Power Consumption: {self.__power_con}\nMemory: {self.__memory}\nProccesor: {self.__processors}\n\
                Base Price: {self.__base_price}\nMake Vibration: {self.__make_vibration}\n\
                    Arrow Sound: {self.__arrow_sound}"
    
    def get_baseprice(self) -> float:
        return self.__base_price
    
    def set_baseprice(self, price: float):
        self.__base_price = price

    def get_weight(self) -> float:
        return self.__weight
    
    def set_weight(self, weight: float):
        self.__weight = weight

    def get_power(self) -> float:
        return self.__power_con
    
    def set_power(self, power: float):
        self.__power_con = power
    
class ShootingArcade(Arcade):
    """
    This class represents the behavior of a shooting arcade machine.
    """
    def __init__(self, material:str, weapons_design: str):
        self.__controls_price = 120000
        self.__weapons_design = weapons_design
        self.__material = material
        self.__dimensions = "170cm x 65cm"
        self.__weight = 100
        self.__power_con = 120
        self.__memory = "128 GB"
        self.__processors = "i7 5th Gen"
        self.__base_price = 450000
        self.__videogames = []

    def add_videogame(self, Videogame: videogame_factory):
        self.__videogames.append(Videogame)

    def __str__(self):
        if self.__material == 1:
            self.__material = "Wood"
        elif self.__material == 2:
            self.__material = "Aluminium"
        elif self.__material == 3:
            self.__material = "Carbon Fiber"
        return f"Material: {self.__material}\nDimensions: {self.__dimensions}\nWeight: {self.__weight}\n\
            Power Consumption: {self.__power_con}\nMemory: {self.__memory}\nProccesor: {self.__processors}\n\
                Base Price: {self.__base_price}\nControls Price: {self.__controls_price}\n\
                    Weapons Design: {self.__weapons_design}"
    
    def get_baseprice(self) -> float:
        return self.__base_price
    
    def set_baseprice(self, price: float):
        self.__base_price = price

    def get_weight(self) -> float:
        return self.__weight
    
    def set_weight(self, weight: float):
        self.__weight = weight

    def get_power(self) -> float:
        return self.__power_con
    
    def set_power(self, power: float):
        self.__power_con = power

class RacingArcade(Arcade):
    """
    This class represents the behavior of a racing arcade machine.
    """
    def __init__(self, material:str, steering_wheel_design: str):
        self.__steering_wheel_design = steering_wheel_design
        self.__material = material
        self.__dimensions = "175cm x 70cm"
        self.__weight = 110
        self.__power_con = 120
        self.__memory = "32 GB"
        self.__processors = "i7 5th Gen"
        self.__base_price = 450000
        self.__videogames = []

    def add_videogame(self, Videogame: videogame_factory):
        self.__videogames.append(Videogame)

    def __str__(self):
        if self.__material == 1:
            self.__material = "Wood"
        elif self.__material == 2:
            self.__material = "Aluminium"
        elif self.__material == 3:
            self.__material = "Carbon Fiber"
        return f"Material: {self.__material}\nDimensions: {self.__dimensions}\nWeight: {self.__weight}\n\
            Power Consumption: {self.__power_con}\nMemory: {self.__memory}\nProccesor: {self.__processors}\n\
                Base Price: {self.__base_price}\nSteering Wheel Design: {self.__steering_wheel_design}"
    
    def get_baseprice(self) -> float:
        return self.__base_price
    
    def set_baseprice(self, price: float):
        self.__base_price = price

    def get_weight(self) -> float:
        return self.__weight
    
    def set_weight(self, weight: float):
        self.__weight = weight

    def get_power(self) -> float:
        return self.__power_con
    
    def set_power(self, power: float):
        self.__power_con = power

class ArcadeFactory:
    """
    This class work as a factory to create the arcades
    """
    
    @staticmethod
    def create_arcade(arcade_type: int, material: str) -> Arcade:
        """
        This static method allows to create a videogame depending on its type

        Args:
        vg_type(str): Type of the videogmae (HD or Standard)

        Returns:
        Videogame: A videogame that contains the data entered
        """

        if arcade_type == 1:
            vibration = input("Activate Vibration Yes(Y) or No(N)\n Enter your selection: : ").strip().upper()
            while vibration not in ["Y","N"]:
                print("Invalid input, please enter a valid option, Y or N")
                vibration = input("Activate Vibration Yes(Y) or No(N)\n Enter your selection: : ").strip().upper()
            sound = input("Activate Sound Alert? Yes(Y) or No(N)\n Enter your selection: ").strip().upper()
            while sound not in ["Y","N"]:
                print("Invalid input, please enter a valid option, Y or N")
                sound = input("Activate Sound Alert? Yes(Y) or No(N)\n Enter your selection: ").strip().upper()
            return ClassicalArcade(material, vibration, sound)
        elif arcade_type == 2:
            return DanceRevolution(material)
        elif arcade_type == 3:
            wpn = int(input("Select a Weapon Design 1) Halo Style 2) Realistic Style 3) Duck Hunt Style\n Enter your selection: "))
            while wpn not in [1,2,3]:
                print("Invalid input, please enter a valid option, 1,2 or 3")
                wpn = input("Select a Weapon Design 1) Halo Style 2) Realistic Style 3) Duck Hunt Style\n Enter your selection: ")
            return ShootingArcade(material, wpn)
        elif arcade_type == 4:
            wheel = int(input("Select a Steering Wheel Design 1) Regular Style 2) Nascar Style 3) F1 Style\n Enter your selection: "))
            while wheel not in [1,2,3]:
                print("Invalid input, please enter a valid option, 1,2 or 3")
                wheel = input("Select a Steering Wheel Design 1) Regular Style 2) Nascar Style 3) F1 Style\n Enter your selection: ")
            return RacingArcade(material, wheel)