# RMF Template
The purpose of this repository is to give a solid starting point to those looking at integrating RMF into their own environments.

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
Choose a name for your project
```sh
export NEW_PRJ_NAME="wh_example"
```

Create and navigate to your ROS2 workspace
```sh
git clone git@github.com:JosiahBLB/rmf_template.git ~/projects/"$NEW_PRJ_NAME"_ws
cd ~/projects/"$NEW_PRJ_NAME"_ws
```

Initialize and download the submodules
```sh
git submodule update --init --recursive
```

Rename the project
```sh
# replace all occurances of "prj_name" inside file contents
grep -rl prj_name src | xargs sed -i "s/prj_name/$NEW_PRJ_NAME/g"

# replace all occurances of "prj_name" in files and folder names
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

Launch the example world
```sh
ros2 launch "$NEW_PRJ_NAME"_gz_classic simple_warehouse.launch.xml
```