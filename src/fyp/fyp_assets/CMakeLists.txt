cmake_minimum_required(VERSION 3.5)
project(fyp_assets)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY models
  DESTINATION share/${PROJECT_NAME}
)

# Add models to the user's gazebo model path
install(
  DIRECTORY models
  DESTINATION $ENV{HOME}/.gazebo
)

# Add models to the user's gazebo model path
# NOTE: This is not available in later ros2 versions
ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env_hook/add_models_dir_to_gazebo_path.sh.in")

ament_package()