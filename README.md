# MSU Rover

## Пошаговая настройка

1. `sudo apt install ros-noetic-velocity-controllers ros-noetic-gazebo-plugins ros-noetic-ros-controllers`
2. `python3 -m pip install click inquirer colorama`
3. `make catkin_build`
4. `source setup.sh`
5. Инициализация рабочего пространства
    - `make run-script`
    - `dev` -> `init.sh`

Такой длинной является только первоначальная настройка. В дальнейшем, чтобы опять начать работать с симулляцией, надо будет выполнить только `source setup.sh`.

В правильно настроенном рабочем пространстве доступны команды:

- `run_sim` - запуск симулляции газебо с моделью ровера и топиками управления
- `check_rover` - валидирует urdf-файл модели ровера
- `link_model $ARG1` - добавляет модели из папки models в газебо, ARG1 - название папки
- `rover_stop` - отправляет все нули в /cmd_vel

Кроме того, с помощью `make run-script` доступно меню выполнения утилит из папки [scripts](https://github.com/MSURoverTeam/Baseplate/tree/master/scripts). Там можно добавлять и свои python или sh скрипты - [пример для sh](https://github.com/MSURoverTeam/Baseplate/blob/master/scripts/dev/example.sh), аналогично для python (только без `source .../_base.sh`).

**TL;DR** чтобы запустить симуляцию (после выполненной настройки) - `source setup.sh; run_sim`.

## Зависимости

Установленные ROS **Noetic** и Gazebo (full-desktop-install).

**Apt** (`sudo apt install ...`):

- ros-noetic-velocity-controllers
- ros-noetic-gazebo-plugins
- ros-noetic-ros-controllers

**Python** (`pip install ...`):

- click
- inquirer
- colorama
