# Effective practices for teaching Python programming

DDI session - 24th January 2023


## Exercise: Wordle feedback

Wordle is a game where the player must guess a secret word. Each turn, the player makes a guess, and the game tells the player:

- which letters are correct, and in the correct place (✅),
- which letters are in the secret word, but at the wrong place (☑️),
- which letters are not in the word at all (🚫).

Write a function `wordle_feedback(guess, secret)` which takes 2 strings of the same length, `guess` and `secret`, and gives the player feedback on their guess according to the rules above.

You should work in the file `main.py`. There is some starter code available there.

### Example

For example, if the secret was 'bat', the feedback for the guess 'tan' could be something like `☑️t ✅a 🚫n`.

When playing the game (see `play.py`), the output could look like:
```
Guess a 3-letter word!

Guess the word: lot
🚫l 🚫o ✅t

Guess the word: tan
☑️t ✅a 🚫n

Guess the word: cat
🚫c ✅a ✅t

Guess the word: bat
✅b ✅a ✅t

YOU WIN. The secret was 'bat'
```



---
## Python help for those unfamiliar


```python
# f-strings: inserting values into a formatted string
a = 2
b = 3.5
my_string = f'The result of {a} + {b} is {a+b}.'
print(my_string)
```
Output:

    The result of 2 + 3.5 is 5.5.


---
```python
# The enumerate() function
for x, y in enumerate('HELLO'):
    print(x, y)
```
Output:

    0 H
    1 E
    2 L
    3 L
    4 O

---

```python
# You can concatenate strings using +
print('a' + 'b' + 'c')

# Append a new string to an existing string
x = 'AAA'
x += 'BB'      # same as x = x + 'BB'
print(x)
```
Output:

    abc
    AAABB

---

```python
# Joining a list of strings into a single string
list_of_strings = ['dd', 'ee', 'ff', 'xx']
print(list_of_strings)
print('%%%'.join(list_of_strings))
print(''.join(list_of_strings))
```
Output:

    ['dd', 'ee', 'ff', 'xx']
    dd%%%ee%%%ff%%%xx
    ddeeffxx

---
