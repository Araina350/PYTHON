print("Hi I am Sally your AI chatbot! What is your name?")
name = input()
print("Nice to meet you ",name)
print("How are you feeling today? Good,bad,can't decide")
feel = input()
if feel == "good":
    print("Yay! I am happy to hear that")
elif feel == 'bad':
    print("I am sorry to hear that hope you feel better. ")
else:
    print("That is ok sometimes you just feel indifferent")

print("Bye it was nice chatting with you")