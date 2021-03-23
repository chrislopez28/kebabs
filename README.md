# Kebabs
[![Build Status](https://travis-ci.com/chrislopez28/kebabs.svg?branch=main)](https://travis-ci.com/chrislopez28/kebabs)

Kebabs is a lightweight Python package that only does one thing: convert a string to [kebab-case](https://en.wikipedia.org/wiki/Letter_case#Special_case_styles). 

## Requirements
Python 3.6+

## Installation
```python

```

## How to Use
```
from kebabs import kebab_case
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

Kebabs removes the following punctuation marks: ("), ('), (.), (?), and (!).

```python
kebab_case("Why, sometimes I've believed as many as six impossible things before breakfast.") 
# why-sometimes-ive-believed-as-many-as-six-impossible-things-before-breakfast
```

### Spaces
Kebabs removes spaces, newlines, and tabs. 

```python

```
