#!/bin/bash
docker run --rm -ti -v `pwd`:/work mingw:latest make
./extract.sh
rm ../hook.bin
cp hook.bin ../hook.bin
nim c -d:release -d=mingw -d:noRes ../BlockDll.nim
echo "Done !"
