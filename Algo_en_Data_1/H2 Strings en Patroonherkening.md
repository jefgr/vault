# Characters, Strings, en Patroonherkening

## Characters: 
> char->integer
> integer->char

ASCII 0-127 vast (7 bits), 128-255 vaker variërend (8 bits)

ASCII achterhaald door Unicode

## String

> Een string is een eindige sequentie van karakters

Default string immutable (er is een library met mutable-string datatype)

```scheme
O(1):
string-length
string-ref
O(n):
string->list
list->string
O(min(n, m)):
;predicaten om strings te vergelijken
(string=? a b)
(string-ci=? a b)
(string<? a b)
(string>? a b)
(string<=? a b)
(string>=? a b)
(string-ci<? a b)
(string-ci>? a b)
(string-ci<=? a b)
(string-ci>=? a b)
```

postfix -ci (case incensitive)

## Patroonherkenningsprobleem

 > Gegeven een tekst
 > Gegeven een patroon
 > Wat is de index van het patroon in de tekst?

```scheme
match
(string string -> number U {#f})
```

index wordt ook wel _offset_ of _shift_ genoemd
### Notatie
tekst: t
patroon p

| woord                      | notatie    | scheme |
| -------------------------- | ---------- | ------ |
| tekst                      | t          | t      |
| patroon                    | p          | p      |
| lengte tekst               | $n_{t}$    | n-t    |
| lengte patroon             | $n_{p}$    | n-p    |
| lengte van een string      | \|s\|      |        |
| k'de karakter              | $S_{k}$    |        |
| substring (i tot en met j) | $S_{i->j}$ |        |
voor string v = u.w geldt
u prefix, w suffix
u en w zijn echte pre/suffix als verschillend van "" en v
# Brutekracht Algoritme

Geneste loop:
- Check t1 tegen p1
	- if gelijk: check t2 tegen p2
	- else: move 1tje vooruit en start terug te testen bij p1
herhaal tot einde tekst of tot t-x == p-eind
Dit geeft timecomplexity worst-case $O(n_{t}.n_{p})$ 

belangrijk  $O(n_{t}.n_{p}) \neq O(n²)$
# Quicksearch Algoritme

In de praktijk zeer goed, average-case zeer goed voor engelse teksten
Worst-case blijft  $O(n_{t}.n_{p})$ 

- **Vergelijking**: Quicksearch vergelijkt het patroon met de tekst van links naar rechts.    
- **Mismatch Afhandeling**: Bij een mismatch kijkt de algoritme naar het karakter net _achter_ het patroon in de tekst:
    - **Karakter niet in patroon**: Als dit karakter helemaal niet voorkomt in het patroon, schuiven we het patroon verder voorbij dit karakter. Dit kan een grote sprong betekenen.
    - **Karakter wel in patroon**: Als het karakter wél in het patroon voorkomt, verschuift Quicksearch het patroon zodanig dat dit karakter in de tekst gelijkkomt met de laatste overeenkomstige positie in het patroon. Zo bespaart het algoritme tijd door onnodige posities over te slaan.

modulo in slides is om index out of bounds te vermijden
# Knuth-Morris-Pratt Algoritme