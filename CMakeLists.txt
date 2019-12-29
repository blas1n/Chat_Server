cmake_minimum_required (VERSION 3.8)

project (BS_Engine_Package_Server VERSION 0.0.1 LANGUAGES CXX)

set (CMAKE_CXX_STANDARD 17)
set (CMAKE_CXX_STANDARD_REQUIRED ON)
set (CMAKE_CXX_EXTENSIONS OFF)

set (FOLDER_NAME ${ARCH}-${CMAKE_BUILD_TYPE})

set (CMAKE_BINARY_DIR ${CMAKE_CURRENT_LIST_DIR}/build/${FOLDER_NAME})
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/build/${FOLDER_NAME})
set (CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/build/${FOLDER_NAME}/lib)
set (CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/build/${FOLDER_NAME}/lib)

add_subdirectory (external)

set (LIBRARY_PATH ${CMAKE_CURRENT_LIST_DIR}/external/Serv_Work/server)
include_directories (${LIBRARY_PATH}/base_library)
include_directories (${LIBRARY_PATH}/TCP)

add_subdirectory (server)