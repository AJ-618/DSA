# Hashing
Read, Insert and delete operations are O(1) time in hashing on average.
Second most used data-structure after array in whole of computer science.
We trade-off memory to achieve these constant time operations.

## Applications of Hashing
  - Dictonaries
  - Database Indexing
  - Cryptograhpy
  - Caches
  - Symbol tables in Compiler/Interpreters
  - Routers
  - Getting data from databases, etc.

## Direct Access Table
The whole idea of hashing is based on this simple concept to understand
direct access table. Suppose we have some numbers from the range 0 - 999,
and we want to be able to perform read, write and delete operations on
these numbers in constant time, then we can initialize an array of size
1000 with all 0's and set the value of the respective index (the number)
we want to perform an operation on to 1 in case we want to insert it, 0
in case we want to delete it and to read we can just check the value at
the respective index, whether it is 0 or 1 to see if the value is present
in the table.
 