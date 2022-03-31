import Src.Week0.swap as swap
import Src.Week0.christmastree as christmastree
import Src.Week0.keypad as keypad
import Src.Week0.badboat as badboat
import Src.Week0.goodboat as goodboat
import Src.Week1.listsandloops as listsandloops
import Src.Week1.Fibonacci as Fibonacci
import Src.Week2.factorialclass as factorialclass
import Src.Week2.mathfunction as mathfunction
import Src.Week2.palindrome as palindrome

Main_menu = [
]

Week0_menu = [
    ["Swap", swap.run],
    ["Keypad", keypad.run],
    ["Christmas Tree", christmastree.options],
    ["1st Boat", badboat.run],
    ["2nd Boat", goodboat.ship]
]

Week1_menu = [
    ["Anime lists and loops", listsandloops.run],
    ["Fibonacci", Fibonacci.Tester]
]

Week2_menu = [
    ["Factorial Class", factorialclass.solve],
    ["Math Function", mathfunction.prime],
    ["Palindrome", palindrome.driver]
]


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def buildMenu(banner, options):
    print(dylan)
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")
    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid Choice: {choice}")
    buildMenu(banner, options)


def Week0_variable():
    title = "Week 0 Menu" + banner
    buildMenu(title, Week0_menu)


def Week1_variable():
    title = "Week 1 Menu" + banner
    buildMenu(title, Week1_menu)

def Week2_variable():
    title = "Week 2 Menu" + banner
    buildMenu(title, Week2_menu)

def menu():
    title = "Function Menu" + banner
    menu_list = Main_menu.copy()
    menu_list.append(["Week 0", Week0_variable])
    menu_list.append(["Week 1", Week1_variable])
    menu_list.append(["Week 2", Week2_variable])
    buildMenu(title, menu_list)

if __name__ == "__main__":
    menu()
