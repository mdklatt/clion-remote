add_subdirectory(lib/gtest EXCLUDE_FROM_ALL)

add_executable(test_hello
    test_greeting.cpp
    $<TARGET_OBJECTS:greeting>
)

target_link_libraries(test_hello
    gtest
    gtest_main
)
