# Eenvoudige Queries

```scheme
;; namen van alle planete
(is-planeet ?planeet)
;; alle manen van Jupiter
(is-maan-van ?maan Jupiter)
;; alles ontdekt door Galilei
(is-ontdekt ?lichaam ?jaar Galilei)
;; jaar dat Deimos werd ontdekt
(is-ontdekt Deimos ?jaar ?ontdekker)
;; Middellijn van Mars
(heeft-middellijn Mars ?lijn)
;; Rotatietijd van Jupiter
(heeft-rotatietijd Jupiter ?s ?tijd)
```

# Samengestelde queries

```scheme
;; afstand tot de zon van de planeet van Deimos
(and (is-maan-van Deimos ?planeet)
     (heeft-afstand-tot-zon ?planeet ?afstand))
;; de afstand tot de Zon, rotatietijd en massa van de planeet Uranus
(and (heeft-afstand-tot-zon Uranus ?afstand)
     (heeft-rotatietijd Uranus ?s ?tijd)
     (heeft-massa Uranus ?massa))
;; de namen van alle manen van Saturnus en Jupiter, samen met hun ontdekkers.
(and 
	(or (is-maan-van ?maan Saturnus)
	    (is-maan-van ?maan Jupiter))
	(is-ontdekt ?maan ?jaar ?ontdekker))
```

# Filters

```scheme
;; de namen van planeten die geen maan hebben
(and (is-planeet ?p)
     (not (is-maan-van ?maan ?p)))
;; de namen van planeten kleiner dan de Aarde
(and (is-planeet ?p)
     (heeft-middellijn ?p ?p-massa)
     (heeft-middellijn Aarde ?a-massa)
     (lisp-value < ?p-massa ?a-massa))
;; de planeet met de grootste massa
(and (is-planeet ?p)
     (heeft-massa ?p ?m)
     (not (and (is-planeet ?p2)
          (heeft-massa ?p2 ?m2)
          (lisp-value < ?m ?m2))))
;; het object (maan of planeet) met de kleinste middellijn in de databank.
(and 
     (or (is-planeet ?object)
         (is-maan-van ?object ?p))
	 (heeft-middellijn ?object ?km)
     (not (and 
               (or (is-planeet ?object2)
	                (is-maan-van ?object2 ?p2))
               (heeft-middellijn ?object2 ?km2)
               (lisp-value > ?km ?km2))))
;; de manen ontdekt voor 1700 of door Galilei
(and (is-maan-van ?maan ?p)
    (or (is-ontdekt ?maan ?jaar Galilei)
        (and (is-ontdekt ?maan ?jaar ?persoon)
             (lisp-value < ?jaar 1700))))
```

# Logische Regels

```scheme
;; een regel `(is-maan ?x)` die bepaalt of `?x` een maan is
(assert! (rule (is-maan ?x)
               (is-maan-van ?x ?p)))
;; een regel `(heeft-maan ?p)` die bepaalt of planeet `?p` (één of meerdere) manen heeft
(assert! (rule (heeft-maan ?p)
               (is-maan-van ?m ?p)))
;; een regel `(kleiner ?x ?y)` die bepaalt of `?x` een kleiner hemellichaam is dan `?y`
(assert! 
	(rule 
		(kleiner ?x ?y)
           (and
	            (or (is-planeet ?x)
                   (is-maan-van ?x ?planeetX))
	            (or (is-planeet ?y)
                    (is-maan-van ?y ?planeetY))
                (heeft-middellijn ?x ?kmX)
                (heeft-middellijn ?y ?kmY)
                (lisp-value < ?kmX ?kmY))))
```

# Logisch Programmeren

```scheme
;; Selectie
(assert! (rule (selection () ?list)))
(assert! (rule (selection (?first . ?rest) (?first . ?rest2))
               (selection ?rest ?rest2)))
(assert! (rule (selection ?selection (?first2 . ?rest2))
               (selection ?selection ?rest2)))
;; prefix
(assert! (rule (prefix () ?lijst)))
(assert! (rule (prefix (?first . ?rest) (?first . ?lijst) )
               (prefix ?rest ?lijst)))
;; postfix
(assert! (rule (postfix ?last ?last)))
(assert! (rule (postfix ?post (?rest . ?last))
               (postfix ?post ?last)))
;; sublist
(assert! (rule (prefix () ?lijst)))
(assert! (rule (prefix (?first . ?rest) (?first . ?lijst) )
               (prefix ?rest ?lijst)))
(assert! (rule (postfix ?last ?last)))
(assert! (rule (postfix ?post (?rest . ?last))
               (postfix ?post ?last)))
(assert! (rule (sublist ?sub ?lijst)
               (and (prefix ?pre ?lijst)
                    (postfix ?sub ?pre))))
;; omgekeerde

```

# Volledig Logisch Programma
```scheme
;; input
(assert! (is-kleur rood))
(assert! (is-kleur groen))
(assert! (is-kleur beige))
(assert! (is-kleur zwart))
(assert! (is-kleur geel))
(assert! (is-kleur kaki))
(assert! (is-kleur paars))
(assert! (is-kleur wit))
(assert! (kleur-heeft-helderheid rood 333))
(assert! (kleur-heeft-helderheid groen 196))
(assert! (kleur-heeft-helderheid beige 944))
(assert! (kleur-heeft-helderheid zwart 0))
(assert! (kleur-heeft-helderheid geel 833))
(assert! (kleur-heeft-helderheid kaki 856))
(assert! (kleur-heeft-helderheid paars 722))
(assert! (kleur-heeft-helderheid wit 1000))
(assert! (persoon-draagt ilse ((jurk wit) (tas zwart))))
(assert! (persoon-draagt evi ((hemd rood) (riem zwart) (broek zwart))))
(assert! (persoon-draagt jan ((hemd wit) (linkersok zwart) (rechtersok zwart))))
;; program
(assert! (rule (kleur-is-donker ?kleur)
               (and (is-kleur ?kleur)
                    (kleur-heeft-helderheid ?kleur ?helder)
                    (lisp-value < ?helder 500))))
(assert! (rule (kleur-is-licht ?kleur)
               (and (is-kleur ?kleur)
                    (not (kleur-is-donker ?kleur)))))

(assert! (rule (element ?first (?first . ?rest))))
(assert! (rule (element ?el (?first . ?rest))
               (element ?el ?rest)))
(assert! (rule (yinyang-persoon ?p)
               (and (persoon-draagt ?p ?kledij)
                    (element (?stuk-licht ?kleur-licht) ?kledij)
                    (element (?stuk-donker ?kleur-donker) ?kledij)
                    (kleur-is-licht ?kleur-licht)
                    (kleur-is-donker ?kleur-donker))))

(assert! (rule (kleur-suggestie ?kleur ?suggestie)
               (and (kleur-is-donker ?kleur)
                    (kleur-is-licht ?suggestie))))
(assert! (rule (kleur-suggestie ?kleur ?kleur)
               (kleur-is-licht ?kleur)))

(assert! (rule (suggestie-stuk (?stuk ?kleur) (?stuk ?suggestie))
                (kleur-suggestie ?kleur ?suggestie)))
(assert! (rule (suggesties (?kledij) (?suggesties))
               (suggestie-stuk ?kledij ?suggesties)))
(assert! (rule (suggesties (?car . ?kledij) (?car2 . ?suggesties))
               (and (suggestie-stuk ?car ?car2)
                    (suggesties ?kledij ?suggesties))))

(assert! (rule (lichtere-kledij-voor ?p ?suggestie)
               (and (persoon-draagt ?p ?kledij)
                    (suggesties ?kledij ?suggestie))))
```
