cmake_minimum_required(VERSION 3.11)
project(mba VERSION 0.9.1 LANGUAGES C)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(DEFAULT_BUILD_TYPE "Debug")

if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  message(STATUS "Setting build type to '${DEFAULT_BUILD_TYPE}' as none was specified.")
  set(CMAKE_BUILD_TYPE "${DEFAULT_BUILD_TYPE}" CACHE STRING "Choose the type of build." FORCE)
  # Set the possible values of build type for cmake-gui
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
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

add_library(${PROJECT_NAME} STATIC ${SOURCE_FILES})
add_library(${PROJECT_NAME}-shared SHARED ${SOURCE_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME mba CLEAN_DIRECT_OUTPUT 1)
set_target_properties(${PROJECT_NAME}-shared PROPERTIES OUTPUT_NAME mba CLEAN_DIRECT_OUTPUT 1)
set_property(TARGET ${PROJECT_NAME} PROPERTY POSITION_INDEPENDENT_CODE ON)
set_property(TARGET ${PROJECT_NAME}-shared PROPERTY POSITION_INDEPENDENT_CODE ON)

target_include_directories(${PROJECT_NAME} PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
    PRIVATE src)
