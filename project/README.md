# Database 4 Sales
#### Video Demo:  <https://youtu.be/8rZkZxx9YFs>
#### Description:

This is a straightforward sales database management program developed in Python, providing essential functionalities for item registration, modification, and removal.

## Functionalities

1. **Item Registration:**
   - Users can register new items by providing a name, cost, and sales price.
   - Input validation ensures that only valid alphanumeric names are accepted, avoiding special characters.

2. **Item Change:**
   - Allows users to change the name, cost, or sales price of existing items.
   - Users can remove a single item, with a confirmation prompt to avoid accidental deletions.

3. **Program Output:**
   - The program provides the option to exit gracefully.

## How to Use

1. Upon launching the program, users encounter a main menu with selectable options.
2. Users can choose from available options like item registration, modification, or program exit.
3. Each menu option comes with additional instructions for seamless user interaction.

## Requirements

- Python 3.x
- Python libraries: `pyfiglet`, `tabulate`

## Execution

Run the program using the following command:

```bash
python project.py
```

## Author

#### [Lucas Felipe de Souza Bastos Figueiredo](https://github.com/Luxxer1)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

---

## Unit Tests

### [test_project.py](test_project.py)

#### test_check_item_name()
- Validates the `check_item_name` function.
- Tests the conversion of input names to lowercase and checks for invalid characters.

#### test_check_valid_float()
- Validates the `check_valid_float` function.
- Tests the conversion of input strings to floating-point numbers and checks for invalid input.

#### test_get_unique_item_id()
- Validates the `get_unique_item_id` function.
- Tests the generation of a unique item ID based on the current database content.

#### test_check_item_id()
- Validates the `check_item_id` function.
- Tests the retrieval of the correct item ID from the database and checks for invalid input.

These unit tests ensure the correctness of critical functions in the program, contributing to the overall reliability and robustness of the sales database management system.

For more details, refer to the [test_project.py](test_project.py) file.
