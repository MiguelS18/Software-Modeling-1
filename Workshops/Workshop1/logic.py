"""
This module has the classes that contains the logic of the software

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

from datetime import datetime

class Validate:
    """
    CLASS
    """
    def valid_option(self, prompt: str, options: list):
        """
        This method validates that the user only be able to choose
        between options without the program breaking
        """
        while True:
            try:
                op = int(
                    input(
                        prompt
                    )
                )
                if op in options:
                    return op
                else:
                    print("\nPlease, choose a valid option")
            except ValueError:
                print("\nPlease, enter a valid number")

class ArcadeMachine(Validate):
    """
    This class contains the logic that calculate the cost of the arcade machine,
    and the validators for some options
    """

    def arcade_cost(self, m: int, c: int, gml: list) -> int:
        """
        This method calculates the total cost of the arcade machine taking into account
        the cuantity of games in it, the materials and the colors choosen

        Args:
            m(int) = Number that represents a type of material
            c(int) = Number that represents a color of joysticks

        Returns:
            An integer value with the total cost of the arcade
        """
        cost = 450000
        if m == 1:
            cost += 50000
        elif m == 2:
            cost += 100000
        elif m == 3:
            cost += 200000
        else:
            cost += 0

        if c == 1:
            cost += 5000
        elif c == 2:
            cost += 10000
        elif c == 3:
            cost += 12000
        else:
            cost += 0

        g = len(gml)

        cost = cost + (g * 3000)
        return cost

    def material_valid(self):
        """
        This method validates that the user only be able to choose
        between 1,2 or 3 without the program breaking when
        selecting the material of the arcade
        """
        return self.valid_option("\nChoose the material of the arcade"+
                                 " 1) Wood, 2) Aluminium, 3) Carbon Fiber: ", [1,2,3])

    def color_valid(self):
        """
        This method validates that the user only be able to choose
        between 1,2 or 3 without the program breaking when
        selecting the color of the joysticks of the arcade
        """
        return self.valid_option("\nChoose a color for the joystick"+
                                 " 1) Yellow, 2) Red, 3) Blue: ", [1,2,3])


class Game(Validate):
    """
    This class contains the logic that allow the customer to see the game list,
    add games to it and validates an option
    """

    def see_games(self, gml: list):
        """
        This method allow the customer to see the list of games in the arcade
        """
        for game in gml:
            print("\n" + game)

    def add_game(self, gml: list):
        """
        This method allow the customer to add a new game to the list of games
        in the arcade
        """
        game = input("Enter the name of the game you want to add: ")
        gml.append(game)

    def option_valid(self):
        """
        This method validates that the user only be able to choose
        between 1,2 or 3 without the program breaking when
        selecting the option to see the game list, add a game or
        continue with the process
        """
        return self.valid_option("\nChoose an option 1) See game list, 2) Add a game to the list," 
                                 + "3) Continue Buying Process: ", [1,2,3])


class Order:
    """
    This class contains the logic that allow the program to generate the order
    with the data entered by the customer
    """
    def gen_order(
        self,
        name: str,
        address: str,
        doc_num: int,
        material: int,
        color: int,
        cost: int,
        gml: list,
    ):
        """
        This method generates the order taking into account the options 
        choosen by the customer and their data
        """
        if material == 1:
            m = "Wood"
        elif material == 2:
            m = "Aluminium"
        elif material == 3:
            m = "Carbon Fiber"
        else:
            m = ""

        if color == 1:
            c = "Yellow"
        elif color == 2:
            c = "Red"
        elif color == 3:
            c = "Blue"
        else:
            c = ""

        order = (
            """
        ----- Summary of the order -----
        Buyer's name: """
            + name
            + """
        Buyer's address: """
            + address
            + """
        Buyer's document number: """
            + str(doc_num)
            + """
        Material of the Arcade Machine: """
            + m
            + """
        Color of the Arcade Machine: """
            + c
            + """
        Games in the Arcade Machine: """
            + str(gml)
            + """
        Total Cost of the Arcade Machine: $"""
            + str(cost)
            + ""
        )

        return order


class Admin(Validate):
    """
    This class has the logic that has to do with the admin like, 
    generate and get the purchase log and valid an option
    """
    def purchase_valid(self):
        """
        This method validates that the customer only choose between 
        1 or 2 without the program breaking at the time to confirm
        the purchase
        """
        return self.valid_option("Do you confirm the purchase? 1) Yes 2) No: ", [1,2,3])

    def gen_purchase_log(self, name: str, cost: int):
        """
        This method generates a purchase txt file with the name of the 
        buyer and the total cost of the arcade machine
        """
        with open("Workshop1/Log.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{datetime.now()} Buyer's Name: "
                + name
                + ", Cost of the Arcade Machine: $"
                + str(cost)
                + "\n"
            )

    def get_purchase_log(self):
        """
        This method allows to print the content on the purchase log 
        to see it in the execution of the program
        """
        with open("Workshop1/Log.txt", "r", encoding="utf-8") as f:
            content = f.read()
            return content


class Customer:
    """
    This class contains the data of the customers who make a purchase
    """

    def __init__(self, name: str, address: str, doc_num: int) -> None:
        self.name = name
        self.address = address
        self.doc_num = doc_num

    def gen_customer_data(self, name: str, address: str, doc_num: int):
        """
        This method generates a txt file with the customers name, address 
        and number of document
        """
        with open("Workshop1/Customers.txt", "a", encoding="utf-8") as f:
            f.write(
                "- Name: "
                + name
                + ", Address: "
                + address
                + ", Number of Document: "
                + str(doc_num)
                + "\n"
            )

    def get_customer_data(self):
        """
        This method allows to print the content on the customers data log
        to see it in the execution of the program
        """
        with open("Workshop1/Customers.txt", "r", encoding="utf-8") as f:
            content = f.read()
            return content
