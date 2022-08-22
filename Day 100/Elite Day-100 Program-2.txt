Govind is playing with words, He find that few words have the same pattern
like the following: abc <-> bcd <-> .. <-> mno <-> pqr <->..<-> xyz

The pattern is formed by shifting each letter by either adding or subtracting 'i' 
in alphabetic order either in forwarding direction or backward.

e.g.: letters of 'abc' can be shift by 12-positions forward to match with 'mno'
and letters of 'mno' can be shift by 12-positions backword to match with 'abc'.

He is given a list of space-separated strings, words[].
Your task is to help him to form the word-groups having the same pattern.

NOTE: 
------
	- word-groups should be formed as per input order 
	and each group should be a sorted word-group.
	- shifting of letters can be circular in thier ASCII order like as follows:
		abc..yz
	e.g.: (abc, yza, zab) can form word-group like - [[abc, yza, zab]]

Input Format:
-------------
A single line Space separated strings, words[]

Output Format
--------------
Print the output, as described in the samples below.


Sample Input-1:
--------------
abc bcd acef xyz az ba

Sample Output-1:
-----------------
[[abc, bcd, xyz], [acef], [az, ba]]


Sample Input-2:
--------------
yurp qmjh gdba jfca

Sample Output-2:
----------------
[[jfca, qmjh, yurp], [gdba]]


Sample Input-3:
----------------
abc xyz yza zbc yab acd

Sample Output-3:
------------------
[[abc, xyz, yza], [acd, yab, zbc]]
