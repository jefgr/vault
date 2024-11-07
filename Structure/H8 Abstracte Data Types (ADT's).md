In [[R7RS]] (niet in R5RS)

# Name clashes
oplossingen:
```scheme
only
prefix
except
rename
```

# Proceduretypes


# ADT
> Abstract Datatype bestaat uit een _naam voor een datatype_ en een _reeks proceduretypes_

## Voordelen
- domeinspecifiek (leesbaarder voor jezelf en domeinexperten)
- van data representatie wisselen zonder effect
- kan van implementatie wisselen zonder operaties andere functionaliteit te geven
# Set
Vergelijkbaar met wiskundig concept verzameling. Dus elementen komen max 1 keer voor.
intersection en union hebben timecomplexity O(n.m) bij ongesorteerde lijsten
