## CMake build file for the hello application test suite.
##
## This will build a Google Test test runner for all contained tests.
##
project(test_hello)

add_subdirectory(lib/gtest)

include_directories(${gtest_SOURCE_DIR} ${gtest_SOURCE_DIR}/include)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build/${CMAKE_BUILD_TYPE})

add_executable(${PROJECT_NAME} test_greeting.cpp ../src/greeting.cpp)
target_link_libraries(${PROJECT_NAME} gtest gtest_main)
