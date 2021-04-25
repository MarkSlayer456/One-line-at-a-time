import curses
import sys
import re

args = sys.argv

stdscr = curses.initscr()

fileStr = ""

curses.noecho()
curses.cbreak()

#clear screen
stdscr.clear()

lines = []

if(len(args) == 2):
    file = open(args[1], "r")
    for i in file:
        fileStr += i
    lines = re.split('[.!?]', fileStr)
    j = 0
    while(j < len(lines)):
        if(lines[j][0] == "\n"):
            lines[j] = lines[j][1:len(lines[j])]
        j+=1
    if(len(lines) > 0):
        curr = 0
        stdscr.clear()
        stdscr.addstr(0, 0, lines[curr])
        
        while(True):
            c = stdscr.getch()
            if c == ord('p'):
                if(len(lines) != curr+1):
                    curr += 1
                    stdscr.clear()
                    stdscr.addstr(0, 0, lines[curr])
            elif c == ord('o'):
                if(curr > 0):
                    curr -= 1
                    stdscr.clear()
                    stdscr.addstr(0, 0, lines[curr])
                    
            else:
                break
    else:
        print("File is empty")
else:
    print("Usage: python3 main.py <file name>")



curses.endwin()
