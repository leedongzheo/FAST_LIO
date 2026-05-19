# ROS2 Jazzy Migration Audit (FAST_LIO)

## Kết luận nhanh
Chưa chuyển hoàn toàn sang ROS2 Jazzy. Phần build/package đã là ROS2 (`ament_cmake`) nhưng runtime chính vẫn dùng API ROS1 trong `laserMapping.cpp` và `IMU_Processing.hpp`.

## Các điểm còn ROS1
- `#include <ros/ros.h>`, `ros::init`, `ros::NodeHandle`, `ros::Publisher`, `ros::Subscriber`, `ros::Rate`, `ros::spinOnce`, `ros::ok`.
- Message kiểu ROS1: `sensor_msgs::Imu`, `sensor_msgs::PointCloud2`, `nav_msgs::Odometry`, `nav_msgs::Path` (header `.h` kiểu ROS1).
- TF ROS1: `tf::TransformBroadcaster`, `tf::Quaternion`, `tf::StampedTransform`.
- Logging macro ROS1: `ROS_WARN`, `ROS_INFO`.

## Tệp cần refactor ưu tiên
1. `src/laserMapping.cpp` (nút chính, pub/sub/spin/time/tf).
2. `src/IMU_Processing.hpp` (kiểu message IMU và logging).
3. `include/common_lib.h` (kiểu `MeasureGroup::imu` đang là ROS1 ConstPtr).

## Trạng thái hiện tại
- `preprocess.*` đã dùng nhiều thành phần ROS2 (`rclcpp`, `sensor_msgs::msg::PointCloud2`).
- Toàn cục project vẫn là **hybrid** ROS1/ROS2 nên chưa chạy sạch ROS2 runtime.
