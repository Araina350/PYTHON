import colorama
from colorama import Fore,init
import re,random
init(autoreset=True)
destinations = {
    "beaches":["Indonesia", "Thailand", "Malaysia", "Vietnam", "Lakshwadeep","Andaman"],
    "mountains":["Himalayas", "Swiss Alps", "Andes", "Rocky Mountains",],
    "cities":["London", "Dubai", "Singapore", "Mumbai", "Paris","Tokyo","Rome","Madrid"]
}
jokes = [
    "What's worse than raining cats and dogs? Hailing taxis!"
    "Me: 'I'd love to travel more.' The bank account: 'Like, to the park?'"
    "Where do LEGO people go on holiday? The Czech RepuBRICK!"
]
def normalize_input(text):
    return re.sub(r"\s+"," ",text.strip().lower())
def recommend():
    print("Beaches, mountains or cities?")
    preference = input("You")
    preference = normalize_input(preference)
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(f"How about {suggestion}?")
        print("Did you like it? Yes/no")
        answer = input("You:").lower
def show_help():
    print((Fore.MAGENTA),"I can:")
    print((Fore.GREEN),"Suggest a travel spot say 'recommend'")
    print((Fore.GREEN),"Tell a joke, say 'joke'")
    print((Fore.GREEN),"Give packing say 'pack'")
    print((Fore.GREEN),"Type exit to end")
def chat():
    print(Fore.CYAN + "Hello I'm TravelBot")
    name = input(Fore.LIGHTYELLOW_EX + "Your name?")
    print(Fore.GREEN + f"Nice to meet you {name}!")
    show_help()
    while True:
        user_input = input(Fore.YELLOW + f"{name}:")
        user_input = normalize_input(user_input)
        if "recommend" in user_input:
            recommend()
        elif "pack" in user_input:
            packing_tips()
        elif "joke" in user_input:
            tell_joke()
        elif "bye" in user_input:
            print("Have a safe journey!Goodbye")
            break
        else:
            print(Fore.RED + "Could you please rephrase that")
if __name__ == "__main__":
    chat()