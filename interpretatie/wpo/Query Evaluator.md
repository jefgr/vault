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
(assert! (rule (selection (?first . ?rest) (?first2 . ?rest2))
               (selection (?first . ?rest) ?rest2)))
```