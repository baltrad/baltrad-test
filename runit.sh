#!/bin/sh

for item in 1 2 3 4 5 6 7 8 9 10; do
  echo "RUNNING $item"
  ./clean_bdb.sh >> /dev/null 2>&1
  python TestSeveralMatchingCriterias.py >> /dev/null 2>&1
done

