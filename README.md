# Pokemon Catcher

## Overview

This Python program counts the number of unique positions visited by Ash during a journey based on a string of movement directions in a infinite two-dimensional grid.

## How to Run `pokemonCatcher.py`

To run the program, follow these steps:

1. Make sure you have Python 3.7 or a higher version installed on your system.

2. To open the folder in an IDE (e.g., PyCharm) or VSCode and then open a terminal there, or simply open a terminal for the running file (or you need to navigate to the directory where the code is located), in this case, `pokemonCatcher.py` or `testPokemonCatcher.py`

3. Run the program using the following command:

    ```bash
    python pokemonCatcher.py <directions>
    ```

   Replace `<directions>` with a string of movement directions containing only the following characters: 'N', 'S', 'E', or 'O'. For example:

    ```bash
    python pokemonCatcher.py NSEONS
    ```

4. The program will calculate the total number of unique positions visited by Ash and display the result.

5. If the provided directions contain any invalid characters or if you don't provide the correct number of arguments, the program will raise an error. This program is not case sensitive.



## Example

Here's an example of how to run the program:

```bash
python pokemonCatcher.py NSEONS
```
Here's an example of how to run the tests file:

```bash
python testPokemonCatcher.py
```
