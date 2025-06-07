#!/usr/bin/env python3
import sys 

current_category = None
count = 0

for line in sys.stdin:
 category, val = line.strip().split('\t')
 val = int(val)
 if current_category == category:
  count +=val
 else:
  if current_category:
   print(f"{current_category}\t{count}")
  current_category = category
  count = val

if current_category:
 print(f"{current_category}\t{count}") 
