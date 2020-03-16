# slovo (wip)

Slovo (slo-vo, Ukrainian for "word"). Tiny lib for making words into... well into something.

## Examples

### Creating Langauge Class Instance

```python3
from slovo import Word, Gender, Term


# New usage Class can be created via instantiation
class Castellano(Word):
  lang = "es"
print(Castellano("verde"))
>> (es) verde


# Or Using class methods
Eng = Word.constr("Eng", "en")
print(Eng("Hello"))
> (en) Hello
```

### Combining Words

```python3
words = Eng("Hello")+Eng("There")
print(words, words.)
> (en) Hello There
```

### TODO
....
