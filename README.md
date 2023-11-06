# Recursive Calculator
### Philipus Adriel Tandra & Dafa Ramadan Syaidina L5BC

Good afternoon sir, `main.py` contains the recursive calculator and is able to allow white space between numbers as well as account for parse tree construction, has division and contains early error detection.

## White space
```
user_input = list(input('> ').replace(' ', ''))
```
This statement in the program removes whitespace from the inputs and allows for calculations

## Parse Tree construction
### Example Ouput
```
> 6 / 3 + 5
Parse Tree:
+
  /
    6.0
    3.0
  5.0
```
This is example output of the program for parse tree construction

## Additional operators
### Example Output
```
> 6/ 2
Parse Tree:
/
  6.0
  2.0
Result: 3.0
```
Here is example output for division

## Early Error detection
### Example Output
```
> $ + 
Error: Invalid input token: $
```
This is an example of when there is an invalid input token