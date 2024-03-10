cmake_minimum_required(VERSION 3.8)
project(fyp_maps)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  maps/
  DESTINATION share/${PROJECT_NAME}
)

file(GLOB_RECURSE traffic_editor_paths "maps/*.building.yaml")

foreach(path ${traffic_editor_paths})

  # Get the output world name
  string(REGEX REPLACE "\\.[^.]*\.[^.]*$" "" no_extension_path ${path})
  string(REGEX MATCH "[^\/]+$" world_name  ${no_extension_path})

  set(map_path ${path})
  set(output_world_name ${world_name})
  set(output_dir ${CMAKE_CURRENT_BINARY_DIR}/maps/${output_world_name})
  set(output_world_path ${output_dir}/${output_world_name}.world)
  set(output_model_dir ${output_dir}/models)

  ##############################################################################
  # Generate Gz world and download Models
  ##############################################################################

  message("BUILDING WORLDFILE WITH COMMAND: ros2 run rmf_building_map_tools building_map_generator gazebo ${map_path} ${output_world_path} ${output_model_dir}")
  if (NO_DOWNLOAD_MODELS)
    add_custom_command(
      DEPENDS ${map_path}
      COMMAND ros2 run rmf_building_map_tools building_map_generator gazebo ${map_path} ${output_world_path} ${output_model_dir}
      OUTPUT ${output_world_path}
    )

    # TODO: Add the else statement to specify custom models
  else()
    message("DOWNLOADING MODELS WITH COMMAND: ros2 run rmf_building_map_tools building_map_model_downloader ${map_path}")
    add_custom_command(
      DEPENDS ${map_path}
      COMMAND ros2 run rmf_building_map_tools building_map_generator gazebo ${map_path} ${output_world_path} ${output_model_dir}

      # NOTE: models are being downloaded to ~/.gazebo/models
      COMMAND ros2 run rmf_building_map_tools building_map_model_downloader ${map_path} -e ~/.gazebo/models
      OUTPUT ${output_world_path}
    )
  endif()

  ##############################################################################
  # generate the navmesh and required files for crowd simulation for gz
  ##############################################################################

  # set(crowd_sim_config_resource ${output_dir}/config_resource/)
  #
  # add_custom_command(
  #   OUTPUT ${world_name}_crowdsim
  #   COMMAND ros2 run rmf_building_map_tools building_crowdsim ${map_path} ${crowd_sim_config_resource} ${output_world_path}
  #   DEPENDS ${output_world_path}
  # )
  #
  # # This will initiate both custom commands: ${output_world_path} and ${world_name}_crowdsim
  # add_custom_target(generate_${world_name}_crowdsim ALL
  #   DEPENDS ${world_name}_crowdsim
  # )

  ##############################################################################
  ## Ign worlds
  ##############################################################################

  # generate Ignition simulation world
  set(ign_output_dir ${CMAKE_CURRENT_BINARY_DIR}/maps/${output_world_name}_ign)
  set(ign_output_world_path ${ign_output_dir}/${output_world_name}.world)
  set(ign_output_model_dir ${ign_output_dir}/models)

  add_custom_command(
    OUTPUT ${ign_output_world_path}
    COMMAND ros2 run rmf_building_map_tools building_map_generator ignition ${map_path} ${ign_output_world_path} ${ign_output_model_dir}
    DEPENDS ${map_path}
  )


  ##############################################################################
  # generate the navmesh and required files for crowd simulation for ign
  ##############################################################################

  # add_custom_command(
  #   OUTPUT ${world_name}_crowdsim_ign
  #   COMMAND ros2 run rmf_building_map_tools building_crowdsim ${map_path} ${crowd_sim_config_resource} ${ign_output_world_path}
  #   DEPENDS ${ign_output_world_path}
  # )
  #
  # # This will initiate both custom commands: ${ign_output_world_path} and  ${world_name}_crowdsim_ign
  # add_custom_target(generate_${world_name}_crowdsim_ign ALL
  #   DEPENDS ${world_name}_crowdsim_ign
  # )
  #
  # install(
  #   DIRECTORY ${ign_output_dir}
  #   DESTINATION share/${PROJECT_NAME}/maps
  # )

  ##############################################################################
  # Generate the nav graphs
  ##############################################################################

  set(output_nav_graphs_dir ${output_dir}/nav_graphs/)
  set(output_nav_graphs_phony ${output_nav_graphs_dir}/phony)
  message("GENERATING NAV GRAPHS WITH COMMAND: ros2 run rmf_building_map_tools building_map_generator nav ${map_path} ${output_nav_graphs_dir}")
  add_custom_command(
    OUTPUT ${output_nav_graphs_phony}
    COMMAND ros2 run rmf_building_map_tools building_map_generator nav ${map_path} ${output_nav_graphs_dir}
    DEPENDS ${map_path}
  )

  add_custom_target(generate_${output_world_name}_nav_graphs ALL
    DEPENDS ${output_nav_graphs_phony}
  )

  install(
    DIRECTORY ${output_dir}
    DESTINATION share/${PROJECT_NAME}/maps
  )

endforeach()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
