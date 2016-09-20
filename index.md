# Programmering i Python

### Kodeklubben Oslo 2016

## Oss?

Fransis (er her) og Teodor (kommer snart!)

# Om Python

## For begynnere

Forståelig syntaks med lite støy:

```python
name = input("Hi! I'm Python. Who are you? ")
print("Hello, " + name + "! Nice to meet you!")
```

## *og* viderekommende

* Støtter imperativ, objektorientert og funksjonell programmering
* Knallgodt standardbibliotek

## Eksempler på bruk

* Instagram, Pinterest og The Washington Times kjører på Python-rammeverket Django
* Maskinlæring: Google TensorFlow anbefaler Python som grensesnitt
* Vitenskaplig og numerisk programmering: SciPy og NumPy

# Variabler

## Hva er en variabel?

* Tilordner verdier til navn, for gjenbruk

## Variabler i Python

```python
navn = "Alexander Perry"
alder = 27
```

## Oppgave: familiens alder

* Lagre alderen til 3 familiemedlemmer i variabler

```python
tim_age = 18
# ... og så videre
```

* Lagre summen av alderene i en variabel
* Lagre gjenomsnittet av alderene i en variabel

# Input / output

## Hva er input / output?

## Input / output i Python

```python
navn = input("Hvor heter du?")
print(navn)
```

## Å lese inn tall

* Funksjonen `input()` gir ut *tekst*
* Funksjonen `int()` konverterer tekst til tall

```python
age_text = input("How old are you? ")
age = int(age_text)
```

## Å skrive ut tall

* Funksjonen `str()` konverterer tall til tekst

```python
age_text = input("How old are you? ")
age = int(age_text)
# Obs: "in five " + "years" blir "in five years"!
print("In five years, you are " + str(age + 5) + " years old!")
```

## Oppgave: familiens alder 2

Nå skal vi utvide oppgaven fra tidligere. I stedet for å lagre alderen til familiemedlemmer i programmet, spør brukeren! Skriv så ut gjennomsnitt og total alder.

Funksjoner vi har brukt:

* `input()` spør brukeren
* `int()` konverterer fra tekst til tall
* `str()` konverterer fra tall til tekst
* `print()` forteller brukeren noe

```python
navn = input("Hvor heter du?")
print(navn)
```

# Stemningen i Python

## Navnet?

![](http://www.anglotopia.net/wp-content/uploads/2015/05/Monty-Python-and-The-Holy-Grail-40th_640.jpg)

---

![](http://imgs.xkcd.com/comics/python.png)

Fra [XKCD](http://xkcd.com/353/).

# If

## Hva er if-setninger?

* Sjekker om et uttrykk er sant, og kjører så en gitt kodesnutt


## If-setninger i Python
```python
svar = input("Hvor gammel er du?")
alder = int(svar)

if alder == 20:
    print("Du er 20 år gammel")
elif alder > 20:
    print("Du er over 20 år gammel")
else:
    print("Du er " + str(alder) + " år gammel")
```

## Oppgave: Gammel nok?

Lag et program som

* Leser inn brukerens alder
* Skriver ut "Du er ikke gammel nok" dersom brukeren er under 18 år

# Lister

## Hva er lister?

* Null-indeksert liste over verdier

## Lister i Python
```python
masseTall = [1,2,3,4,5,6,7,8,9]
print("Tall nummer 1 i rekken er " + str(mangeTall[0]))
```

## Oppgave: elementer fra liste

* Lag en liste som inneholder 5 tall
* Skriv ut første tall
* Skriv ut nest siste tall

Tips: `list[-3]` henter element 3 *bakfra*!

# While

## Hva er while-løkker?

* Kjører en kodesnutt så lenge et gitt uttrykk er sant
* Kan kjøre evig, og avbrytes med break

## While-løkker i Python

```python
print("Dette er en huskeliste-app")
huskeliste = []

while True:
    svar = input("Legg til noe på huskelisten: ")
    huskeliste.append(svar)
    print(huskeliste)
```

## Oppgave: mattespill!

Lag et multiplikasjonsspill!

1. Be brukeren gange to tall
2. Sjekk svaret!
3. Gjør dette mange ganger ... `while`?

Tilfeldige tall:

```python
from random import randint

x = randint(0, 6) # gir x = 0, x = 1, ..., eller x = 5
```

# For

## Hva er for-løkker?

* Kjører en kodesnutt et gitt antall ganger
* Går igjennom (itererer) over en liste med verdier

## For-løkker i Python

```python
for i in range(100):
    print(i)
```

* `range(4)` gir `[0, 1, 2, 3]`
* `range(10)` gir `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
* `range(n)` gir *n* elementer!

## Flere for-løkker i Python

```python
mangeTall = [1,2,3,4,5,6,7,8,9]
for tall in mangeTall
    print("Sjekker om " + str(tall) + " er et partall")

    if tall % 2:
        print(str(tall) + " er et oddetall")
    else:
        print(str(tall) + " er et partall")
```

## Oppgave: mattespill 2!

* Bruk mattespillet du allerede har laget
* I stedet for *uendelig* mange oppgaver, gi brukeren 5 oppgaver!

# Workshop

## Oppgaver på kodeklubben

[Kodeklubbens nettsider](http://kodeklubben.github.io/python/) har gode oppgaver:

* [Mattespill](http://kodeklubben.github.io/python/mattespill/mattespill.html)
* [Gjettelek](http://kodeklubben.github.io/python/gjettelek/gjettelek.html)
