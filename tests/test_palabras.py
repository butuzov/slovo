import pytest
import slovo


class Spa(slovo.Word):
    lang: str = "es"


def test_str():
    assert str(Spa("El gato")) == "(es) El gato"
