 # Task 9 Cat problem
# You've collected too many cats. Write a program to count how
# many cats you have by reading in their names. All your cats only
# have first names, with no spaces.

def main():
    #Write your code here
    var = input('Cats: ')
    var2 = len(var.split())
    print(f'You have {var2} cats.')



    # End of your code here





if __name__ == '__main__':
    main()