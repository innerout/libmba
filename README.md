libmba  
A library of generic C modules  
http://www.ioplex.com/~miallen/libmba/  

## Usage

You can include the code below in your `cmake` project and `#include <mba/relevant.h>` in your sources.

``` cmake
FetchContent_Declare(libmba # Recommendation: Stick close to the original name.
                     GIT_REPOSITORY https://github.com/innerout/libmba.c.git)
FetchContent_GetProperties(libmba)
if(NOT libmba_POPULATED)
  FetchContent_Populate(libmba)
  add_subdirectory(${libmba_SOURCE_DIR} ${libmba_BINARY_DIR})
  FetchContent_MakeAvailable(libmba)
endif()
target_link_libraries(YOUR_LIB_NAME libmba)
```


## Installation

``` bash
mkdir build;cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make install
```

