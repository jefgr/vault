# Oefening 2
> Zie Google drive voor excel met berekeningen en zie notities

Een onderzoeker behandelde de huid van 5 muizen met een carcinogene substantie en  
mat de concentratie van deze substantie in de lever 48 uur na de behandeling. De  
resultaten zijn (nmol/g): 6,3; 5,9; 7,0; 6,9; 5,9
a) Bereken het gemiddelde, de mediaan, de modus, de variantie en de MAD.  
b) Maak een boxplot.  

| Data:                    | 6.3  | 5.9                  | 7    | 6.9                        | 5.9  |     |
| ------------------------ | ---- | -------------------- | ---- | -------------------------- | ---- | --- |
|                          | x1   | x2                   | x3   | x4                         | x5   |     |
| Sorted Data:             | 5.9  | 5.9                  | 6.3  | 6.9                        | 7    |     |
| Afwijking van gemiddelde | -0.5 | -0.5                 | -0.1 | 0.5                        | 0.6  |     |
| kwadraad                 | 0.25 | 0.25                 | 0.01 | 0.25                       | 0.36 |     |
| ABS(xi-med)              | 0.4  | 0.4                  | 0    | 0.6                        | 0.7  |     |
|                          |      |                      |      |                            |      |     |
| Gemiddelde               | 6.4  |                      |      |                            |      |     |
| Mediaan                  | 6.3  | = x3                 |      |                            |      |     |
| Modus                    | 5.9  |                      |      |                            |      |     |
| Q1                       | 5.9  | = x1 + 0.5*(x2 - x1) |      | Waarneming: (25/100)*(5+1) |      | 1.5 |
| Q3                       | 6.95 | = x4 + 0.5*(x5 - x4) |      | Waarneming: (75/100)*(5+1) |      | 4.5 |
| variantie                | 0.28 |                      |      |                            |      |     |

c) Een zesde muis werd aan de studie toegevoegd. De concentratie voor deze muis  
was: 10,2 nmol/g. Herhaal punt a) en b) voor de 6 muizen.


| Data:                    | 6.3          | 5.9                   | 7             | 6.9                        | 5.9            | 10.2        |
| ------------------------ | ------------ | --------------------- | ------------- | -------------------------- | -------------- | ----------- |
|                          | x1           | x2                    | x3            | x4                         | x5             | x6          |
| Sorted Data:             | 5.9          | 5.9                   | 6.3           | 6.9                        | 7              | 10.2        |
| Afwijking van gemiddelde | -1.133333333 | -1.133333333          | -0.7333333333 | -0.1333333333              | -0.03333333333 | 3.166666667 |
| kwadraad                 | 1.284444444  | 1.284444444           | 0.5377777778  | 0.01777777778              | 0.001111111111 | 10.02777778 |
| ABS(xi-med)              | 0.7          | 0.7                   | 0.3           | 0.3                        | 0.4            | 3.6         |
|                          |              |                       |               |                            |                |             |
| Gemiddelde               | 7.033333333  |                       |               |                            |                |             |
| Mediaan                  | 6.6          | = x3 + 0.5 (x4 - x3)  |               |                            |                |             |
| Modus                    | 5.9          |                       |               |                            |                |             |
| Q1                       | 5.9          | = x1 + 0.75*(x2 - x1) |               | Waarneming: (25/100)*(6+1) |                | 1.75        |
| Q3                       | 7.8          | = x5 + 0.25*(x6 - x5) |               | Waarneming: (75/100)*(6+1) |                | 5.25        |
| variantie                | 2.630666667  |                       |               |                            |                |             |
| MAD                      | 0.55         |                       |               |                            |                |             |
| IQR                      | 1.9          |                       |               |                            |                |             |

# Oefening 4
> zie google drive voor excel met berekeningen

In de volgende tabel vind je de prestaties neergezet door 54 landen op de 100m sprint bij de vrouwen.

|   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
|Data|||||||||
|10.78|11|11.08|11.14|11.18|11.21|11.29|11.34|11.41|
|10.84|11|11.1|11.15|11.19|11.23|11.29|11.35|11.57|
|10.86|11.01|11.11|11.16|11.2|11.23|11.3|11.36|11.6|
|10.87|11.02|11.11|11.16|11.2|11.24|11.32|11.37|11.64|
|10.93|11.06|11.11|11.17|11.21|11.27|11.32|11.38|11.78|
|11|11.08|11.13|11.17|11.21|11.28|11.33|11.4|11.97|

|                             |         |         |
| --------------------------- | ------- | ------- |
| 54 waarnemingen             |         |         |
| Q1                          | 13.75   | 11.095  |
| Mediaan                     | 27.5    | 11.2    |
| Q3                          | 41.25   | 11.3225 |
| IQR                         | 0.2275  | 0.22    |
|                             |         |         |
| limieten voor uitschieters: |         |         |
|                             | 10.765  |         |
|                             | 11.6525 |         |
> Boxplot zie notities

# Oefening 6
> Zie notities

Een scheikundige bepaalde de pH-waarde van bepaalde oplossingen, aangemaakt door verschillende personen. Typische waarden waren: 7,43; 7,16; 7,51; etc. Zij berekende het gemiddelde en de standaardafwijking en vond: 7,373 en 0,129 voor deze pH- waarden. Nadien transformeerde zij de data door er 7 van af te trekken en nadien met 100 te vermenigvuldigen, e.g. 43, 16, 51, etc. Wat zijn nu het gemiddelde en de standaardafwijking?

> int kort 
> $\overline{x'} = 100*(\overline{x} - 7)$    
> $s'² = 100² * s²$
> $s' = 100 * s$

# Oefening 7

Vele diersoorten worden bedreigd, zo ook de walvis. Regelmatig worden er uitermate moeilijke en daarom geheel onbetrouwbare tellingen uitgevoerd. Dit leverde de volgende tabel op voor 7 soorten walvissen, gemeten in 1980. Daarnaast zijn er ruwe schattingen over de oorspronkelijke aantallen walvissen:

|   |   |   |   |
|---|---|---|---|
|Soort Walvis|Gemiddelde lengte volwassen walvis|Aantallen in 1980|Oorspronkelijke aantallen geschat|
|Gewone vinvis|28,0|145000|428000|
|Noordse vinvis|20,0|175000|210000|
|Blauwe vinvis|34,0|11000|156000|
|Dwergwalvis|23,0|9000|7500|
|Bultrug|18,0|6300|110000|
|Grijze walvis|11,5|11000|20000|
|Dwergvinvis|15,5|150000|150000|
1)  Bepaal de gemiddelde lengte van een volwassen walvis in 1980.
> 21.1	
2) Bepaal de gemiddelde lengte van de volwassen walvissen in 1980, indien er van elke soort hetzelfde aantal zou geweest zijn.
> 21.43
3) Met welke grafieken en diagrams zou je de oorspronkelijke populatie en die in 1980 weergeven?
> Staafdiagram voor absolute waarden binnen soorten, om de verhouding tussen de soorten weer te geven pie-charts.