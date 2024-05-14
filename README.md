# RMF Project Template
The purpose of this repository is to give a solid starting point to those looking at integrating RMF into their own environments.

## Dependencies
This project requires that you are running Ubuntu 22.04 and ROS2 Humble Hawksbill.
See the [ROS2 Humble Hawksbill installation guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).

> :warning: WARNING
> In the ROS2 installation instructions there is a choice between `ros-humble-desktop` and `ros-humble-ros-base`. However, you **MUST** install both for this package to work


### Other Dependencies
```sh
sudo apt install rename
```

## Setup
Choose a name for your project
```sh
export PRJ="wh_example"
```

Create and navigate to your ROS2 workspace
```sh
git clone git@github.com:JosiahBLB/rmf_template.git ~/projects/"$PRJ"_ws
cd ~/projects/"$PRJ"_ws
```

Initialize and download the submodules
```sh
git submodule update --init --recursive
```

Rename the project
```sh
# replace all occurances of "prj_name" inside file contents
grep -rl prj_name src | xargs sed -i "s/prj_name/$PRJ/g"

# replace all occurances of "prj_name" in files and folder names
find src -name '*prj_name*' -execdir rename 's/prj_name/'"$PRJ"'/' '{}' \+
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
ros2 launch "$PRJ"_gz_classic simple_warehouse.launch.xml
```

# Getting Started

Once you have confirmed the project can run, it is then time to start configuring your new project to suit your specific implementation.

> :memo: REMEMBER
> To get access to the environment variables specific to your ROS2 workstation you must source your terminal by running `source install/setup.bash` or `source install/setup.<your_shell>`. See the `install` directory for supported shells.

## Step 1: Adding Assets
Models can be added to the `src/"$PRJ"/"$PRJ"_assets/models` directory. This directory is added to the `$GAZEBO_MODEL_PATH` environment variable when the simulation is launched. To use these in `traffic_editor` we must add a thumbnail with the models name and add it to the `model_list.yaml` file.

## Step 2: Designing your World in Traffic Editor
Although the RMF documentation is generally outdated, using [this](https://osrf.github.io/ros2multirobotbook/traffic-editor.html) page will get you started. However, if you are impatient like me, here are a few basic steps to get down a working solution:

1. Run `source install/setup.bash; traffic_editor`
2. Click: <ins>B</ins>uilding $\rightarrow$ <ins>N</ins>ew
3. Save your map under `src/"$PRJ"/"$PRJ"_maps/maps/<your_map_name>/<your_map_name>.building.yaml`
4. Ensure to check `Reference-image coordinates` when the option pops up
5. Save a floor plan `.png` image in the same location, named `<your_map_name>.png`
6. Click `Add` on the right-hand side under the `levels` tab and name it `L1` for level 1 and add your reference image
7. Click the pink line tool or press `T` to add a reference measurement to your map
8. Click Select or press `Esc` and then click this line to open its properties where you can define its length
9. IMPORTANT: Save, close and re-open to complete the coordinate transform

From this point you can start to build your world using:
- Draw <ins>W</ins>alls (press `Esc` to stop drawing)
- Add <ins>F</ins>loor Polygon (`right-click` to close polygon)
- Add <ins>L</ins>ine (press `Esc` to stop drawing)
- Select (`Esc`): Select components to give them additional parameters i.e. for nodes: pickup, drop-off, charging station etc.

## Step 3: Fleet Configuration
The next stage is to add your fleet configuration files in `src/"$PRJ"/config/<your_map_name>` which describe the parameters and capabilities of the robots in each fleet. Another step is to configure the fleet adapter to your fleet managers API, which the `fleet_adapter.py` is already configured for the RMF supplied robots and can be used straight away.

## Step 4: Launch Files
The `CMakeLists.txt` file found in packages often installs files at build-time allowing for users to execute custom launch files. We have already done this at the start! We launched the `simple_warehouse` using:
```sh
ros2 launch "$PRJ"_gz_classic simple_warehouse.launch.xml
```

There are a number of launch files that are required, one in `src/"$PRJ"/launch/<your_map_name>.launch.xml` which is executed by another found in `src/"$PRJ"_gz_classic/launch/<your_map_name>.launch.xml`. You will find that each of these both call a common launch file, which runs all the basic RMF and Gazebo functionality. It is useful to know that runtime environment variables are also set within these launch files such as the previously mentioned `$GAZEBO_MODEL_PATH`.
