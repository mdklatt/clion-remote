/**
 * Unit tests for greeting.cpp.
 *
 * Link with the gtest_main library to create a command-line application that
 * will run all tests and report the results.
 */
#include <string>
#include "gtest/gtest.h"


/**
 * Test the greeting() function.
 * 
 */
TEST(test_clion-remote, greeting) {
    extern std::string greeting();
    ASSERT_EQ("Hello, World.", greeting());
    return;
}
