## CMake build file for the hello application.
##
## This will build the application itself and its test suite. Compiled binaries
## will be written to build/${CMAKE_BUILD_TYPE}.
##
cmake_minimum_required(VERSION 2.8.12)
project(hello)


# The remote build directory must be visible on the local machine for debugging
# purposes, but must not be the same directory CLion uses to run CMake locally,
# e.g. `cmake-build-debug`. The CLion directory should be ignored in this case;
# only the remote build directory matters.

if(NOT DEFINED CMAKE_BUILD_TYPE)
    # If no build type was specified, presume that the current build directory
    # is named after the build type, e.g. ../Debug.
    get_filename_component(CMAKE_BUILD_TYPE ${CMAKE_BINARY_DIR} NAME)
endif()
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/${CMAKE_BUILD_TYPE})

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
