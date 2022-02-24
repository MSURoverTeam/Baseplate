#include <string.h>

#include <Arduino.h>
#include <Servo.h>
#include <ros.h>
#include <brain/ServoCommand.h>

Servo altServo;
Servo lidServo;

typedef void (*Handler)();


enum class Limit {
    UP = 40,
    DOWN = 130,
    OPEN = 100,
    CLOSED = 40
};


enum class Command {
    OPEN,
    CLOSE,
    UP,
    DOWN,
    DROP,
    RETRACT,
    PUT,
};


void up_handler() {
    altServo.write(int(Limit::UP));
}


void down_handler() {
    altServo.write(int(Limit::DOWN));
}


void open_handler() {
    lidServo.write(int(Limit::OPEN));
}


void close_handler() {
    lidServo.write(int(Limit::CLOSED));
}


void drop_handler() {
    down_handler();
    delay(500);
    open_handler();
}


void retract_handler() {
    close_handler();
    delay(500);
    up_handler();
}


void put_handler() {
    drop_handler();
    delay(300);
    retract_handler();
}


Handler getHandler(const char* command) {
    if (strcmp(command, "open") == 0) {
        return &open_handler;
    }
    else if (strcmp(command, "close") == 0) {
        return &close_handler;
    }
    else if (strcmp(command, "up") == 0) {
        return &up_handler;
    }
    else if (strcmp(command, "down") == 0) {
        return &down_handler;
    }
    else if (strcmp(command, "drop") == 0) {
        return &drop_handler;
    }
    else if (strcmp(command, "retract") == 0) {
        return &retract_handler;
    }
    else if (strcmp(command, "put") == 0) {
        return &put_handler;
    }
    return nullptr;
}


class MicroHardware : public ArduinoHardware {
    public:
    MicroHardware():ArduinoHardware(&Serial1, 115200){};
};
ros::NodeHandle_<MicroHardware>  nh;


void messageCb(const brain::ServoCommand& servo_msg) {
    Serial.println(servo_msg.command);
    auto handler = getHandler(servo_msg.command);
    if (handler == nullptr) {
        Serial.println("No handler!");
        return;
    }
    handler();
}


ros::Subscriber<brain::ServoCommand> sub("servo", &messageCb);


void setup() {
    altServo.attach(44);
    lidServo.attach(45);
    Serial.begin(9600);
    nh.initNode();
    nh.subscribe(sub);
}


void loop() {
    nh.spinOnce();
    delay(1);
}
