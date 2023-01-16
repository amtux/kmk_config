#!/usr/bin/env bash

set -eu

LEFT=/Volumes/CIRCUITPYL
RIGHT=/Volumes/CIRCUITPYR

work=0
for vol in $LEFT $RIGHT; do
    if [ -d "$vol" ]; then
      work=1
      echo "$vol exists..writing to it"
      cp -i {kb,boot,main}.py "$vol/"
    fi
done

[ $work -eq 0 ] && echo "No volumes found"
