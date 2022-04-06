# MSU Rover

Репозиторий с конфигурацией нашего ровера в gazebo. Постепенно будет обрастать функционалом (манипулятор, навигация, и пр.) и различными утилитами.

## TODO

- [x] "Центрировать" ровер
- [x] Правильные массы
- [ ] Подкрутить управление

--- БЫСТРЫЕ ЗАДАЧИ ---
- [ ] Правильные ограничения шарниров
- [ ] Упростить urdf с помощью xarco
- [ ] Удалить ненужные зависимости из brain
- [ ] Дефолтный материал ровера

## Пошаговая настройка

1. Скопировать `.env.example` -> `.env`, и (*пока пропускаем эту часть*) заполнить `.env` реальными значениями
2. `sudo apt install ros-noetic-velocity-controllers ros-noetic-gazebo-plugins ros-noetic-ros-controllers ros-noetic-ros-control jsonnet`
3. `python3 -m pip install click inquirer colorama`
4. `catkin_make --source pkg -DCMAKE_BUILD_TYPE=$(BUILD_TYPE) --pkg=brain`
5. `source setup.sh`
6. Инициализация рабочего пространства
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
