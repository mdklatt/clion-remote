cmake_minimum_required(VERSION 3.8)
project(hello
    LANGUAGES CXX
)

add_library(greeting OBJECT
    src/greeting.cpp
)

add_executable(${PROJECT_NAME}
    src/main.cpp
    $<TARGET_OBJECTS:greeting>
)

target_compile_options(${PROJECT_NAME}
PRIVATE
    -Wall
    $<$<CXX_COMPILER_ID:GNU>:-pedantic>
)

add_subdirectory(test)
