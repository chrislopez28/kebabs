import pytest
from .kebabs import kebab_case


def test_camelcase():
    assert kebab_case("camelCase") == "camel-case"


def test_sentence():
    assert kebab_case(
        "Why, sometimes I've believed as many as six impossible things before breakfast.") == "why-sometimes-ive-believed-as-many-as-six-impossible-things-before-breakfast"


def test_snakecase():
    assert kebab_case("snake_case") == "snake-case"


def test_pascalcase():
    assert kebab_case("PascalCase") == "pascal-case"
