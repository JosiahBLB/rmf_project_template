cmake_minimum_required(VERSION 3.5)
project(prj_name_assets)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY models
  DESTINATION share/${PROJECT_NAME}
)

# Make assets available to the traffic editor
install(
  DIRECTORY assets
  DESTINATION ${CMAKE_INSTALL_PREFIX}/../rmf_traffic_editor_assets/share
)

ament_package()