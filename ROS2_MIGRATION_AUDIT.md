# ROS2 Jazzy Migration Audit (FAST_LIO)

## Kết luận nhanh
Mã nguồn C++ runtime đã được chuyển sang ROS2 API (rclcpp, `*::msg::*`, tf2). Không còn `ros::`, `tf::` hay include ROS1 (`ros/ros.h`) trong source hiện tại.

## Các điểm còn ROS1
- Không còn ROS1 API trong C++ source sau khi audit lại.
- Đã chuyển các launch XML kiểu ROS1 sang ROS2 Python launch (`*.launch.py`) và cập nhật lệnh build/run trong README sang ROS2 (`colcon`, `ros2 launch`, `source install/setup.bash`).

## Tệp cần refactor ưu tiên
1. `README.md` (hướng dẫn build/run vẫn thiên ROS1).

## Trạng thái hiện tại
- C++ runtime: ROS2.
- Build/package: ROS2 (`ament_cmake`).
- Tài liệu sử dụng: ROS2-first; các lệnh ROS1 cũ đã được thay thế.
