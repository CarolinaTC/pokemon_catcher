import sys

def find_pokemons(directions: str) -> int:
    """
      Counts the number of unique positions visited by Ash based on a string of directions.
      Parameters:
      directions type (str): A string containing the directions for Ash's movement. Each character in the string represents a direction.
          - 'N' / 'S' / 'E' / 'O'
      Returns:
      int: The total number of unique positions visited by Ash during the journey.
      Raises:
      Exception: If the provided directions contain any character other than 'N', 'S', 'E', or '0'.
      """

    # Ash current position
    current_position = (0, 0)

    # Locations on the infinite two-dimensional grid where Ash passed through
    pokemons_found = [(0, 0)]
    #pokemons_found = set()


    for dir in directions:
        if dir == "N":
            current_position = (current_position[0], current_position[1] + 1)
        elif dir == "S":
            current_position = (current_position[0], current_position[1] - 1)
        elif dir == "E":
            current_position = (current_position[0] + 1, current_position[1])
        elif dir == "O":
            current_position = (current_position[0] - 1, current_position[1])
        else:
            raise Exception(f"Provided directions are not valid: {dir}. Please provide a string containing only the following characters: N, S, E, O.")

        if current_position not in pokemons_found:
            pokemons_found.append(current_position)

    return len(pokemons_found)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Please provide a string containing only the following characters: N, S, E, O.")
    directions = sys.argv[1].upper()
    result = f"Total number of pokemons caught: {find_pokemons(directions)}"
    print(result)

