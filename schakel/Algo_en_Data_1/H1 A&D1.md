Voornamelijk gaan we worst-case en best-case bestuderen, average-case is vaak moeilijk te bepalen, amortised gaan we pas in A&D2 zien


Grootte ordes

| $log(n)$ | $\sqrt{n}$ | $n$ | $n.log(n)$ | $n²$ | $n³$ | $2^n$ | $n!$ |
| -------- | ---------- | --- | ---------- | ---- | ---- | ----- | ---- |

Grafiek in gedachten houden:
![[bigOgraph.png]]

# Grote Theta
$$ Θ(g(n)) = \{{ f | ∃ c1, c2 > 0, n0 ≥ 0 : ∀ n ≥ n0 : 0 ≤ c1.g(n) ≤ f(n) ≤ c2.g(n) }\} $$ Functie tussen twee veelvouden van  g(n) sandwichen

# Grote O
Definitie:
$$ O(g(n)) = \{{ f | ∃ c, n0 ≥ 0 : ∀ n ≥ n0 : 0 ≤ f(n) ≤ c g(n) }\} $$
Functie onder een veelvoud van g(n) begrenzen, om worst-case gedrag te bestuderen
# Grote Omega
Definitie:
$$ Ω(g(n)) = \{{ f | ∃ c, n0 ≥ 0 : ∀ n ≥ n0 : 0 ≤ c g(n) ≤ f(n) }\} $$
Functie boven een veelvoud van g(n) begrenzen, om best-case gedrag te bestuderen

# Eigenschappen

- Voor alle functies f en g geldt:
$$ f ∈ Θ(g) \Leftrightarrow f ∈ Ω(g) \ en \ f ∈ O(g) $$
- Enkel dominante termen tellen mee:
$$ O( t1(n) + t2(n) ) = O (max(t1(n), t2(n))) $$ $$ Ω( t1(n) + t2(n) ) = Ω (min(t1(n), t2(n)))$$ waarbij: $1 < log(n) < √n < n < n.log(n) < nk-1 < nk < 2n < n!$

- $O(c.f) = O(f)$ voor alle constanten c


# Geheugengebruik
O(1): in-place
