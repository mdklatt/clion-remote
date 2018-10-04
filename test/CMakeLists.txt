## CMake build file for the hello application test suite.
##
## This will build a Google Test test runner for all contained tests.
##
project(test_hello)

add_subdirectory(lib/gtest)

include_directories(${gtest_SOURCE_DIR} ${gtest_SOURCE_DIR}/include)

add_executable(${PROJECT_NAME}
    ${CMAKE_SOURCE_DIR}/src/greeting.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/test_greeting.cpp
)
target_link_libraries(${PROJECT_NAME}
    gtest
    gtest_main
)
