cmake_minimum_required(VERSION 2.8)

set(CMAKE_CXX_COMPILER mpic++)
set(CMAKE_C_COMPILER mpicc)
set(CMAKE_CXX_STANDARD 20)

project(MPI_project)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${MPI_project_SOURCE_DIR}/bin)

add_compile_options(-g -O3 -fopenmp)
add_link_options(-fopenmp)

add_executable(main main.cpp)
