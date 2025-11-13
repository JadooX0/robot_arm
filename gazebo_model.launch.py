from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    sdf_path = os.path.join(
        os.getenv('HOME'),
        'ros2_ws', 'src', 'my_robot_arm', 'urdf', 'my_robot_arm.sdf'
    )

    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'ros2', 'launch', 'ros_gz_sim', 'gz_sim.launch.py',
                f'gz_args:=-r -v 4 {sdf_path}'
            ],
            output='screen'
        )
    ])

