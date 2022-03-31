# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "AnimeName": "Naruto Shippuden",  
               "DateofFirstEpisode": "February 15, 2007",  
               "AnimeStudio(s)": "Studio Pierrot",  
               "MostFamousAnimeCharacters":["Naruto Uzamaki","Sasuke Uchiha","Sakura Haruno","Kakashi Hatake", "Obito Uchiha", "Itachi Uchiha", "Madara Uchiha"]  
              })  

InfoDb.append({  
               "AnimeName": "Tokyo Revengers",  
               "DateofFirstEpisode": "April 11, 2021",  
               "AnimeStudio(s)": "Liden Films",  
               "MostFamousAnimeCharacters":["Sano Manjiro","Ken Ryuguji","Hanagaki Takemichi", "Hina Tachibana", "Keisuke Baji", "Kazutora Hanemiya", "Chifuyu Matsuno", "Izana Kurokawa"]  
              })  

InfoDb.append({  
               "AnimeName": "Attack On Titan",  
               "DateofFirstEpisode": "April 7, 2013",  
               "AnimeStudio(s)": "WIT Studio(Seasons 1-3) and MAPPA(Season 4)",  
               "MostFamousAnimeCharacters":["Eren Yeager","Mikasa Ackerman","Armin Arlert", "Levi Ackerman", "Boruto Hoover", "Erwin Smith"]  
              })  

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
