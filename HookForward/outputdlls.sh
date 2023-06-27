#!/bin/bash

cat dlls.txt | grep -E "\w" | grep -v "#" | sed 's/^\(.*\)$/"\0",/g'
