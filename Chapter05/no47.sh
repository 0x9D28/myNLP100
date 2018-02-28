#!bin/sh
sort out47.txt | uniq -c | sort -rn > predicate-particle-freq47.txt
cut -f 1 out47.txt | sort | uniq -c | sort -rn > predicate-freq47.txt