# Programmering i Python

### Lærerkonferanse Oslo 2016

## Oss?

![](assets/index-c4edb.png) ![](assets/index-0b0f7.png)

Perry og Teodor

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
*

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

# Stemningen i Python

## Navnet?

![](http://www.anglotopia.net/wp-content/uploads/2015/05/Monty-Python-and-The-Holy-Grail-40th_640.jpg)

---

![](http://imgs.xkcd.com/comics/python.png)

Fra [XKCD](http://xkcd.com/353/).

# If

## Hva er if-setninger?

* Sjekker om et uttrykk er sant, og kjører så koden


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

# While

## Hva er while-løkker?

* Kjører et sett med kode så lenge et gitt uttrykk er sant


```python

```

## Lister

* Null-indeksert liste over verdier

```python
mangeTall = [1,2,3,4,5,6,7,8,9]
print("Tall nummer 1 i rekken er " + str(mangeTall[0]))
```

## For-løkker

## Hva er for-løkker?

* Kjører en kodesnutt et gitt antall ganger
* Går igjennom (itererer) over en liste med verdier

## For-løkker i Python

```python
for i in range(100):
    print(i)

mangeTall = [1,2,3,4,5,6,7,8,9]
for i in mangeTall
    print("Sjekker om " + i + " er et partall")

    if i % 2:
        print(i + " er et partall")
    else:
        print(i + " er et oddetall")
```

# Workshop

## Oppgaver på kodeklubben

[Kodeklubbens nettsider](http://kodeklubben.github.io/python/) har gode oppgaver:

* [Mattespill](http://kodeklubben.github.io/python/mattespill/mattespill.html)
* [Gjettelek](http://kodeklubben.github.io/python/gjettelek/gjettelek.html)
