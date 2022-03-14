## Data Structures Project:
### Jekyll: ###
[Jekyll](https://dylanluo05.github.io/TLDEW-DylanLuo/)
### Replit Link: ###
[Replit Python Menu](https://replit.com/@Dylanluo05/Python-Menu#main.py)
### Week 0: ###
[Week 0 Plans, Team, Jobs Review Ticket - Dylan Luo](https://github.com/Dylanluo05/TLDEW-DylanLuo/issues/1)
* Python Menu Challenge:
 1. Build your own menu and sub-menu
 2. Add swap and keypad from Tri 2 Week 10, to your project and menu.
 3. For additional challenge and review, build a Christmas tree with *s or a pattern of your choice

<img src="https://user-images.githubusercontent.com/88572244/156895395-6bbf72be-605f-4bca-a376-b9ee985b5786.png" width="150" height="240">

 4. Add two items below to get ready for animations and interacting with terminal codes 
 
* Key Learning Code Snippets:

import swap
import christmastree
import keypad
import badboat
import goodboat


main_menu = [
    ["Swap", swap.run],
    ["Keypad", keypad.run],
]

drawingsub_menu = [
    ["Christmas Tree", christmastree.options]
]

animationsub_menu = [
    ["Bad Boat", badboat.run],
    ["Good Boat", goodboat.ship]
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def buildMenu(banner, options):
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



## Create Task Project: ##
* Intended Create Task Project:

   * The Hiking Trail Recommendation Feature is essentially a type of Personality Quiz. Users will take a quiz that asks them questions about their personalities and ideal hiking trails. At the end, the quiz result will recommend users hiking ideas that suit their personalities.
     * Ex: Choose your preferred weather, types of foods, hobby → Recommended place shows up with details(image).

## TPT Notes:
[TPT 5.1 and 5.2 Notes](https://github.com/Dylanluo05/TLDEW-DylanLuo/wiki/TPT-5.1-and-5.2-Notes)
