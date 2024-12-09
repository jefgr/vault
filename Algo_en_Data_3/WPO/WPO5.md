# Exercise 1
> **See Also a-d/db/table/fixed-sized-slots/schema.rkt**
## a
What is the biggest natural number that can be stored in the nr-of- attributes field of the schema block?
> line 54: de/en-code **BYTE**
> 1 Byte so 0-255

## b
What is the maximum number of different data types that we can potentially support for the attributes described by the schema?
> momenteel 4 data types ondersteund: natural, integer, decimal, string
> line 60: de/en-code **BYTE**
> 256 opties

## c
What is the maximum size (in bytes) for any tuple field (= value of any attribute) described by the schema?
> line 66: de/en-code **BYTE**
> 255 Bytes, moet in 1 Byte ge-encodeerd worden

# 1bis
> **See Also a-d/db/table/fixed-sized-slots/schema+wpo5.rkt**
## d
$$\lfloor\frac{(blockSize - capacity - nrOfAttributes)}{2}\rfloor$$

## e
What will happen if a user tries to use a schema with more attributes than we can handle in the schema block (i.e. more than your formula for (d))?
> There will be types overwritten with size data

## f
Change the new procedure to make sure that this problem is avoided (by only accepting schemas with a number of attributes that fit).
> **See Also a-d/db/table/fixed-sized-slots/schema+wpo5.rkt**

# Exercise 2
