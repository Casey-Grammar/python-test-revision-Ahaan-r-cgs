# Task 5 FIFA World Cup
# With 9 FIFA World Cup wins between them, Brazil and Italy two of
# the most successful soccer countries in the world. Write a program
# that works out who won their latest soccer match, given the scores
# of both teams.

def main():
    #Write your code here
    var = input('Italy: ')
    var1 = input('Brazil: ')
    if var > var1:
        print('Italy won the match.')
    elif var < var1:
        print('Brazil own the match.')
    else:
        print('The match was a draw.')
    # End of your code here





if __name__ == '__main__':
    main()