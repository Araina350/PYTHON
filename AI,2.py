import colorama
from colorama import Fore,Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.CYAN}🐍Welcome to Sentiment Spy ")
user_name = input(f"{Fore.MAGENTA} Please enter your Superhero name{Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent"
conversation_history = []
print(f"\nHello Agent{user_name}!")
print("Type a sentence and I will analyse how you feel using Textblob")
print(f"Type{Fore.YELLOW}exit{Fore.WHITE} to quit,{Fore.YELLOW}reset{Fore.WHITE}to start the conversation again and{Fore.YELLOW}history{Fore.WHITE}to see previous conversation")    
while True:
    user_input = input(">>").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter valid text")
        continue
    if user_input.lower() == "exit":
        print("exiting")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print("All Conversation History cleared")    
    elif user_input.lower() == "history":
        if not conversation_history:
            print("No Conversation History ") 
    else:
        print("Conversation history:")
        for idx,(text,polarity,sentiment_type)in enumerate(conversation_history,start=1):
            if sentiment_type == "Positive":
                color = Fore.GREEN
                emoji = "☺️"    
            elif sentiment_type == "Negative":
                color = Fore.RED
                emoji = "😢"
            else:
                color = Fore.YELLOW
                emoji = "😑🙁"
            print(f"{idx}. {color}{emoji} {text} "
                f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
    continue    
