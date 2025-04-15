# This example toolchain file describes the cross compiler to use for
# the target architecture indicated in the configuration file.

# Basic cross system configuration
SET(CMAKE_SYSTEM_NAME           Linux)
SET(CMAKE_SYSTEM_VERSION        1)
SET(CMAKE_SYSTEM_PROCESSOR      arm)

# Specify the cross compiler executables
# Typically these would be installed in a home directory or somewhere
# in /opt.  However in this example the system compiler is used.
# SET(CMAKE_C_COMPILER            "/home/dulguun/cfs/buildroot/output/host/bin/arm-buildroot-linux-gnueabihf-gcc")
# SET(CMAKE_CXX_COMPILER          "/home/dulguun/cfs/buildroot/output/host/bin/arm-buildroot-linux-gnueabihf-g++")


# Check if we are cross-compiling for the ARM target
IF(CMAKE_SYSTEM_PROCESSOR MATCHES "arm")
    # Use the ARM cross-compilation toolchain
    SET(CMAKE_C_COMPILER "/home/dulguun/cfs/buildroot/output/host/bin/arm-buildroot-linux-gnueabihf-gcc")
    SET(CMAKE_CXX_COMPILER "/home/dulguun/cfs/buildroot/output/host/bin/arm-buildroot-linux-gnueabihf-g++")
ELSE()
    # Use the host compiler for Lua and other host-specific code
    FIND_PACKAGE(Lua REQUIRED)
    SET(CMAKE_C_COMPILER "/usr/bin/gcc")
    SET(CMAKE_CXX_COMPILER "/usr/bin/g++")
ENDIF()


# Override for EDS tool (force using host's x86 toolchain)
if(NOT TARGET_EDS_TOOL)
    SET(CMAKE_C_COMPILER            "/usr/bin/gcc")
    SET(CMAKE_CXX_COMPILER          "/usr/bin/g++")
endif()

# Configure the find commands
SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM   NEVER)
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY   NEVER)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE   NEVER)

# These variable settings are specific to cFE/OSAL and determines which 
# abstraction layers are built when using this toolchain
SET(CFE_SYSTEM_PSPNAME      "pc-linux")
SET(OSAL_SYSTEM_BSPNAME     "pc-linux")
SET(OSAL_SYSTEM_OSTYPE      "posix")

