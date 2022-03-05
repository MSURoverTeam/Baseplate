PYTHONPATH = PYTHONPATH=./
PYTHON = $(PYTHONPATH) python3

_SETUP = set -e ; source /opt/ros/noetic/setup.bash ; source setup.sh ; source scripts/_base.sh

.PHONY: run-script help
SHELL = bash

BUILD_TYPE = Release
catkin_build:  ## Сбилдить пакет
	{ \
	$(_SETUP) ;\
	warning "Build type - $(BUILD_TYPE)\n" ;\
	catkin_make --source pkg -DCMAKE_BUILD_TYPE=$(BUILD_TYPE) --pkg=brain ;\
	}

run-script:  ## Запустить скрипты
	${PYTHON} -m scripts

help:  ## Показать это сообщение
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
