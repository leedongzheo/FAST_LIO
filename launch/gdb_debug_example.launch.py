from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    rviz = LaunchConfiguration('rviz')

    return LaunchDescription([
        DeclareLaunchArgument('rviz', default_value='true', description='Launch RViz2'),
        Node(
            package='fast_lio',
            executable='fastlio_mapping',
            name='laserMapping',
            output='screen',
            prefix=['gdb -ex run --args'],
            parameters=['config/avia.yaml', {
                'publish/path_en': True,
                'publish/scan_publish_en': True,
                'publish/dense_publish_en': True,
                'publish/scan_bodyframe_pub_en': True,
            }]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', 'rviz_cfg/loam_livox.rviz'],
            condition=IfCondition(rviz)
        )
    ])
