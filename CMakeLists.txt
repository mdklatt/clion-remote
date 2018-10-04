## CMake build file for the hello application.
##
## This will build the application itself and its test suite. Compiled binaries
## will be written to build/${CMAKE_BUILD_TYPE}.
##
cmake_minimum_required(VERSION 3.4)
project(hello)


cmake_host_system_information(RESULT PROJECT_BUILD_HOST QUERY HOSTNAME)
if(NOT DEFINED CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()


if(CMAKE_COMPILER_IS_GNUCXX)
    # Set GCC-specific compiler flags.
    list(APPEND PROJECT_CXX_FLAGS_LIST
        -Wall
        -Wno-unknown-pragmas
        -Wno-format-y2k
        -Wno-multichar
        -std=c++11
    )
endif()

add_executable(${PROJECT_NAME}
    ${CMAKE_SOURCE_DIR}/src/greeting.cpp
    ${CMAKE_SOURCE_DIR}/src/main.cpp
)
add_subdirectory(test)
