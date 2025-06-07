#!/usr/bin/env python3
import sys
for line in sys.stdin:
 parts = line.strip().split('\t')
 if len(parts) >=1:
  print(f"{parts[0]}\t1")
