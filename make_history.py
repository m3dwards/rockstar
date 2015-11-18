import os
from datetime import date, timedelta

def convert_to_github_day(day):
    return day + 1 if day < 6 else 0

def dark_block(x, y):
    blocks = []
    # R
    blocks.append((3, 2))
    blocks.append((3, 3))
    blocks.append((3, 4))
    blocks.append((3, 5))
    blocks.append((3, 6))
    blocks.append((4, 1))
    blocks.append((5, 1))
    blocks.append((6, 2))
    blocks.append((6, 3))
    blocks.append((5, 4))
    blocks.append((4, 4))
    blocks.append((6, 5))
    blocks.append((7, 6))

    #O
    blocks.append((9, 4))
    blocks.append((10, 3))
    blocks.append((10, 5))
    blocks.append((11, 2))
    blocks.append((11, 6))
    blocks.append((12, 3))
    blocks.append((12, 5))
    blocks.append((13, 4))

    #C
    blocks.append((15, 2))
    blocks.append((15, 3))
    blocks.append((15, 4))
    blocks.append((15, 5))
    blocks.append((16, 1))
    blocks.append((17, 1))
    blocks.append((18, 1))
    blocks.append((16, 6))
    blocks.append((17, 6))
    blocks.append((18, 6))

    #K
    blocks.append((20, 1))
    blocks.append((20, 2))
    blocks.append((20, 3))
    blocks.append((20, 4))
    blocks.append((20, 5))
    blocks.append((20, 6))
    blocks.append((21, 4))
    blocks.append((22, 3))
    blocks.append((22, 5))
    blocks.append((23, 2))
    blocks.append((23, 6))

    #S
    blocks.append((25, 1))
    blocks.append((25, 2))
    blocks.append((25, 3))
    blocks.append((25, 6))
    blocks.append((26, 1))
    blocks.append((26, 3))
    blocks.append((26, 6))
    blocks.append((27, 1))
    blocks.append((27, 3))
    blocks.append((27, 6))
    blocks.append((28, 1))
    blocks.append((28, 4))
    blocks.append((28, 5))
    blocks.append((28, 6))

    #T
    blocks.append((30, 1))
    blocks.append((31, 1))
    blocks.append((32, 1))
    blocks.append((33, 1))
    blocks.append((34, 1))
    blocks.append((32, 2))
    blocks.append((32, 3))
    blocks.append((32, 4))
    blocks.append((32, 5))
    blocks.append((32, 6))

    #A
    blocks.append((36, 3))
    blocks.append((36, 4))
    blocks.append((36, 5))
    blocks.append((36, 6))
    blocks.append((36, 6))
    blocks.append((37, 2))
    blocks.append((38, 1))
    blocks.append((39, 2))
    blocks.append((40, 3))
    blocks.append((40, 4))
    blocks.append((40, 5))
    blocks.append((40, 6))
    blocks.append((37, 4))
    blocks.append((38, 4))
    blocks.append((39, 4))
   
   #R
    blocks.append((42, 2))
    blocks.append((42, 3))
    blocks.append((42, 4))
    blocks.append((42, 5))
    blocks.append((42, 6))
    blocks.append((43, 1))
    blocks.append((44, 1))
    blocks.append((45, 2))
    blocks.append((45, 3))
    blocks.append((44, 4))
    blocks.append((43, 4))
    blocks.append((45, 5))
    blocks.append((46, 6))

    return (x,y) in blocks

def main():
    first_day = convert_to_github_day((date.today() - timedelta(days=364)).weekday())

    for i in range(365, -1, -1):
        day = date.today() - timedelta(days=i)
        y = convert_to_github_day(day.weekday())
        x = (first_day + abs(364-i)) / 7
        commits = 1;
        day_str = day.strftime("%a %b %d 12:12:12 %Y -0100")
        if dark_block(x, y):
            commits = 75
        for n in range(0, commits): 
            command = "GIT_AUTHOR_DATE='{0}' GIT_COMMITTER_DATE='{0}' git commit --allow-empty -m 'rockstar'".format(day_str)
            os.system(command)

    print "Done"
        
    

    # grid is 53 * 7 with top row being day 6 Sunday and bottom row being Saturday (day 5)

    #>>> d.strftime("%d/%m/%y")
    #'11/03/02'
    #>>> d.strftime("%A %d. %B %Y")
    #'Monday 11. March 2002'
    #>>> 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
    #'The day is 11, the month is March.'

    #datetime.datetime.today().weekday()
    #4
    #Return the day of the week as an integer, where Monday is 0 and Sunday is 6.

    #GIT_AUTHOR_DATE='your date' GIT_COMMITTER_DATE='your date' git commit -m 'new (old) files'
    #GIT_AUTHOR_DATE='Fri Jul 26 19:32:10 2013 -0400' GIT_COMMITTER_DATE='Fri Jul 26 19:32:10 2013 -0400' git commit

if __name__ == "__main__":
    main()
