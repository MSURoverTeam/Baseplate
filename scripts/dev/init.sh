#!/usr/bin/env bash
set -e

if [ -z "${ROVER_DIR}" ]; then
    echo "Рабочее пространство не инициаизированно! Выпоните \"source setup.sh\""
    exit 1
fi

sudo mkdir ${ROVER_DIR}

if [[ ! "${ROVER_DIR}" == "/opt/rover" ]]; then
    echo "Linking ${ROVER_DIR} to /opt/rover"
    sudo ln -s ${ROVER_DIR} /opt/rover
fi

sudo chown -R $(id -u):$(id -g) ${ROVER_DIR}
sudo chown -R $(id -u):$(id -g) /opt/rover

ln -s ${ROVER_PROJECT_ROOT}/models/meshes /opt/rover/meshes

mkdir -p ~/.gazebo/models

ln -s ${ROVER_PROJECT_ROOT}/models/rover ~/.gazebo/models/rover
ln -s ${ROVER_PROJECT_ROOT}/models/rover /opt/rover/rover
