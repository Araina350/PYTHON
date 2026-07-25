def get_genre():
    print("Available genres",end=" ")
    for i,g in enumerate(genres,1):
        print(i,".",g)
        print()
        while True:
            x = input("Enter number or name").strip()
            if x.isdigit() and 1<= int(x) <= len(genres): return genres[int(x) - 1]
            x = x.title()
            if x in genres: return x
            print("Invalid input. Try Again ")
def get_rating():
    while True:
        x = input("Enter minimum rating(7.6 to 9.3) or 'Skip'").strip()
        if x.lower() == "skip":
            return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3:
                return r
            print("Rating is out of range")
        except ValueError:
            print("Invalid input")
print("Welcome to your Personal Movie Recommendation Assistant")
name = input("What's your name").strip()
print("Nice to meet you",name)
print("Let's find the perfect movie for you")
genres = get_genre()
mood = input("How do you feel today?").strip()
print("Analyzing mood...",end=" ",flush=True)
mp = Textblob(mood).sentiment.polarity
md = 'positive' if mp > 0 else 'negative' if mp < 0 else 'neutral'
print(f"Your mood is {md}(polarity: {mp:.2f})")
rating = get_rating
print("Finding movies for you",end=" ",flush=True)
recs = recommend(genres = genres,mood = mood,rating = rating,n=5)
print(recs + "\n") if isinstance(recs, str) else show(recs, name)
while True:
    a = input("Would you like more movie recomendations?Yes/No").strip().lower()
    if a == 'no':
        print("Enjoy your movies!!") 
        break
    elif a == 'yes':
        recs = recommend(genres = genres,mood = mood,rating = rating,n=5)
        print(recs + "\n") if isinstance(recs, str) else show(recs, name)
    else:
        print("Invalid input")    