from __future__ import annotations

from typing import Dict, Set, Optional

from slovo import Gender, Term
from slovo import (
    ImmutableClassError,
    DiffLangsError,
)


class Word():
    lang: Optional[str] = None

    def __init__(self, word):
        self._translations: Dict[str, Set[Word]] = {}
        self._synonyms: Set[Word] = set()
        self._word: str = word

        # TODO: inbound collections

        # default none/zero values
        self._term: Term = Term.NONE
        self._gender: Optional[Gender] = None
        self._img: Optional[str] = None

    @property
    def value(self) -> str:
        return self._word

    def term(self, term: Term) -> Word:
        """ Sets the lexical class to the word """

        is_none = self._term == Term.NONE
        is_same = self._term == term
        is_phrase = self._term == Term.PHRASE and term == Term.PHRASE

        if is_none or is_same or is_phrase:
            self._term = term
        elif not is_none:
            raise ImmutableClassError(
                "Can't change class to %s. Current setting %s" % (term, self._term))

        return self

    def gender(self, gender: Gender) -> Word:
        """ Does word has gender? """
        # TODO: Additional type checks.

        self._gender = gender
        return self

    def picture(self, src: str) -> Word:
        """ set picture for word or phrase"""
        self._img = src
        return self

    def img(self) -> Optional[str]:
        return self._img

    def __str__(self) -> str:

        if self.lang:
            return "({}) {}".format(self.lang, self._word)

        return "{}".format(self._word)

    def __hash__(self) -> int:
        return hash(repr(self))

    def __repr__(self) -> str:
        # TODO: better representation.

        attrs = []

        attrs.append(f"term={self._term}" if self._term != Term.NONE else "")
        attrs.append(f"gender={self._gender}" if self._gender else "")

        return '<%s %s>%s</%s>' % (self.lang, " ".join(attrs).strip(), self.value, self.lang)

    def __add__(self, word: Word) -> Word:
        # TODO: Better add mehanisms

        if self.lang != word.lang:
            raise DiffLangsError("Different languages")

        new = Word("%s %s" % (self.value, word.value))
        new.lang = self.lang
        new.term(Term.PHRASE)

        return new

    @classmethod
    def constr(cls, name, lang):
        return type(name, (cls, ), {"lang": lang})


if __name__ == "__main__":

    Eng = Word.constr("Eng", "en")
    Deu = Word.constr("Deu", "en")

    class Cas(Word):
        lang: str = "es"

    # El Gato Sobre La Mesa
    palabras = {
        'el': Cas("El").gender(Gender.Mas),
        'gato': Cas("Gato").gender(Gender.Mas),
        'sobre': Cas("Sobre"),
        'la': Cas("La").gender(Gender.Fem),
        'mesa': Cas("Mesa").gender(Gender.Fem),
    }

    table1 = Eng("Table").term(Term.NOUN)
    table2 = Eng("Table").term(Term.NOUN)

    print(table1, hash(table1), repr(table1), id(table1))
    print(table2, hash(table2), repr(table2), id(table2))
