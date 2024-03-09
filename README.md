# Final Year Project

## Adding RMF as Submodules to Your Project
This was done using the `rmf_demos` repository as reference, using their `rmf.repos` file to find all the required packages for the project.
```sh
 git submodule add -b humble https://github.com/open-rmf/rmf_battery.git src
 git submodule add -b humble https://github.com/open-rmf/rmf_battery.git src/rmf/rmf_battery
 git submodule add -b humble https://github.com/open-rmf/rmf_internal_msgs.git src/rmf/rmf_internal_msgs
 git submodule add -b humble https://github.com/open-rmf/rmf_api_msgs.git src/rmf/rmf_api_msgs
 git submodule add -b humble https://github.com/open-rmf/rmf_ros2.git src/rmf/rmf_ros2
 git submodule add -b humble https://github.com/open-rmf/rmf_task.git src/rmf/rmf_task
 git submodule add -b humble https://github.com/open-rmf/rmf_traffic.git src/rmf/rmf_traffic
 git submodule add -b humble https://github.com/open-rmf/rmf_utils.git src/rmf/rmf_utils
 git submodule add -b humble https://github.com/open-rmf/ament_cmake_catch2.git src/rmf/ament_cmake_catch2
 git submodule add -b humble https://github.com/open-rmf/rmf_visualization.git src/rmf/rmf_visualization
 git submodule add -b humble https://github.com/open-rmf/rmf_visualization_msgs.git src/rmf/rmf_visualization_msgs
 git submodule add -b humble https://github.com/open-rmf/rmf_building_map_msgs.git src/rmf/rmf_building_map_msgs
 git submodule add -b humble https://github.com/open-rmf/rmf_simulation.git src/rmf/rmf_simulation
 git submodule add -b humble https://github.com/open-rmf/rmf_traffic_editor.git src/rmf/rmf_traffic_editor
 git submodule add -b humble https://github.com/open-rmf/menge_vendor.git src/thirdparty/menge_vendor
 git submodule add -b humble https://github.com/open-rmf/nlohmann_json_schema_validator_vendor.git src/thirdparty/nlohmann_json_schema_validator_vendor
 git submodule add -b humble https://github.com/open-rmf/pybind11_json_vendor.git src/thirdparty/pybind11_json_vendor
 git submodule update --init --recursive
```
