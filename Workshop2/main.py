"""
This module has the main program

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

from arcade import ArcadeFactory
from videogame import videogame_factory
from user import Customer

class Main:
    """
    This class represents the behavior of the application
    """
    
    def valid_option(self, prompt: str, options: list):
        """
        This method validates that the user only be able to choose
        between the desired options without the program breaking
        """
        while True:
            try:
                op = int(input(prompt))
                if op in options:
                    return op
                else:
                    print("\nPlease, choose a valid option")
            except ValueError:
                print("\nPlease, enter a valid number")

    def add_videogame_to_machine(self):
        """
        This method allows the customer to add a videogame to the machine that he is buying
        """
        v_type = self.valid_option("Select a type of videogame 1) HD 2) Standard\n Enter your selection: ", [1,2])
        v_name = input("\n Enter the videogame name: ")
        v_story_creator = input("\n Enter the name of the story creator: ")
        v_graph_creator = input("\n Enter the name of the graphics creator: ")
        v_category = input("\n Enter the category where the game belongs: ")
        v_year = input("\n Enter the year when the game was released: ")

        return videogame_factory.create_vg(v_type, v_name, v_story_creator, v_graph_creator, v_category, v_year)
        

    def run(self) -> None:
        """
        This method runs the application
        """
        while True:
            print("""Select the type of arcade machine you want to buy:
            1) Classical Machine
            2) Dance Revolution Machine
            3) Shooting Machine
            4) Racing Machine
            5) Exit""")
            op = int(input("\nEnter an option: "))

            if op != 5:
                material = self.valid_option("Select a material 1) Wood 2) Aluminium 3) Carbon Fiber\n Enter your selection: ", [1,2,3])
                arcade = ArcadeFactory.create_arcade(op, material)
            else: 
                break

            vg = self.add_videogame_to_machine()
            print("""Do you want to add another game?:
            1) Add Another Game
            2) Continue the Purchase""")
            vgop = int(input("\nEnter an option: "))
            arcade.add_videogame(vg)

            while vgop == 1:
                self.add_videogame_to_machine()
                print("""Do you want to add another game?:
                1) Add Another Game
                2) Continue the Purchase""")
                vgop = int(input("\nEnter an option: "))

            if material == 1:
                price = arcade.get_baseprice()
                price = price - price * 0.05
                arcade.set_baseprice(price)
                weight = arcade.get_weight()
                weight = weight + weight * 0.1
                arcade.set_weight(weight)
                power = arcade.get_power()
                power = power + power * 0.15
                arcade.set_power(power)
            elif material == 2:
                price = arcade.get_baseprice()
                price = price + price * 0.1
                arcade.set_baseprice(price)
                weight = arcade.get_weight()
                weight = weight - weight * 0.05
                arcade.set_weight(weight)
            elif material == 3:
                price = arcade.get_baseprice()
                price = price + price * 0.2
                arcade.set_baseprice(price)
                weight = arcade.get_weight()
                weight = weight - weight * 0.15
                arcade.set_weight(weight)
                power = arcade.get_power()
                power = power - power * 0.10
                arcade.set_power(power)

            print("Enter your data to confirm the purchase: \n")
            Name = input("Enter your name: ")
            Email = input("\nEnter your email: ")
            Address = input("\nEnter your address: ")
            C = Customer(Name, Email, Address)
            print("--------------------- PURCHASE SUMMARY ---------------------\n")
            print(f"{arcade.__str__()}  \n {C.__str__()}")
     
if __name__ == "__main__":
    app = Main()
    app.run()
            