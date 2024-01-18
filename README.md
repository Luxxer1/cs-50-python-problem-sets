# CS50 Python Problem Sets Repository

This repository contains my solutions to the problem sets from the CS50 Introduction to Computer Science course, specifically the Python track. The course is offered by Harvard University and covers fundamental concepts in computer science and programming.

## Problem Sets

### Week 0 - Functions, Variables
1. **Indoor Voice:**
   - Description: Transform user input to lower case. 
   - Directory: `indoor`
   - File: `indoor.py`

2. **Playback Speed:**
   - Description: Modify speech pacing by replacing spaces with three periods.
   - Directory: `playback`
   - File: `playback.py`

3. **Making Faces:**
   - Description: Transform :) to 🙂 and :( to 🙁.
   - Directory: `faces`
   - File: `faces.py`

4. **Einstein:**
   - Description: Calculate the equivalent energy (in Joules) based on user-inputted mass (in kilograms) using Einstein's famous formula, E=mc^2.
   - Directory: `einstein`
   - File: `einstein.py`

5. **Tip Calculator:**
   - Description: Calculate the tip amount based on user-inputted meal cost and tip percentage. 
   - Directory: `tip`
   - File: `tip.py`

### Week 1 - Conditionals
1. **Deep Thought:**
   - Description: Determine if the user's input holds the answer to the Great Question of Life, the Universe, and Everything. Output "Yes" for input 42, "Forty Two," or "forty-two," and "No" otherwise. 
   - Directory: `deep`
   - File: `deep.py`

2. **Home Federal Savings Bank:**
   - Description: Determine the reward based on the user's greeting at the Home Federal Savings Bank. Output $0 for "hello," $20 for a greeting starting with "h," and $100 otherwise.
   - Directory: `bank`
   - File: `bank.py`

3. **File Extensions:**
   - Description: Identify the media type of a file based on its name's suffix. Output the corresponding media type for common file extensions or application/octet-stream to default.
   - Directory: `extensions`
   - File: `extensions.py`

4. **Math Interpreter:**
   - Description: Perform basic arithmetic operations on integer inputs, supporting addition, subtraction, multiplication, and division. Display the result formatted to one decimal place.
   - Directory: `interpreter`
   - File: `interpreter.py`

5. **Meal Time:**
   - Description: Detect whether it's time for breakfast, lunch, or dinner based on user-inputted time in 24-hour format.
   - Directory: `meal`
   - File: `meal.py`

### Week 2 - Loops
1. **camelCase:**
   - Description: Convert a variable name from camel case to snake case.
   - Directory: `camel
   - File: `camel.py`

2. **Coke Machine:**
   - Description: Simulate a Coke machine that accepts specific coin denominations, calculates the amount due, and returns change once the user has inserted at least 50 cents.
   - Directory: `coke`
   - File: `coke.py`

3. **Just setting up my twttr:**
   - Description: Remove vowels from a given text, considering both uppercase and lowercase letters, in a program inspired by Twitter's character limit practices. 
   - Directory: `twttr`
   - File: `twttr.py`

4. **Vanity Plates:**
   - Description: Check if a given license plate follows Massachusetts vanity plate requirements, such as starting with at least two letters, having a maximum of 6 characters, and satisfying other specific conditions.
   - Directory: `plates`
   - File: `plates.py`

5. **Nutrition Facts:**
   - Description: Implement a program that, based on the user's input of a fruit, outputs the number of calories in one portion of that fruit according to the FDA's nutrition poster.
   - Directory: `nutrition`
   - File: `nutrition.py`

### Week 3 - Exceptions
1. **Fuel Gauge:**
   - Description: Calculate the fuel percentage in a tank based on a provided fraction, rounding to the nearest integer. Output "E" if the tank is virtually empty (1% or less) or "F" if it's virtually full (99% or more). Handle cases like non-integer inputs, division by zero, or improper fraction formats by prompting the user again.
   - Directory: `fuel
   - File: `fuel.py`

2. **Felipe’s Taqueria:**
   - Description: Place an order at Felipe's Taqueria by inputting menu items, displaying the total cost after each entry. The program continues until the user inputs control-d. Ignore non-menu inputs and treat input case insensitively.
   - Directory: `taqueria`
   - File: `taqueria.py`

3. **Grocery List:**
   - Description: Generate a sorted and formatted grocery list by inputting items one per line. The program displays each item in uppercase, sorted alphabetically, and prefixed with the count of occurrences.
   - Directory: `grocery`
   - File: `grocery.py`

4. **Outdated:**
   - Description: Convert a date given in month-day-year order to the international standard YYYY-MM-DD format, accounting for variations in input like "9/8/1636" or "September 8, 1636." If the user inputs an invalid date, prompt for input again.
   - Directory: `outdated`
   - File: `outdated.py`

### Week 4 - Libraries
1. **Emojize:**
   - Description: Transforms english text into emoji symbols by converting emoji codes or aliases to their corresponding emojis.
   - Directory: `emojize
   - File: `emojize.py`

2. **Frank, Ian and Glen’s Letters:**
   - Description: Operates with either zero or two command-line arguments, allowing users to output text in a random font or a specified font using pyfiglet. Prompts the user for input text and displays it in the chosen font. Handles error conditions for invalid command-line arguments.
   - Directory: `figlet`
   - File: `figlet.py`

3. **Adieu, Adieu:**
   - Description: Prompts the user for names until control-d is input. Bids farewell to the entered names, formatting the adieu messages with correct grammar, separating names with commas and "and" appropriately.
   - Directory: `adieu`
   - File: `adieu.py`

4. **Guessing Game:**
   - Description: Prompts the user for a level and generates a random integer between 1 and the specified level (inclusive). Asks the user to guess the generated integer, providing feedback for each guess until the correct number is guessed.
   - Directory: `game`
   - File: `game.py`

5. **Little Professor:**
   - Description: Prompts the user to select a difficulty level (1, 2, or 3), generates ten addition problems with non-negative integers, prompts the user to solve each problem, provides feedback, and outputs the user's score based on correct answers out of 10.
   - Directory: `professor`
   - File: `professor.py`
  
6. **Bitcoin Price Index:**
   - Description: Takes a specified command-line argument representing the number of Bitcoins to buy, queries the CoinDesk API for the current Bitcoin Price Index, and outputs the total cost in USD to four decimal places, while handling potential input errors and exceptions.
   - Directory: `bitcoin`
   - File: `bitcoin.py`


## How to Use
- Each problem set is contained in its respective file.
- To run a specific problem set, execute the corresponding Python file using a Python interpreter.

Feel free to explore the solutions and use them as a reference. If you have any questions or suggestions, feel free to open an issue or reach out to me.

Happy coding! 🚀
