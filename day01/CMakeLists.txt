add_executable(day01 main.cpp)
add_custom_target(day01_python
    COMMAND ${CMAKE_COMMAND} -E chdir ${CMAKE_CURRENT_SOURCE_DIR}
    ${Python3_EXECUTABLE} go.py
    SOURCES go.py)
