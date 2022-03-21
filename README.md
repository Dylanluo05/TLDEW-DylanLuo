## Data Structures Project:
### Jekyll: ###
[Jekyll](https://dylanluo05.github.io/TLDEW-DylanLuo/)

### Replit Embed: ###

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@Dylanluo05/Python-Menu-2?lite=true#src/menuy.py"></iframe>
  
### Week 0: ###
[Week 0 Plans, Team, Jobs Individual Review Ticket - Dylan Luo](https://github.com/Dylanluo05/TLDEW-DylanLuo/issues/1)
* Python Menu Challenge:
 1. Build your own menu and sub-menu
 2. Add swap and keypad from Tri 2 Week 10, to your project and menu.
 3. For additional challenge and review, build a Christmas tree with *s or a pattern of your choice

<img src="https://user-images.githubusercontent.com/88572244/156895395-6bbf72be-605f-4bca-a376-b9ee985b5786.png" width="150" height="240">

 4. Add two items below to get ready for animations and interacting with terminal codes 
 
* Key Learning Code Snippets:

```
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
```


### Week 1: ###
[Week 0 Plans, Team, Jobs Individual Review Ticket - Dylan Luo](https://github.com/Dylanluo05/TLDEW-DylanLuo/issues/1)
* Key Learning Code Snippets:

List and Loops:
```
# given an index this will print InfoDb content
def print_list(n):
    print("Anime Name:", InfoDb[n]["AnimeName"], "Date of First Episode:", InfoDb[n]["DateofFirstEpisode"], "Anime Studio(s):", InfoDb[n]["AnimeStudio(s)"] )  # using comma puts space between values
    print("\t", "Most Famous Anime Characters: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["MostFamousAnimeCharacters"]))  # join allows printing a string list with separator
    print()

def run():
    print("For Loop:")
    for_loop(0,1)
    print("While loop:")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop:")
    recursive_loop(0)  # requires initial index to start recursion

def for_loop(initial, final):
    for n in range(initial, final + 1):
      print_list(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_list(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_list(n)
        recursive_loop(n + 1)
    return # exit condition
```

Fibonacci:
```
# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

def Tester():
    num = int(input("Enter a number for fibonacci terms: "))
    A1, A2 = 0, 1
    count = 0
  
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num ==1:
        print("Fibonacci sequence upto",num,":")
        print(A1)
    else:
       print("Fibonacci sequence:")
    while count < num:
       print(A1)
       nth = A1 + A2
       A1 = A2
       A2 = nth
       count += 1
```

## Create Task Project: ##
* Intended Create Task Project:

   * The Hiking Trail Recommendation Feature is essentially a type of Personality Quiz. Users will take a quiz that asks them questions about their personalities and ideal hiking trails. At the end, the quiz result will recommend users hiking ideas that suit their personalities.
   * Ex: Choose your preferred weather, types of foods, hobby → Recommended place shows up with details(image).

## TPT Notes:
1. [TPT 5.1 and 5.2 Notes](https://github.com/Dylanluo05/TLDEW-DylanLuo/wiki/TPT-5.1-and-5.2-Notes) 
2. [TPT 5.3 and 5.4 Notes](https://github.com/Dylanluo05/TLDEW-DylanLuo/wiki/TPT-5.3-and-5.4-Notes) 
