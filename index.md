# Programmering i Python

### Lærerkonferanse Oslo 2016

## Hva ser jeg nå?

Nettleseren Chromium som viser nettsiden `http://teodorlu.github.io/python-intro/` i fullskjerm.

Gå inn her på egen maskin! Da kan du se tidligere lysbilder, og er ikke avhengig av hvor vi er.

## Hvem er vi?

Teodor Heggelund

![](http://www.norconsult.com/Images/Logos/logo_norconsult_200x200.jpg)

---

Alexander Perry

![](http://kampanje.com/contentassets/ef767832064f4b5b853db52dee9ca940/logo_bouvet_222x222px.png)

# Hvorfor Python?

## For begynnere

Forståelig syntaks med lite støy:

```python
>>> navn = "Teodor"
>>> navn
'Teodor'
>>> "Hei! Jeg heter " + navn
'Hei! Jeg heter Teodor'
```

## *og* viderekommende

* Støtter imperativ, objektorientert og funksjonell programmering
* Knallgodt standardbibliotek

## Driver New York Times

![](http://www.slate.com/content/dam/slate/articles/life/culturebox/2014/01/140108_CBOX_NYTimesRedesign.jpg.CROP.promo-mediumlarge.jpg)

## Brukes av NASA

![](http://www.nasa.gov/sites/default/files/thumbnails/image/ocs_iss_0.jpg)

## Brukes av Google

![](https://www.google.com/selfdrivingcar/images/home-where.jpg)

## Driver beregninger

Troll II, 1995

![](http://www.norskpetroleum.no/wp-content/uploads/Troll-A-platform-Photo-%C3%98yvind-Hagen-Statoil.jpg)

# Verktøy

## Hva trenger vi?

Når vi utvikler Python, trenger vi to verktøy:

* Et skall
* En teksteditor

Når vi installerer programmeringsspråket Python, følger miljøet IDLE med.
IDLE gir oss et skall og en teksteditor.

## Last ned Python

1. Gå til [python.org/downloads](https://www.python.org/downloads/)
2. Last ned og installer nyeste Python (`3.x.x`)

## Python-skallet i IDLE

Et skall lar oss skrive en linje og tolke den.

![](assets/idle-shell.png)

## Python-skallet i IDLE

Tre piler (`>>>`) dukker automatisk opp i skallet. Når vi skriver tre piler her:

```
>>> 4 + 4
8
```

skal du skrive `4 + 4` og trykke enter.

## Teksteditoren i IDLE

![](assets/idle-new-file.png)

## Teksteditoren i IDLE

Vi åpner teksteditoren ved å lage en ny fil fra Python-skallet:

`File` --> `New file` (`Ctrl+N`) gir oss en tom fil:

![](assets/idle-empty-file.png)

## Teksteditoren i IDLE

Først lagrer vi filen der vi vil ha den, og kaller den `hello.py` ...

![](assets/idle-save-as.png)

## Teksteditoren i IDLE

... så kjører vi den for å se at alt er i orden ...

![](assets/idle-run-module.png)

## Teksteditoren i IDLE

... og en tom fil gjør ... ingenting.

![](assets/idle-nothing-happened.png)

# Variabler

## Hva er en variabel?

* Tilordner verdier til navn, for gjenbruk

## Variabler i Python

```python
>>> navn = "Alexander Perry"
>>> navn
'Alexander Perry'
>>> alder = 27
>>> alder
27
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
navn = input("Hva heter du?")
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

```python
 input() # spør brukeren
 int() # konverterer fra tekst til tall
 str() # konverterer fra tall til tekst
 print() # forteller brukeren noe
```

```python
navn = input("Hva heter du?")
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
