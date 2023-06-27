FROM ubuntu:kinetic

RUN apt update -y && apt install gcc-mingw-w64 -y
RUN apt install make nasm -y
RUN x86_64-w64-mingw32-gcc -v

RUN mkdir /work
WORKDIR /work
