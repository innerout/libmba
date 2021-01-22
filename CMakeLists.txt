cmake_minimum_required(VERSION 3.11)
project(mba VERSION 0.9.1 LANGUAGES C)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
option(BUILD_SHARED_LIBS
       "Build shared libraries (.dll/.so) instead of static ones (.lib/.a)" OFF)

# Set a default build type if none was specified
set(default_build_type "Release")
if(EXISTS "${CMAKE_SOURCE_DIR}/.git")
  set(default_build_type "Debug")
endif()

if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  message(
    STATUS
      "Setting build type to '${default_build_type}' as none was specified.")
  set(CMAKE_BUILD_TYPE
      "${default_build_type}"
      CACHE STRING "Choose the type of build." FORCE)
  # Set the possible values of build type for cmake-gui
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release"
                                               "MinSizeRel" "RelWithDebInfo")
endif()

include(GNUInstallDirs)

set(
  SOURCE_FILES
  src/allocator.c
  src/bitset.c
  src/cfg.c
  src/csv.c
  src/daemon.c
  src/dbug.c
  src/diff.c
  src/eval.c
  src/hashmap.c
  src/hexdump.c
  src/linkedlist.c
  src/misc.c
  src/msgno.c
  src/path.c
  src/pool.c
  src/shellout.c
  src/stack.c
  src/suba.c
  src/svcond.c
  src/svsem.c
  src/text.c
  src/time.c
  src/varray.c
)

add_library(${PROJECT_NAME} ${SOURCE_FILES})
target_include_directories(${PROJECT_NAME} PRIVATE include)
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME mba CLEAN_DIRECT_OUTPUT 1)
set_property(TARGET ${PROJECT_NAME} PROPERTY POSITION_INDEPENDENT_CODE ON)

target_include_directories(
  ${PROJECT_NAME} PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
  PRIVATE src
)

install(
  TARGETS ${PROJECT_NAME} EXPORT mba
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${PROJECT_NAME})

install(EXPORT ${PROJECT_NAME} DESTINATION share/${PROJECT_NAME}/cmake)


export(TARGETS ${PROJECT_NAME} FILE ${PROJECT_NAME}.cmake)
