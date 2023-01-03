#!/usr/bin/env bash

set -eu

LEFT=/Volumes/CIRCUITPYL
RIGHT=/Volumes/CIRCUITPYR

if [ -d "$LEFT" ]; then
  echo "left exists. pushing.."
  cp -i {kb,boot,main}.py $LEFT/
fi

if [ -d "$RIGHT" ]; then
  echo "right exists. pushing.."
  cp -i {kb,boot}.py $RIGHT/
  sed "s/SplitSide.LEFT/SplitSide.RIGHT/g" main.py > .right.py
  cp -i .right.py $RIGHT/main.py
fi

echo "complete"
