# Kebabs
[![Build Status](https://travis-ci.com/chrislopez28/kebabs.svg?branch=main)](https://travis-ci.com/chrislopez28/kebabs)
[![codecov](https://codecov.io/gh/chrislopez28/kebabs/branch/main/graph/badge.svg?token=1VY7MANTD3)](https://codecov.io/gh/chrislopez28/kebabs)

Kebabs is a lightweight Python package that only does one thing: convert a string to [kebab-case](https://en.wikipedia.org/wiki/Letter_case#Special_case_styles). 

## Requirements

Python 3.6+

## Installation

```shell
python -m pip install git+https://github.com/chrislopez28/kebabs.git
```

## How to Use
Import the `kebab_case()` function from kebabs and have at it.
```python
from kebabs import kebab_case

kebab_case("I like kebabs") # i-like-kebabs
```

## Examples

### Common Case Styles

Kebabs handles common case styles:

```python
kebab_case("camelCase")     # camel-case
kebab_case("snake_case")    # snake-case
kebab_case("PascalCase")    # pascal-case
```


### Punctuation

Kebabs removes the following punctuation marks: ("), ('), (.), (,), (?), and (!).

```python
kebab_case("Why, sometimes I've believed as many as six impossible things before breakfast.") 
# why-sometimes-ive-believed-as-many-as-six-impossible-things-before-breakfast
```

### Spaces
Kebabs removes spaces. 

```python
kebab_case("Spaces in                    the middle")
# spaces-in-the-middle
```
