import curses 
import random
import time 

def main(stdscr):
 
  sentences = [
    "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet.",
    "Typing regularly improves speed and accuracy. Consistent practice is key to mastering typing skills.",
    "A day without laughter is a day wasted. Laughter is the best medicine for a healthy life.",
    "Practice makes perfect, especially in typing. The more you type, the faster and more accurate you become.",
    "Typing fast is an advantage, but accuracy is key. It's important to balance speed with precision.",
    "Mastering typing can help you write documents efficiently. This skill is valuable in many professional fields.",
    "Typing skills are useful in many professions. From programming to journalism, good typing can boost productivity.",
    "Interactive tools can help you learn typing faster. Games and exercises make learning fun and engaging.",
    "Typing games can make learning fun and engaging. They provide a playful way to improve your skills.",
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
            writing = writing[:-1]
    else:
      if cp < len(sentence) :
          row, col = divmod(cp, width)
          if key == ord(sentence[cp]):
              stdscr.addstr(row + 1, col, chr(key), curses.color_pair(1))
              writing += chr(key)
              correct_letter += 1 
              
          else:
              stdscr.addstr(row + 1, col, chr(key), curses.color_pair(2))
              writing += chr(key)
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
