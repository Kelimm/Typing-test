import curses 
import random
import time 

def main(stdscr):
 
  sentences = [
    
    "Good typing skills can boost your productivity. They allow you to complete tasks quickly and accurately."
]


  
  # Initialize colors
  curses.start_color()
  curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
  
  # Display welcome message
  stdscr.addstr(0, 0, 'Welcome to the WPM test!')
  stdscr.addstr(1, 0, 'Press any key to continue...')
  stdscr.refresh()
  stdscr.getkey()
  
  # Select a random sentence
  sentence = random.choice(sentences)
  
  # Clear the screen and display the sentence to type
  stdscr.clear()
  stdscr.addstr(0, 0, 'Type this sentence as fast as you can:')
  stdscr.addstr(1, 0, sentence)
  stdscr.refresh()
  
  # Initialize variables for typing test
  writing = ""
  cp = 0 
  correct_letter = 0
  wpm = 0
  start = time.time()
  height, width = stdscr.getmaxyx()
  check = False
  
  # Main loop to capture user input and display results
  while not check:
    key = stdscr.getch()
    
    if key in (8, 127): # Backspace
        if cp > 0:
            cp -= 1
            row, col = divmod(cp,width)
            stdscr.addstr(row + 1 , col, sentence[cp]) # Correct the character
            stdscr.move(row + 1, col)
    else:
      if cp < len(sentence) :
          row, col = divmod(cp, width)
          if key == ord(sentence[cp]):
              stdscr.addstr(row + 1, col, chr(key), curses.color_pair(1))
              writing += chr(key)
              correct_letter += 1 
              
          else:
              stdscr.addstr(row + 1, col, chr(key), curses.color_pair(2))
          cp += 1
      
    # Calculate WPM
    end = time.time()
    elapsed_time = end - start
    wpm = (correct_letter / 5) / (elapsed_time / 60)
    stdscr.addstr(3, 0, f'WPM : {wpm:.2f}')
    stdscr.refresh()
    
    if writing == sentence:
      check = True
    
  # Display final result
  stdscr.clear()
  stdscr.addstr(0,0 , f'You typed the sentence in {elapsed_time:.2f} seconds.')
  stdscr.addstr(1,0 , f'WPM : {wpm:.2f}')
  stdscr.addstr(2, 0, 'Press any key to exit...')
  stdscr.refresh()

  # Wait for a key press to exit
  stdscr.nodelay(False)
  stdscr.getkey()
  
curses.wrapper(main)