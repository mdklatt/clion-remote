## CMake build file for the hello application.
##
## This will build the application itself and its test suite. Compiled binaries
## will be written to build/${CMAKE_BUILD_TYPE}.
##
cmake_minimum_required(VERSION 3.0)
project(hello)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/${CMAKE_BUILD_TYPE})

set(SOURCE_FILES src/main.cpp src/greeting.cpp)
add_executable(${PROJECT_NAME} ${SOURCE_FILES})
add_subdirectory(test)
