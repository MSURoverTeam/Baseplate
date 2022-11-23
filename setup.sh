export ROVER_PROJECT_ROOT=$(git rev-parse --show-toplevel)
export ROVER_DIR="${1:-/opt/rover}"
export ROVER_SCRIPTS_ROOT=${ROVER_PROJECT_ROOT}/scripts
export ROVER_CONFIG_ROOT=${ROVER_PROJECT_ROOT}/pkg/brain/config

export PROJECT_ROOT=${ROVER_PROJECT_ROOT}

echo "Root is - ${ROVER_PROJECT_ROOT}"

export PYTHONPATH=${PYTHONPATH}:${ROVER_PROJECT_ROOT}:${ROVER_SCRIPTS_ROOT}

pushd .
cd $ROVER_PROJECT_ROOT

source ./devel/setup.bash
source /usr/share/gazebo/setup.bash

ln -sfn $(dirname ${ROS_ROOT})/catkin/cmake/toplevel.cmake ./pkg/CMakeLists.txt

popd

function build_model() {( set -e
    cd $ROVER_PROJECT_ROOT

    model=${1:-rover}
    echo "Building model ${model}"
    xacro ${ROVER_PROJECT_ROOT}/models/${model}/model.xacro > ${ROVER_PROJECT_ROOT}/models/${model}/model.urdf

    if [[ "$model" == "rover" ]]; then
        echo "Running jsonnet for configs"
        jsonnet --jpath ${ROVER_CONFIG_ROOT} -S ${ROVER_CONFIG_ROOT}/rover_control.jsonnet -o ${ROVER_CONFIG_ROOT}/rover_control.yaml
    fi
)}

function link_model() {
    ln -s ${ROVER_PROJECT_ROOT}/models/$1 ~/.gazebo/models/$1
    ln -s ${ROVER_PROJECT_ROOT}/models/$1 /opt/rover/$1
}

function check_rover() {
    check_urdf ${ROVER_PROJECT_ROOT}/models/rover/model.urdf
}

function launch_brain() {
    launch_file="${1}"
    model="${2:-/opt/rover/rover/model.urdf}"
    echo "Launching with $launch_file and $model"

    NO_AT_BRIDGE=1 roslaunch brain ${launch_file} model:=${model}
}

function run_sim() {
    launch_brain gazebo.launch
}

function run_rviz() {
    launch_brain rviz.launch
}

function easy_sim() {( set -e
    build_model rover
    run_sim
)}

function easy_run() {( set -e
    make catkin_build
    rosrun brain control
)}

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
