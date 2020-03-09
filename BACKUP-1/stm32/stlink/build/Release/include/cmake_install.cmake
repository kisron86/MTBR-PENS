# Install script for directory: /home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/include/stlink.h")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/usr/local/include" TYPE FILE FILES "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/include/stlink/mmap.h;/usr/local/include/stlink/backend.h;/usr/local/include/stlink/sg.h;/usr/local/include/stlink/commands.h;/usr/local/include/stlink/reg.h;/usr/local/include/stlink/usb.h;/usr/local/include/stlink/flash_loader.h;/usr/local/include/stlink/chipid.h;/usr/local/include/stlink/logging.h;/usr/local/include/stlink/version.h")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/usr/local/include/stlink" TYPE FILE FILES
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink/mmap.h"
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink/backend.h"
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink/sg.h"
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink/commands.h"
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink/reg.h"
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink/usb.h"
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink/flash_loader.h"
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink/chipid.h"
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/include/stlink/logging.h"
    "/home/core/catkin_ws/src/omnirobot/src/stm32/stlink/build/Release/include/stlink/version.h"
    )
endif()

