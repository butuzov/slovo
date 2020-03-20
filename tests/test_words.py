import pytest
import slovo


class Eng(slovo.Word):
    lang = "en"


class Deu(slovo.Word):
    lang = "de"


def test_all():

    it = Eng("It")
    es = Deu("Es")

    assert str(it) == "(en) It"
    assert it.__html__() == "<small>(en)</small> It"

    assert it.get_image() is None
    it_picture = "https://i.pinimg.com/originals/6b/38/21/6b38213c6d35dbd0a505a883cd694af5.png"
    it.image(it_picture)
    assert it.get_image() == it_picture

    it.translates_to(es)

    assert Deu.lang in it.translations()
    assert Eng.lang in es.translations()

    assert es in it.translation(Deu.lang)
    assert it in es.translation(Eng.lang)
