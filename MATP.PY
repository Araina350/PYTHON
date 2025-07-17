import matplotlib.pyplot as plt
sn = ["Sanjay","Priya","Ajay","Purvi"]
sm = [60,80,70,79]
mark_perc = []
for x in sm:
    res = (x/80)*100
    mark_perc.append(res)
print(mark_perc)
def line_chart():
    plt.plot(sn,sm)
    plt.title("RESULT TIME!")
    plt.xlabel("STUDENT NAMES")
    plt.ylabel("STUDENT MARKS")
    plt.show()
line_chart()
def bar_chart():
    plt.bar(sn,sm)
    plt.title("RESULT TIME!")
    plt.xlabel("STUDENT NAMES")
    plt.ylabel("STUDENT MARKS")
    plt.show()
bar_chart()