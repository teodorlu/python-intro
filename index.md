# Programmering i Python

### Norconsult - Sandvika 2016

## Hva ser jeg nå?

Nettleseren Chromium som viser nettsiden `http://teodorlu.github.io/python-intro/` i fullskjerm.

Gå inn her på egen maskin! Da kan du se tidligere lysbilder, og er ikke avhengig av hvor vi er.

## Hva gjør jeg nå?

Du er på Python-kurs! Kurs med fartstid:

- [Lærerkonferanse Teknologihuset, juni 2016](http://kidsakoder.no/konferanser/juni2016/)
- Kodeklubben høsten 2016
- [Lærerkonferanse Teknologihuset, november 2016](http://kidsakoder.no/konferanser/oslo2016/)
- Lærerkonferanse Gardermoen, november 2016
- Internkurs Norconsult, Sandvika, november 2016

## Intensjon for presentasjon

- Ryddig første vei inn i Python-programmering

- Referanse til videre bruk.

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

<!-- ## Driver beregninger

Troll II, 1995

![](http://www.norskpetroleum.no/wp-content/uploads/Troll-A-platform-Photo-%C3%98yvind-Hagen-Statoil.jpg) -->

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
>>> tim_age = 18
# ... og så videre
# Dette er en kommentar. Python ignorerer alt som kommer etter
# en hash (#)
```

* Lagre summen av alderene i en variabel
* Lagre gjenomsnittet av alderene i en variabel

## Tekstmanipulering

```python
>>> navn1 = "Alexander"
>>> navn2 = "Teodor"
>>> navn1 + navn2
```

## Tekstmanipulering

```python
>>> navn1 = "Alexander"
>>> navn2 = "Teodor"
>>> navn1 + navn2
'AlexanderTeodor'
```

## Tekstmanipulering

```python
>>> navn1 = "Alexander"
>>> navn2 = "Teodor"
>>> navn1 + " " + navn2
'Alexander Teodor'
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
>>> alder = 20
>>> if alder == 20:
>>>     svar = "Du er 20 år gammel"
>>> svar
'Du er 20 år gammel'
```

## If-setninger i Python
```python
>>> alder = 30
>>> if alder > 20:
>>>     svar = "Du er over 20 år gammel"
>>> svar
'Du er over 20 år gammel'
```

## If-setninger i Python
```python
>>> alder = 10
>>> if alder < 20:
>>>     svar = "Du er under 20 år gammel"
>>> svar
'Du er under 20 år gammel'
```

## If-setninger i Python
```python
>>> alder = 30
>>> if alder == 20:
     svar = "Du er 20 år gammel"
else:
     svar = "Du er ikke 20 år gammel"
>>> svar
'Du er ikke 20 år gammel'
```

## Oppgave: Gammel nok?

Lag et program som

* Lagrer en alder i en variabel
* Skriver ut "Du er ikke gammel nok" dersom alderen er under 18 år

# Funksjoner

## Funksjoner i Python

```python
def hei(): # Definer en funksjon med navnet 'hei'
    return "Hei" # Funksjonen returnerer teksten "Hei"
```

## Funksjoner i Python

```python
>>> hei()
'Hei'
```

## Parametre

```python
def hei(navn):
    return "Hei " + navn
```

## Parametre

```python
>>> hei("Teodor")
'Hei Teodor'
```

## Myndig
```python
def er_myndig(alder):
    if alder > 17:
        return "Du er myndig!"
    else:
        return "Du er ikke myndig :("
```

## Myndig
```python
>>> er_myndig(18)
'Du er myndig!'
```

## Kalkulator

```python
def addition(tall1, tall2):
    return tall1 + tall2
```

## Kalkulator

```python
>>> addition(2, 3)
5
```

## Oppgave

* Lag en kalkulator som tar inn to tall og en operator, og som returnerer svaret
* Prøv med operatorene +, -, \* og \\

Tips: Bruk if-setninger!

```python
>>> kalkulator("*", 3, 4)
12
```

# Input / output

## Hva er input / output?

* Kommunikasjon med verden uten å bruke IDLE
* ... Når andre enn du skal bruke programmet ditt!

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
input() # Spør brukeren
int()   # Konverterer fra tekst til tall
str()   # Konverterer fra tall til tekst
print() # Forteller brukeren noe
```

```python
navn = input("Hva heter du?")
print(navn)
```

# Lister

## Hva er lister?

- Lister lar oss samle mange verdier
- Google gir oss en liste av søkeresultater
- Facebook har lister over e-postadresser

## Lister i Python

```python
>>> mine_tall = [1,2,3,42,1337,-55]
>>> mine_tall
[1, 2, 3, 42, 1337, -55]
>>> mine_tall[0]
1
>>> mine_tall[-1]
-55
>>> mine_tall[-3]
42
>>> len(mine_tall)
6
>>> mine_tall[6-1]
-55
```

## Lister i Python 2

```python
>>> mine_tall = [1,2,3,42,1337,-55]  # Samme som før
>>> mine_tall[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> mine_tall
[1, 2, 3, 42, 1337, -55]
>>> mine_tall[2:]
[3, 42, 1337, -55]
>>> mine_tall[:2]
[1, 2]
>>> mine_tall[2]
3
>>> [1, 2, 3] + [10, 11, 12]
[1, 2, 3, 10, 11, 12]
```

## Oppgave: elementer fra liste

Gjør følgende i Python-skallet:

* Lag en liste som inneholder 5 tall
* Hent første tall
* Hent nest siste tall

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

## Hvor`for`?

`for` gjør noe med hvert element i en liste:

```python
>>> numbers = [1,2,42]
>>> for number in numbers: print(number)
...
1
2
42
>>> for number in numbers: print(2*number)
...
2
4
84
```

## For i skallet

For på én linje er fint i skallet:
```python
>>> for number in numbers: print number
```

## For i kildekode 1

I kildekode legger vi `for` over flere linjer:

```python
mange_tall = [101,102,103]
for x in mange_tall:
  print(x)
  print("Hei!")
```
skriver ut
```
101
Hei!
102
Hei!
103
Hei!
```

## For i kildekode 2

```python
mange_tall = [101,102,103]
for x in mange_tall:
  print(x)
print("Hei!")  # Fjernet indent --> * Ikke del av for
               #                    * Kjøres én gang, _etter_ at
               #                      for er ferdig!
```
skriver ut
```
101
102
103
Hei!
```

## Gjør noe `n` ganger

```python
>>> range(4)
[0, 1, 2, 3]
>>> range(2,4)
[2, 3]
>>> for n in range(4): print n*n
...
0
1
4
9
```

## Oppgave: 7-gangeren

- Bruk en `for`-løkke til å skrive ut 7-gangeren.
- Ønsket output:

```
0
7
14
21
28
35
42
49
56
63
70
```

## Oppgave: 7-gangeren

Løsningsforslag:

```python
for n in range(0, 11):
  print(7*n)
```

## Flere for-løkker i Python

```python
mange_tall = [1,2,3,4,5,6,7,8,9]
for tall in mange_tall
    print("Sjekker om " + str(tall) + " er et partall")

    if tall % 2:
        print(str(tall) + " er et oddetall")
    else:
        print(str(tall) + " er et partall")
```

## Oppgave: mattespill 2!

* Bruk mattespillet du allerede har laget
* I stedet for *uendelig* mange oppgaver, gi brukeren 5 oppgaver!

# Programmer ditt eget gjettespill!

## Hø?

![](assets/guess_my_number_illustration.png)

## Takk til Barski

Spill og illustrasjon er hentet fra den strålende boka "Land of Lisp" av Conrad Barski, og tilpasset Python.

Musikkvideo:

<iframe width="560" height="315" src="https://www.youtube.com/embed/HM1Zb3xmvMc" frameborder="0" allowfullscreen></iframe>

## Demo

Slik kan det fungere ...

Sider under beskriver hvordan gjettespillet kan implementeres. Prøv først selv,
og gå videre nedover om du trenger et tips!

## Gjettefunksjon

Gitt at vi har en øvre og nedre grense, kan vi gjette at tallet ligger midt i mellom:

<!-- ![](assets/guess_my_number_1.png) -->

```python
# Gjettespill!

low = 0
high = 100

def guess():
    total = high + low          # f.eks 75 + 50 = 125
    average = total / 2         # 125/2 = 62.5
    next_guess = int(average)   # int(62.5) = 62
    return next_guess
```

## Prøve gjettefunksjon

Hvordan fungerer denne? Vi kjører modulen i IDLE, så vi kan leke med verdiene.

```python
>>> guess
<function guess at 0x7fee85ff9840>
```

Wops, guess var en funksjon. Vi trenger paranterser for å *kalle* en funksjon:

```python
>>> guess()
50
```

## Prøve gjettefunksjon

```python
>>> high
100
>>> low
0
```

... så low starter på 0, og high på 100. Hva om vi endrer på dette?

```python
>>> low = 75
>>> guess()
87
```

## Lavere? Høyere?

```python
>>> # Hemmelig tall er 42!
>>> guess()
50
>>> lower()
24
>>> higher()
37
>>> higher()
43
>>> lower()
40
>>> higher()
41
>>> higher()
42
```

## Lavere? Høyere?

Vi svarer datamaskinen ved å kalle funksjonen `lower()` eller `higher()`:

```python
def lower():
    # global lar oss endre en global variabel
    # inne i en funksjon
    global high
    high = guess() - 1
    return guess()

def bigger():
    global low
    low = guess() + 1
    return guess()
```

## Hva når vi vinner?

```python
>>> # Guessing 77
>>> guess()
50
>>> higher()
75
>>> higher()
88
>>> lower()
81
>>> lower()
78
>>> lower()
76
>>> higher()
77
>>> correct()
'Yippie!!!'
```

## "Binærsøk"

Gratulerer, dere har nå implementert et binærsøk! Binærsøk er en av grunnene til at Google-søk er raske.

# Python og Abaqus

## Arkitektur 1

![](assets-no/abaqus-python-how-it-works.png)

## Arkitektur 2

- På min maskin ligger Abaqus' Python på `C:\SIMULIA\CAE\2016\win_b64` `\code\bin\python.exe`

- Store deler av Abaqus CAE er skrevet i Python, og kjører på en tilpasset Python-plattform.

- Når vi kjører kode på Abaqus' Python-plattform, får vi tilgang til å lage bokser, endre en CAE-modell og hente ut data fra ODB-er.

## Abaqus Python i CAE

Du har allerede en Python-tolker! `>>>` tyder på at du kan skrive Python.

![](assets-no/abaqus-python-cae.png)

## Abaqus Python i CMD

![](assets-no/abaqus-python-cmd.png)

## Kjøre filer i Abaqus 1

Lag en ny Python-fil på valgfri måte

![](assets-no/abaqus_defining_gx_in.png)

## Kjøre filer i Abaqus 2

Trykk `Run Script`

![](assets-no/abaqus-cae-run-script.png)

## Kjøre filer i Abaqus 3

og og velg scriptet ditt:

![](assets-no/abaqus-cae-choose-my_function.png)

## Kjøre filer i Abaqus 4

Hva du skriver ut med `print` dukker opp her:

![](assets-no/abaqus-cae-print-goes-here.png)

## Kjøre filer i Abaqus 5

og ting du definerer i filen blir tilgjengelig fra skallet:

![](assets-no/abaqus-cae-use-functions-here.png)

## Alternativ Python-editor

Jeg bruker [Github Atom](http://atom.io). Denne er god.

## Oppgave A: Abaqus

Parametrisering av plate:

__Sett inn bilde.__

## Oppgave del A1

__Modeller fritt opplagt plate i Abaqus: `plate.cae`__

- Størrelse: 4m x 6m x 200 mm.
- Dekke: 0.2 m betong, E=30e9 Pa, ν=0.2
- Dimensjonerende last: 10 kN/m2

## Oppgave del A2

__Gjør om til script__

Kopier journal (`plate.jnl`) til `generate-plates.py`.
Endre koden til å generere en annen modell:

- Modellnavn `plate_4_6_260_20`
- Tykkelse 260 mm
- Last 20 kN/m2

## Oppgave del A3

__Parametriser over tykkelse og kraft__

- Trekk ut tykkelse og kraft som variabler
- Generer 9 parts i samme modell:
    - Tykkelse 150 mm, 200 mm eller 260 mm
    - Kraft 7 kN/m2, 10 kN/m2 eller 20 kN/m2
- Lag navn fra parametre:

```
plate_4_6_160_7
plate_4_6_160_10
plate_4_6_160_10
plate_4_6_200_7
plate_4_6_200_10
...
```

## Ferdig alt?

__Len deg tilbake og nyt hva du har fått til.__

Muligheter videre:

- Generer jobb for hver modell
- Kjør jobber
- Åpne ODB og sammenlikne!

## Ressurser for Python og Abaqus

![](assets/abaqus-documentation.png)

## Ressurser for Python og Abaqus

"Scripting" er grunnleggende funksjonalitet. Nyttig til små og store prosjekter.

* [Abaqus Scripting User's Guide](http://50.16.225.63/v2016/books/cmd/default.htm) går gjennom hvordan hvordan du gjør ting som å generere CAE-modeller og manipulere view i en ODB
* [Abaqus Scripting Reference Guide](http://50.16.225.63/v2016/books/ker/default.htm) lister opp alle funksjoner og klasser for programmering av CAE og ODB-modulene og definerer hva de gjør

## Ressurser for Python og Abaqus

"GUI" er grafikk til større programmer.

* [Abaqus GUI Toolkit User's Guide](http://50.16.225.63/v2016/books/cus/default.htm) går gjennom hvordan hvordan du kan lage grafiske grensesnitt som ANDIM og PROCESS-PLUGIN
* [Abaqus GUI Toolkit Reference Guide](http://50.16.225.63/v2016/books/gui/default.htm) lister opp alle funksjoner og klasser for programmering av grafikk

# Python og Dynamo

## Arkitektur

Dynamo bruker et bibliotek som heter **IronPython**. IronPython er en python-implementasjon som kjører på .NET. Det vil typisk si at Dynamo inneholder en fil som heter `python.dll`, som kan tolke Python-script.

Script du skriver kjøres i et modifisert miljø, der variabelen `IN` automagisk inneholder hva du kobler til scriptet ditt på venstre side og variabelen `OUT` hva du vil sende ut på høyre side.

Python-script lagres inne i Dynamo-filer (`.dyn`).

## Starte Dynamo

![](assets-no/dynamo-run-with-revit-from-here.png)
![](assets-no/dynamo-run-without-revit-from-here.png)

## Python-noden

Fra høyreklikk:

![](assets-no/dynamo-python-1.png)

## Python-noden

Fra funksjonslisten:

![](assets-no/dynamo-python-2.png)

## Redigere script

Dobbeltklikk "nede" i boksen:

![](assets-no/dynamo-python-edit.png)

## `IN` og `OUT`

Hva kommer inn, hva går ut?

![](assets-no/dynamo-python-script-def.png)

## Teste script

Kobler på en `Number Slider`:

![](assets-no/dynamo-python-testing-inputs.gif)

## Alternativ Python-editor

Jeg bruker [Github Atom](http://atom.io). Denne er god.

## Oppgave D: Dynamo

Betongbjelke med varierende tverrsnitt.

## Oppgave del D1

Definer en momentdiagrammet matematisk for en fritt opplagt bjelke med jevnt fordelt last.

- Bjelkelengde: L [m]
- Linjelast: q [N/m]
- Avstand fra venstre opplegg: x [m]

M(L,q,x) = ...

Hva er M(8,30000,3)?

## Oppgave del D2

- Implementer `M(L,q,x)` i Python:

```python
def M(L,q,x):
  # Regn ut moment!
  moment = # ... unngår å bruke navnet på funksjonen (M)
  return moment
```

- Hva beregner funksjonen din for `M(8,30000,3)`?

## Oppgave del D3

Tegn momentdiagrammet streker i Dynamo. Velg passe skala. 50 kNm <--> 1 m OK?

## Oppgave del D4

Nå skal vi velge høyde på bjelken. Dette gjør vi enkelt:

1. Regner ut nødvendig indre momentarm `d`
2. Legger på `100 mm` for å få ca nødvendig høyde

Vi neglisjerer effekt fra skjærkrefter.

Definer en matematisk funksjon for berening av nødvendig høyde.

- Armeringsmengde As [m2]

h(L,q,As,x) = ...

- Hva er h(8,30000,3,0.00164)?

## Oppgave del D5

- Implementer `h(L,q,As,x)` i Python:

```python
def h(L,q,As,x):
  moment = M(L,q,x)
  height = # ... unngår å bruke navnet på funksjonen (h)
  return height
```

- Hva beregner funksjonen din for `h(8,30000,3,0.00164)`?

## Tegn bjelke!

# Veien videre

## Lykke til!

- Spis elefanten én bit av gangen
- Du må selv skrive kode om du skal lære programmering

## Videre ressursser

* Disse sidene ligger på `http://teodorlu.github.io/python-intro/`, og blir her.
* [Kodeklubbens nettsider](http://kodeklubben.github.io/python/) har mange gode oppgaver på norsk. To spennende spill:
    * [Mattespill](http://kodeklubben.github.io/python/mattespill/mattespill.html)
    * [Gjettelek](http://kodeklubben.github.io/python/gjettelek/gjettelek.html)
* [Learn Python the Hard Way](https://learnpythonthehardway.org/book/) er dyptgående, grundig og lærerik.

## Videre verktøy

* [Github Atom](https://atom.io/) er en meget god teksteditor til Python.

    En teksteditor er et godt valg for å redigere én fil. Jeg bruker Atom til nesten alt jeg skriver av Python-kode.

* [PyCharm](https://www.jetbrains.com/pycharm/) er et godt IDE til Python.

    IDE-er er større og mer kompliserte enn teksteditorer. PyCharm kan være et godt valg til større prosjekter. Jeg bruker delvis PyCharm når jeg utvikler på ANDIM.
