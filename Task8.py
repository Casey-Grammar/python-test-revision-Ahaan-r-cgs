# Task 8 Call signs
# A portmanteau is a word made by combining parts of two other
# words. This could be used to create call signs for an online
# group.

#For example, david and jones would make daones.

#Let's make some call signs!

#Write a program that asks a user for their first name and last
#name and then takes the first two letters of the first name and
#the last four letters of the last name and combines them to make
#a new call sign. (N.B. we won't test your program with any input
#that's too short!)

def main():
    #Write your code here
    var = input('First and Last Name? ')
    var1 = var.split()[0]
    var2 = var.split()[1]
    var3 = var1[:2] + var2[-4:]
    print("Your call sign is: " + var3)


    # End of your code here





if __name__ == '__main__':
    main()