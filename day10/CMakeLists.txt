add_custom_target(day10_python
    COMMAND ${CMAKE_COMMAND} -E chdir ${CMAKE_CURRENT_SOURCE_DIR}
    ${Python3_EXECUTABLE} go.py
    SOURCES go.py)
