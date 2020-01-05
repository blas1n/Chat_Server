cmake_minimum_required (VERSION 3.8)

project (Chat_Server VERSION 0.0.1 LANGUAGES CXX)

set (CMAKE_CXX_STANDARD 17)
set (CMAKE_CXX_STANDARD_REQUIRED ON)
set (CMAKE_CXX_EXTENSIONS OFF)

add_subdirectory (External)
add_subdirectory (Server)