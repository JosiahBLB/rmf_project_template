# Final Year Project

## Setup
Initialise and download the submodules
```sh
 git submodule update --init --recursive
```

Build the project
```sh
colcon build --mixin release lld
```

Launch the world
```sh
ros2 launch fyp_gz_classic simple_warehouse.launch.xml
```
