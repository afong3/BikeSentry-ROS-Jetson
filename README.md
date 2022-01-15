# README
## BikeSentryROS
### Version: ROS Melodic
### Machine OS: Ubuntu 18.04
### Python Version: Python 2.7 (works nicest with ROS melodic)
### Purpose
This repo should be placed directly into the catkin_ws/src folder of your local machine. 

### /src
Use /src to store all the code for nodes. 

### /scripts
Use /scripts to store all the libraries responsible for handling Audio, Camera, & motor instructions

### To Run the Object Detection from ros_deep_learning package
1. run 'roscore' in terminal
2. open a new terminal tab and run the command below
$roslaunch ros_deep_learning detectnet.ros1.launch input:=v4l2:///dev/video0 output:=display://0

