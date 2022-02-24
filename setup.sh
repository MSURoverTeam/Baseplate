export ROVER_PROJECT_ROOT=$(git rev-parse --show-toplevel)
export ROVER_DIR="${1:-/opt/rover}"
export ROVER_SCRIPTS_ROOT=${ROVER_PROJECT_ROOT}/scripts

echo "Root is - ${ROVER_PROJECT_ROOT}"

pushd .
cd $ROVER_PROJECT_ROOT

source ./devel/setup.bash
source /usr/share/gazebo/setup.bash

ln -sfn $(dirname ${ROS_ROOT})/catkin/cmake/toplevel.cmake ./pkg/CMakeLists.txt

popd

function link_model() {
    ln -s ${ROVER_PROJECT_ROOT}/models/$1 ~/.gazebo/models/$1
    ln -s ${ROVER_PROJECT_ROOT}/models/$1 /opt/rover/$1
}

function check_rover() {
    check_urdf ${ROVER_PROJECT_ROOT}/models/rover/model.urdf
}

function run_sim() {
    NO_AT_BRIDGE=1 roslaunch brain "${1:-gazebo.launch}" model:="${2:-/opt/rover/rover/model.urdf}"
}

function rover_stop() {
    rostopic pub /rover/cmd_vel geometry_msgs/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0"
}
