PYTHONPATH = PYTHONPATH=./
PYTHON = $(PYTHONPATH) python3

.PHONY: setup run-script install-script-deps help
SHELL = bash

_setup:  # Утилитарная команда для настройки среды билд-тасок
	source /opt/ros/noetic/setup.bash
	source setup.sh

run-script:  ## Запустить скрипты
	${PYTHON} -m scripts

catkin_build: _setup  ## Сбилдить пакет
	catkin_make --source pkg -DCMAKE_BUILD_TYPE=Release --pkg=brain

install-script-deps:  ## Установить зависимости для запуска скриптов локально
	${PYTHON} -m pip install click inquirer colorama

help:  ## Показать это сообщение
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
