local wheel_controller(idx) = {
    type: "velocity_controllers/JointVelocityController",
    joint: "wheel_" + idx + "_joint",
    pid: {p: 100.0, i: 0.01, d: 10.0}
};

std.manifestYamlDoc({rover: {
    joint_state_controller: {
        type: "joint_state_controller/JointStateController",
        publish_rate: 50
    },

    wheel_1_position_controller: wheel_controller("1"),
    wheel_6_position_controller: wheel_controller("6"),

    wheel_2_position_controller: wheel_controller("2"),
    wheel_4_position_controller: wheel_controller("4"),

    wheel_3_position_controller: wheel_controller("3"),
    wheel_5_position_controller: wheel_controller("5"),
}})
