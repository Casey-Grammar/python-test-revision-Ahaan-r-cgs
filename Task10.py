# Task 10 Class roll
# Write a program that takes a list of student names and sorts them
# to create a class roll. The list of names will be given on a one line
# separated by a single space.

#The student names could be entered with any combination of capitals or not.
#If they are entered with no capital first letter the list should not append.
#If they are entered with a capital first letter the list should append
#If they are entered with a mix of capitals the name should be converted to capital first letter and
#then added to the list.

def main():
    #Write your code here
    var = input('Sutdents: ').title()
    var1 = var.split()
    print('Class Roll')
    for i in var1:
        print(i)
    
    


    # End of your code here





if __name__ == '__main__':
    main()