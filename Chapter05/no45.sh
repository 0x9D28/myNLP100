#!bin/sh
sort out45.txt | uniq -c | sort -rn > sort_freq45.txt
grep -E 'する|見る|与える' sort_freq45.txt > extract_sort_freq45.txt