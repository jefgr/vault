
Iteratief process: op voorhand bepaalde hoeveelheid geheugen
Recursief process: niet op voorhand bepaalde hoeveelheid geheugen

> Recursieve procedures genereren ofwel een recursief proces (a.k.a. constructieve recursie) ofwel een iteratief proces (a.k.a. staartrecursie).
> Een iteratief proces is een proces waarvan je de “toestand” met een op voorhand gekende eindige hoeveelheid geheugen kan voorstellen.

Proces =/= Procedure

Een recursive procedure kan een iteratief proces genereren door gebruik te maken van tail-call optimisation: 
> Tail-call-optimalisatie is een techniek in programmeertalen waarmee een functie die zichzelf aan het einde van zijn uitvoering (in de "tail position") aanroept, efficiënter uitgevoerd kan worden. Hierbij wordt de oproep van de huidige functie "vervangen" door de nieuwe oproep, waardoor er geen nieuwe stack frame nodig is. Dit bespaart geheugen en voorkomt een overflow van de stack bij diepe of oneindige recursies.

