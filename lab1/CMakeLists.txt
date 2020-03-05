cmake_minimum_required(VERSION 3.12)
project(lab1)

set(CMAKE_CXX_STANDARD 11)
set(python36_32 C:/Users/Agnieszka/AppData/Local/Programs/Python/Python36-32/include)
set(python37_64  C:/Users/Agnieszka/AppData/Local/Programs/Python/Python37/include)
set(python36lib C:/Users/Agnieszka/AppData/Local/Programs/Python/Python36-32/libs/python36.lib)
set(python37lib C:/Users/Agnieszka/AppData/Local/Programs/Python/Python37/libs/python37.lib)
set(python37numpy C:/Users/Agnieszka/AppData/Local/Programs/Python/Python37/Lib/site-packages/numpy/core/include)
add_executable(ex1 ex1and2.cpp JSONparser.h JSONparser.cpp)
add_executable(ex3 ex3.cpp JSONparser.h JSONparser.cpp)
add_executable(ex4 ex4.cpp JSONparser.h JSONparser.cpp)

# Matplotlib
#find_package(PythonInterp   3.7     REQUIRED)
find_package(PythonLibs REQUIRED)
target_include_directories(ex4 PRIVATE ${python36_32} )
target_link_libraries(ex4 PRIVATE ${python36lib})