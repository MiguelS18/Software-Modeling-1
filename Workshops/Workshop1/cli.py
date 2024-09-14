"""
This module has the main software

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

from logic import Game
from logic import ArcadeMachine
from logic import Order
from logic import Admin
from logic import Customer

GM = Game()
AM = ArcadeMachine()
OD = Order()
AD = Admin()

if __name__ == "__main__":
    MENU = """
    1) Buy Arcade Machine
    2) See Orders History
    3) See Customers Info
    4) Exit\n
    """
    op = int(input(MENU))
    while op != 4:
        if op == 1:
            M = AM.material_valid()
            G = GM.option_valid()
            GameList = ["Super Mario", "Sonic", "Zelda", "Kirby", "Mortal Kombat"]
            while G != 3:
                if G == 1:
                    GM.see_games(GameList)
                elif G == 2:
                    GM.add_game(GameList)
                else:
                    print("\nPlease, choose a valid option")
                G = GM.option_valid()
            C = AM.color_valid()
            Cost = AM.arcade_cost(M, C, GameList)
            Name = input("\nPlease, enter your name: ")
            Address = input("\nPlease, enter your address: ")
            try:
                DocNumber = int(input("\nPlease, enter your document number: "))
            except ValueError:
                print("\nPlease, enter a valid number")
            print("\n")
            print(OD.gen_order(Name, Address, DocNumber, M, C, Cost, GameList))
            print("\n")
            Confirm = AD.purchase_valid()
            if Confirm == 1:
                AD.gen_purchase_log(Name, Cost)
                CM = Customer(Name, Address, DocNumber)
                CM.gen_customer_data(Name, Address, DocNumber)
                print("\n Thanks for your purchase " + Name + " \n")
            else:
                print("\n You've cancelled the purchase \n")
        elif op == 2:
            print("\n---- PURCHASE LOG ----\n")
            print(AD.get_purchase_log())
            print("----------------------\n")
        elif op == 3:
            print("\n---- CUSTOMERS DATA ----\n")
            print(CM.get_customer_data())
            print("------------------------\n")
        else:
            print("\nPlease, choose a valid option")

        op = int(input(MENU))
