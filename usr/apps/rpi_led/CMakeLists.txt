cmake_minimum_required(VERSION 2.6.4)
project(CFS_RPI_LED C)

include_directories(fsw/mission_inc)
include_directories(fsw/platform_inc)
include_directories(fsw/src)
include_directories(${app_c_fw_MISSION_DIR}/fsw/app_inc)
include_directories(${app_c_fw_MISSION_DIR}/fsw/platform_inc)
include_directories(${app_c_fw_MISSION_DIR}/fsw/mission_inc)
include_directories(${rpi_iolib_MISSION_DIR}/src)

aux_source_directory(fsw/src APP_SRC_FILES)

# Create the app module
add_cfe_app(rpi_led ${APP_SRC_FILES})
