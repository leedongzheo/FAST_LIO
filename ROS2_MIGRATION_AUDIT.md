# ROS2 Jazzy Migration Audit (FAST_LIO)

## Kết luận nhanh
Mã nguồn C++ runtime đã được chuyển sang ROS2 API (rclcpp, `*::msg::*`, tf2). Không còn `ros::`, `tf::` hay include ROS1 (`ros/ros.h`) trong source hiện tại.

## Các điểm còn ROS1
- Không còn ROS1 API trong C++ source sau khi audit lại.
- README vẫn còn hướng dẫn ROS1 (ví dụ `catkin_make`, `roslaunch`, `source devel/setup.bash`), cần cập nhật tài liệu nếu muốn “ROS2 hoàn toàn” cả docs/workflow.

## Tệp cần refactor ưu tiên
1. `README.md` (hướng dẫn build/run vẫn thiên ROS1).

## Trạng thái hiện tại
- C++ runtime: ROS2.
- Build/package: ROS2 (`ament_cmake`).
- Tài liệu sử dụng: còn lẫn ROS1/ROS2.
