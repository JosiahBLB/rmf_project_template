# Final Year Project

## Dependencies
This project requires that you are running Ubuntu 22.04 and ROS2 Humble Hawksbill.
See the [ROS2 Humble Hawksbill installation guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).

| :warning: WARNING           |
|:----------------------------|
| In the ROS2 installation instructions there is a choice between `ros-humble-desktop` and `ros-humble-ros-base`. However, you **MUST** install both for this package to work   |


### Other Dependencies
```sh
sudo apt install rename
```

## Setup
Initialize and download the submodules
```sh
 git submodule update --init --recursive
```

Choose a name for your project
```sh
export NEW_PRJ_NAME="wh_example"
```

Rename the project
```sh
# rename all occurances of "prj_name" in files
grep -rl prj_name src | xargs sed -i "s/prj_name/$NEW_PRJ_NAME/g"

# rename all files and folder names with "prj_name
find src -name '*prj_name*' -execdir rename 's/prj_name/'"$NEW_PRJ_NAME"'/' '{}' \+
```

Build the project
```sh
colcon build --mixin release lld
```

Source the project
```sh  
source install/setup.bash
```

Launch the world
```sh
ros2 launch "$NEW_PRJ_NAME"_gz_classic simple_warehouse.launch.xml
```