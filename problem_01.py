def main():
    while True:
        user=input("Press Averege for A or Square for S or q for quit! ")
        if user=="q":
            print("Thanks for using!")
            break
        if user=="A":
            num1=int(input("Enter a number:"))
            num2=int(input("Enter a number:"))
            Averege=num1/num2
            print(f"The averege of given number is:{Averege}")
        if user=="S":
             num1=int(input("Enter a number:"))
             num2=int(input("Enter a number:"))
             square=num1*num2
             print(f"The square of given number is:{square}")
        else:
            print("Invalid input")
if __name__=="__main__":
    main()


