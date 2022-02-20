USER="sentry"
REMOTE_IP="192.168.1.98"
HOST_PATH="/home/erik/personal-dev/BikeSentry-ROS-Jetson/"
REMOTE_PATH="/home/sentry/catkin_ws/src/BikeSentry-ROS-Jetson/"
rsync -arvz -e 'ssh' --progress --delete $HOST_PATH $USER@$REMOTE_IP:$REMOTE_PATH
rsync -arvz -e 'ssh' --progress ~/.ssh/ $USER@$REMOTE_IP:~/.ssh/  