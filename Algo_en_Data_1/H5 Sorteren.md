# Terminologie

Sorteren altijd minstens Omega(n)
## Stabiliteit van Sorteeralgoritmen

> Een sorteeralgoritme heet stabiel als het de relatieve orde van velden met gelijke sleutel bewaart

## In-place-heid

> Een sorteeralgoritme heet in-place als het geen extra geheuden gebruikt buiten het geheugen reeds ingenomen door de te-sorteren data

## Interne vs Externe Sorteeralgoritmen
Zie [[Chapter 15 Extern Sort.pdf|AD3]]
# Interne Sorteeralgoritmen
## Simpele Sorteeralgoritmen
O(n²)
### Bubble Sort
### Insertion Sort
### Selection Sort
## Geavenceerde Sorteeralgoritmen
O(n.log(n))
### Merge Sort
Niet stabiel met strikte ongelijkheid, wel met niet strikte ongelijkheid (onze implementatie)
Niet in-place (hulp-vector en recursief process)
Werkt goed op lijsten
Basis van externe sorteeralgoritmen
 
### Heap Sort
Niet stabiel (geen relatie horizontaal, alleen vertikaal als voorgesteld als volledige boom)
### Quick Sort
Niet stabiel, niet in place minstens Omega(log(n)) geheugen extra nodig (recursief **proces**)
Werkt goed op dubbel gelinkte lijsten, maar niet op andere lijsten.
gebruik maken van pivot
Grote overhead dus voor kleine hoeveelheden data beter ander algo gebruiken
Alleen average case is O(n.log(n))
Kan degenereren naar O(n²) als de pivot altijd de grootste/kleinste is
Hier zijn oplossingen voor om dit zo veel mogelijk te vermijden, bvb mediaan van 3 elementen nemen
## Lineaire Sorteeralgoritmen
O(n)
Niet-Comparatief
### Bucket Sort
### Counting Sort
### Radix Sort
> Radix = Grondtal

