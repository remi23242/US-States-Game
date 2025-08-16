# U.S. States Game

A Python game built with Turtle graphics and Pandas, where players guess U.S. state names, and correct guesses are displayed on a blank U.S. map at their respective coordinates. The game tracks guessed states and saves unguessed states to a CSV file when the player exits.

## Table of Contents
- [Features](#features)
- [Files](#files)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Gameplay](#gameplay)
- [Future Improvements](#future-improvements)
- [License](#license)

## Features

- **Interactive Guessing**: Players input state names via a text prompt, and correct guesses appear on the map.
- **Map Display**: Uses a blank U.S. map (`blank_states_img.gif`) as the background.
- **Coordinate Mapping**: State names are placed at coordinates specified in `50_states.csv`.
- **Exit and Save**: Players can exit by typing "Exit," saving unguessed states to `states_to_learn.csv`.
- **Progress Tracking**: Displays the number of correctly guessed states out of 50.

## Files

- `main.py`: Main game script, handling user input, map display, and state placement.
- `day25/50_states.csv`: CSV file with state names and their x, y coordinates on the map.
- `day25/blank_states_img.gif`: Blank U.S. map image used as the game background.
- `states_to_learn.csv`: (Generated) CSV file listing states not guessed when the player exits.

## Requirements

- Python 3.x
- Turtle module (included in standard Python library)
- Pandas library (`pip install pandas`)
- A blank U.S. map image (`blank_states_img.gif`) in the `day25` directory

## How to Run

1. Ensure Python and Pandas are installed:
   ```bash
   pip install pandas
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/remi23242/US-States-Game.git
   ```
3. Navigate to the project directory:
   ```bash
   cd US-States-Game
   ```
4. Ensure `blank_states_img.gif` is in the `day25` subdirectory.
5. Run the game:
   ```bash
   python main.py
   ```

## Gameplay

- The game displays a blank U.S. map using `blank_states_img.gif` on a Turtle screen.
- A text prompt asks, "What's another state's name?" with the current score (e.g., "5/50 States Correct").
- Enter a state name (case-insensitive, automatically capitalized). If correct, the state name appears on the map at its coordinates from `50_states.csv`.
- If incorrect, the prompt reappears without feedback.
- Type "Exit" to quit, generating `states_to_learn.csv` with unguessed states.
- The game continues until all 50 states are guessed or the player exits.

## Future Improvements

- Add feedback for incorrect guesses (e.g., "Invalid state name").
- Include a visual indicator for guessed states (e.g., highlight or mark states).
- Add a restart or reset option without exiting.
- Implement a scoring system or timer for competitive play.
- Add sound effects or animations for correct guesses.
- Support partial matches or hints for state names.

## License

This project is open-source and available under the MIT License.