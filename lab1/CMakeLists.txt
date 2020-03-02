cmake_minimum_required(VERSION 3.12)
project(lab1)

set(CMAKE_CXX_STANDARD 14)

add_executable(ex1 ex1and2.cpp JSONparser.h JSONparser.cpp)
add_executable(ex2 ex2.cpp JSONparser.h JSONparser.cpp)