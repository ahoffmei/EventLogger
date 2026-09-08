cmake_minimum_required(VERSION 3.16)
project(eventLogger)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/$<CONFIGURATION>")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/$<CONFIGURATION>")

add_executable(eventLogger
    src/main.cpp
    src/eventLogging/eventLogger.cpp
)

target_include_directories(eventLogger
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        ${CMAKE_CURRENT_SOURCE_DIR}/src/eventLogging
        ${CMAKE_CURRENT_SOURCE_DIR}/src/tests
)