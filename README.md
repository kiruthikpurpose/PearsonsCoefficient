# Pearson Correlation Coefficient Calculator

This Python script calculates the Pearson correlation coefficient between two sets of values, `x` and `y`. The Pearson correlation coefficient is a measure of the linear relationship between two variables, where a value of 1 indicates a perfect positive correlation, -1 indicates a perfect negative correlation, and 0 indicates no correlation.

## How It Works

1. The script accepts two lists of integers (values for `x` and `y`).
2. It calculates the Pearson correlation coefficient using the following formula:

      r = [ n(Σxy) - (Σx)(Σy) ] / sqrt[ (nΣx² - (Σx)²)(nΣy² - (Σy)²) ]

3. The result is printed as the Pearson correlation coefficient.

## Requirements

- Python 3.x

## Usage

1. Clone or download this repository.
2. Run the script with any Python environment.
3. The script will prompt for input values.

### Example:

```bash
python pearson_correlation.py
```

Input:
```
Enter the values of x: 
1 2 3 4 5
Enter the values of y: 
2 4 6 8 10
```

Output:
```
Pearson correlation coefficient: 1.0
```

## Error Handling

- If the denominator in the Pearson formula is zero, the script will handle this gracefully by setting the result to 0.

## License

This project is licensed under the MIT License.
