# Заметки

Разобратьс с путиями к домашней директории - сейчас приходится переключатсья между `macmini` и `igor`.

- `flatpak run com.st.STM32CubeIDE` - stm ide

---

## Настройка окружения

- `sudo apt install ros-noetic-velocity-controllers`

## Задачи

- [ ] Упростить urdf с помощью xarco
- [ ] Дефолтный материал ровера
- [x] "Центрировать" ровер
- [x] Правильные массы

## Шпаргалка

- `rosservice call gazebo/get_model_properties '{model_name: coke_can3}` - получение информации о модели
- `catkin_make --source pkg --pkg brain` - билд пакета
- `roslaunch gazebo_ros empty_world.launch` - пустой мир
- [образец .launch](https://github.com/ros/urdf_sim_tutorial/blob/master/launch/10-head.launch)
- `rosrun rqt_gui rqt_gui` -

Ссылки:

- [материалы и текстуры](http://gazebosim.org/tutorials?tut=color_model)
- [связь с ros](https://wiki.ros.org/urdf/Tutorials/Using%20a%20URDF%20in%20Gazebo), [более серьезный туториал](http://gazebosim.org/tutorials/?tut=ros_control), [подробный разбор](https://gazebosim.org/tutorials?tut=ros_control&cat=connect_ros#Prerequisites)
- [xarco](https://wiki.ros.org/urdf/Tutorials/Using%20Xacro%20to%20Clean%20Up%20a%20URDF%20File)
- [ROS URDF](http://gazebosim.org/tutorials/?tut=ros_urdf)
- [куча туториалов](https://gazebosim.org/tutorials?cat=connect_ros)
