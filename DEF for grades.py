

def marks(M, E, B):
        a = (M + E + B)
        print("Obtained marks are:", a)
        return a
    
def percentage(a, b):
        c = (a * 100) / b
        print("You got", c, "% marks")
        return c

def grade(c):
        if 80 <= c < 90:
            d=print("You Got Grade of A+")
        elif 70 <= c < 80:
            d=print("You Got Grade of B")
        elif 60 <= c < 70:
            d=print("You Got Grade of C")
        elif c < 60:
            d=print("You are FAIL")
        elif c >= 90:
            d=print("You Got Grade of A++")
        return d

def main(M,E,D,b):
    Total_Marks=marks(M,E,D)
    Percentage=percentage(Total_Marks,b)
    GRADE=grade(Percentage)

main(70,60,90,300)
 
