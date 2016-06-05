# Programmering i Python

### Lærerkonferanse Oslo 2016

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

## Populære språk*

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

\* Mest brukte på GitHub i 2016.

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
alder = input("Hvor gammel er du?")
print(alder)
```

# If

## Hva er if-setninger?

* Sjekker om et uttrykk er sant, og kjører så koden


## If-setninger i Python
```python
alder = input("Hvor gammel er du?")

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
masseTall = [1,2,3,4,5,6,7,8,9]
print("Tall nummer 1 i rekken er " + str(test[0]))
```

## For-løkker

* Går igjennom (itererer) over en liste med verdier

```python
for i in range(100):
    print(i)

masseTall = [1,2,3,4,5,6,7,8,9]
for i in masseTall
    print("Sjekker om " + i + " er et partall")

    if i % 2:
        print(i + " er et partall")
    else:
        print(i + " er et oddetall")
```
