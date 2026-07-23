import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n6a60ec15cb6c054e8f13feaa",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a60ec15cb6c054e8f13feaa",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"6a60eb9dcb6c054e8f13fcd4","mode":"speed","max_speed":6.2832,"reverse":true,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a60ec36cb6c054e8f13ff7d","source_node_id":"6a60ec32cb6c054e8f13ff5f","source_pin_id":"back_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n6a60ec1ecb6c054e8f13fee4",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a60ec1ecb6c054e8f13fee4",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"6a60eba8cb6c054e8f13fd09","mode":"speed","max_speed":6.2832,"reverse":true,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a60ec39cb6c054e8f13ff8c","source_node_id":"6a60ec32cb6c054e8f13ff5f","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n6a60ec20cb6c054e8f13fef5",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a60ec20cb6c054e8f13fef5",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"6a60eba4cb6c054e8f13fced","mode":"speed","max_speed":6.2832,"reverse":true,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a60ec3bcb6c054e8f13ff9b","source_node_id":"6a60ec32cb6c054e8f13ff5f","source_pin_id":"back_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_n6a60ec17cb6c054e8f13febb",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a60ec17cb6c054e8f13febb",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"6a60eb92cb6c054e8f13fcbd","mode":"speed","max_speed":6.2832,"reverse":true,"timeout_s":0}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e541cd15153dec61d7af:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e541cd15153dec61d7af:state","name":"state","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a60ec34cb6c054e8f13ff6e","source_node_id":"6a60ec32cb6c054e8f13ff5f","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_n6a60ec2dcb6c054e8f13ff4e",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a60ec2dcb6c054e8f13ff4e",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"output_mode":"diff_drive"}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e702cd15153dec61d7da:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3e702cd15153dec61d7da:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3e702cd15153dec61d7da:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a60ed7acb6c054e8f14025e","target_node_id":"6a60ec32cb6c054e8f13ff5f","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel_teleop"}]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_n6a60ec32cb6c054e8f13ff5f",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "6a60ec32cb6c054e8f13ff5f",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"teleop_timeout_s":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3e71bcd15153dec61d7f8:cmd_vel_teleop","name":"cmd_vel_teleop","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3e71bcd15153dec61d7f8:cmd_vel_automated","name":"cmd_vel_automated","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3e71bcd15153dec61d7f8:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:back_left_motor","name":"back_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3e71bcd15153dec61d7f8:back_right_motor","name":"back_right_motor","direction":"output","msg_type":"std_msgs/Float64"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a60ed7acb6c054e8f14025e","source_node_id":"6a60ec2dcb6c054e8f13ff4e","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel_teleop"},{"connection_id":"6a60ee15cb6c054e8f1402db","source_node_id":"6a60edb6cb6c054e8f1402b4","source_pin_id":"cmd_vel_automated","target_pin_id":"cmd_vel_automated"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"6a60ec34cb6c054e8f13ff6e","target_node_id":"6a60ec17cb6c054e8f13febb","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"6a60ec36cb6c054e8f13ff7d","target_node_id":"6a60ec15cb6c054e8f13feaa","source_pin_id":"back_left_motor","target_pin_id":"command"},{"connection_id":"6a60ec39cb6c054e8f13ff8c","target_node_id":"6a60ec1ecb6c054e8f13fee4","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"6a60ec3bcb6c054e8f13ff9b","target_node_id":"6a60ec20cb6c054e8f13fef5","source_pin_id":"back_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_NODE_LOG_DIR": "/var/log/polyflow/nodes",
            }
        ),
    ])