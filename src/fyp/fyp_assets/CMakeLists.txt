cmake_minimum_required(VERSION 3.5)
project(fyp_assets)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY models
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY models
  DESTINATION $ENV{HOME}/.gazebo/models
)

ament_package()
