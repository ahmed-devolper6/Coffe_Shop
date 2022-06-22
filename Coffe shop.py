class Cofe_Shop:
    
    def __init__(slef):
        print("Weclome in our coffe shop")
        while True:        
            visit = input("Enter y to see the menu and x to Exit: ")
            try:
                visit = str(visit)
                if visit == "y":
                    slef.Menu()
                elif visit == "x":
                    break
                else:
                    print("plese Enter y or x ")
            except:
                print("Sir plese Enter i Y or N or X")
                continue
    def Menu(slef):
        Menus = {"Coffe:price":70 , "Teaa:prise":85 , "ice Coffe:price":100}
        print(f"The menu {Menus}")
        while True:
            Cohise = input("Enter ur choise or X to exit form the menu: ")
            try:
                Cohise = str(Cohise)
                if Cohise == 'coffe':
                    print("The price is 70")
                    Ask_for_buy = input("Enter Y to buy or no for aother choise: ")
                    if Ask_for_buy == "y":
                        print("Go to the windo...")
                        slef.User_Choise()
                    elif Ask_for_buy == "n":
                        continue
                elif Cohise == 'tea':
                    print("The price is 85")
                    Ask_for_buy = input("Enter Y to buy or no for aother choise: ")
                    if Ask_for_buy == "y":
                        print("Go to the windo...")
                        slef.User_Choise()
                    elif Ask_for_buy == "n":
                        continue
                elif Cohise == 'ice coffe':
                    print("The price is 100")
                    Ask_for_buy = input("Enter Y to buy or no for aother choise: ")
                    if Ask_for_buy == "y":
                        print("Go to the windo...")
                        slef.User_Choise()
                    elif Ask_for_buy == "n":
                        continue
                elif Cohise == 'x':
                    break
                else:
                    print("Sir choise form menu")
            except ValueError:
                print("i can understad what u want")
                continue
    def User_Choise(slef):
        cusmter_name = input("Enter ur name for the oders: ")
        while True:
            Oder = input("Type your oders to confrim: ")
            try:
                Oder = str(Oder) 
                if Oder == 'coffe':
                    print(f"your name is {cusmter_name}, and take the {Oder}")
                    print('Tank for Visit us....')
                    break
                elif Oder == 'ice coffe':
                    print(f"your name is {cusmter_name}, and take the {Oder}")
                    print('Tank for Visit us....')
                    break
                elif Oder == 'tea':
                    print(f"your name is {cusmter_name}, and take the {Oder}")
                    print('Tank for Visit us....')
                    break
                else:
                    print("we dont have this oder")
            except:
                print("sir dont give me i number")

 

Buy = Cofe_Shop()
