Files en Blocks als abstracties voor external memory
Geen hardware simuleren
External Memory grootte ordes trager


# Byte
8 bits
waarden tussen 0 en 255
dus 256 verschillende waarden

# Byterijen
Van getal naar bytes:
modulo/delen door 256

## Big endian vs Little endian
Big endian: most significant byte op eerste/laagste geheugenadres
Little endian: least significant byte op eerste/laagste geheugenadres

Small endian most common

> Giga, Kilo,... word behandeld als gibi, kibi dus 1024MB = 1GB
# Bytevectoren
Efficiënter als vectoren er moeten bvb geen typetags

```scheme
make-bytevector
bytevector-u8-ref
bytevector-u8-set!
```
## Numbers in Bytevectoren
### Hulpprocedures om te bepalen hoeveel bytes nodig zijn voor getallen

```scheme
(define (natural-bytes nmbr)
  (exact (ceiling (log (max (+ nmbr 1) 2) 256)))) 
; +1 om randgeval 256 te vermijden, max om randgevallen 0 en 1 te vermijden

(define (integer-bytes nmbr)
  (exact (ceiling (log (max (abs (+ (* 2 nmbr) 1)) 2) 256))))
; * 2 om de extra bit voor sign in rekening te brengen
```

```scheme
; signed integers
(bytevector-sint-set! bytes indx nmbr 'big size)
(bytevector-sint-ref bytes indx 'big size)
; unsigned integers
(bytevector-uint-set! bytes indx nmbr 'big size)
(bytevector-uint-ref bytes indx 'big size)
; floating point 4 byte (float)
(bytevector-ieee-single-set! bytes indx nmbr 'big)
(bytevector-ieee-single-ref bytes indx 'big)
; floating point 8 byte (double)
(bytevector-ieee-double-set! bytes indx nmbr 'big)
(bytevector-ieee-double-ref bytes indx 'big)
```

## Strings in Bytevectoren

### Hulpprocedure om de grootste mogelijke string te bepalen voor een bepaalde hoeveelheid bytes

```scheme
(define (utf8-sentinel-for nmbr-byts)
	(define byts (make-bytevector nmbr-byts))
	(define (fill! offset rem)
		(cond ((= rem 1)
				(bytevector-u8-set! byts offset 127))
			((= rem 2)
				(bytevector-u8-set! byts offset 223)
				(bytevector-u8-set! byts (+ offset 1) 191))
			(else
				(bytevector-u8-set! byts offset 239)
				(bytevector-u8-set! byts (+ offset 1) 191)
				(bytevector-u8-set! byts (+ offset 2) 191)
				(if (> rem 3)
					(fill! (+ offset 3) (- rem 3))))))
	(fill! 0 nmbr-byts)
	(utf8->string byts))
```

> **Sentinel**
> GPT: In software development, a _sentinel_ is a special value or object used to signal the end of a data structure (like a list or stream) or to indicate a specific condition, such as an error or a "not found" result. It acts as a marker that helps control program flow by providing a clear boundary or status without causing errors or triggering unwanted behaviors.

# Geheugen
- Registers + Caches
	- Zeer duur
	- Supersnel
	- Volatiel
- Centraal Geheugen (RAM)
	- Duur
	- Snel
	- Volatiel
- Periferisch Geheugen (HDD)
	- Goedkoop
	- Traag
	- Persistent
## Geheugenhiërarchie
- Primair Geheugen
	- ex.: Registers, On-Board Cache, Centraal Geheugen
- Secundair Geheugen
	- ex.: Flash, Disk, Tapes
- Tertiair Geheugen
	- ex.: CD, racks, operators

> Focus cursus ligt op secundair geheugen, maar primair geheugen zal de plaats zijn waar de code uitgevoerd wordt

Verschil tussen de 3 lagen:
Verschil in opslagcapaciteit >3 grootteordes
Verschil in toegangstijden >5 grootteordes
Verschil in cost/byte >3 grootteordes

# Disk Abstraction
Wij behandelen een disk als een logische disk, waarin alle blokken achter elkaar liggen

```scheme
ADT disk

block-size
	number
disk-size
	number
block-ptr-size
	number
block-idx-size
	number
new
	( string -> disk )
mount
	( string -> disk )
unmount
	( disk -> ∅ )
disk?
	( any -> boolean )
name
	( disk -> string )
read-block
	( disk number -> block )
```

# Block Abstractie

```scheme
ADT block

write-block! 
	( block -> ∅ )
block?
	( any -> boolean )
disk
	( block -> disk )
position
	( block -> number )
decode-byte
	( block number -> byte )
encode-byte!
	( block number byte -> ∅ )
decode-string 
	( block number number -> string )
encode-string!
	( block number number string -> ∅ )
decode-fixed-natural
	( block number number -> natural )
encode-fixed-natural!
	( block number number natural -> ∅ )
decode-arbitrary-integer
	( block number -> integer × number )
encode-arbitrary-integer!
	( block number integer -> number )
decode-real
	( block number number -> real )
encode-real!
	( block number number real -> number )
decode-bytes
	( block bytevector number number number -> ∅ )
encode-bytes!
	( block bytevector number number number -> ∅ )
```

# Filesysteem

- **Blokpointer**: A _blokpointer_ is a metadata structure that holds pointers to data blocks, often used to locate the physical storage blocks for a file or dataset.
- **Freelist**: A _freelist_ is a list of unallocated memory or storage blocks available for new allocations in data management systems.
- **Metablok**: A _metablok_ refers to a block containing metadata that describes or organizes data structures within a file system or database.
- **File**: A _file_ is a named collection of data stored on disk that can be accessed and manipulated by a computer.
- **Directory**: A _directory_ is a file system structure that organizes and contains references to other files and directories.


Metablok gebruiken we als NULL-pointer
eerste pointer in metablok -> directory
tweede pointer in metablok -> freelist
eerste pointer in directory -> next directory
eerste pointer in freelist block -> next freelist block
