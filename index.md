# Programmering i Python

### Lærerkonferanse Oslo 2016

## Oss?

![](assets/index-c4edb.png) ![](assets/index-0b0f7.png)

<!-- Perry | Teodor
------|-------
Systemutvikler | Sivilingeniør -->

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

<!-- ## Populære språk*

1. JavaScript
2. Java
3. Ruby
4. PHP
5. **Python**
6. CSS
7. C++
8. C#
9. C
10. HTML

\* Mest brukte på GitHub i 2016. -->

# Grunnleggende programmering

# Variabler

## Hva er en variabel?

* Tilordner verdier til navn, for gjenbruk

## Variabler i Python

```python
navn = "Alexander Perry"
alder = 27
```

# Input / output

## Hva er input / output?

## Input / output i Python

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

## Lister

* Null-indeksert liste over verdier

```python
masseTall = [1,2,3,4,5,6,7,8,9]
print("Tall nummer 1 i rekken er " + str(mangeTall[0]))
```


# While

## Hva er while-løkker?

* Kjører en kodesnutt så lenge et gitt uttrykk er sant


## While-løkker i Python

```python
print("Dette er en huskeliste-app")
huskeliste = []

while True:
    svar = input("Legg til noe på huskelisten: ")
    huskeliste.append(svar)
    print(huskeliste)
```


## For-løkker

* Går igjennom (itererer) over en liste med verdier

```python
for i in range(100):
    print(i)

mangeTall = [1,2,3,4,5,6,7,8,9]
for tall in mangeTall
    print("Sjekker om " + str(tall) + " er et partall")

    if i % 2:
        print(str(tall) + " er et partall")
    else:
        print(str(tall) + " er et oddetall")
```
