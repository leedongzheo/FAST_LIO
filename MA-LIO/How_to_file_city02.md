# How_to_file_city02.md

## Mục tiêu
Tài liệu này hướng dẫn **chi tiết theo từng terminal** cách chạy thuật toán FastLIO2/MA-LIO với dữ liệu **City02** trong thư mục `MA-LIO` bằng **ROS2**.

> Lưu ý quan trọng: bộ City02 gốc thường được phát lại qua node/file_player ROS1. Nếu bạn chỉ có ROS1 bag thì cần convert sang ROS2 bag trước khi chạy bằng `ros2 bag play`.

---

## 1) Chuẩn bị workspace ROS2

### Terminal 1 — tạo workspace và clone mã
```bash
mkdir -p ~/fastlio2_ws/src
cd ~/fastlio2_ws/src
git clone <YOUR_FAST_LIO_REPO_URL> FAST_LIO
cd FAST_LIO
```

### Terminal 1 — build toàn bộ package ROS2
```bash
cd ~/fastlio2_ws
source /opt/ros/$ROS_DISTRO/setup.bash
colcon build --symlink-install
source install/setup.bash
```

---

## 2) Tải và giải nén City02

### Terminal 2 — tải City02
```bash
mkdir -p ~/datasets/city
cd ~/datasets/city
# Tải từ Google Drive (City02)
# https://drive.google.com/file/d/1lpXGPIz67T_x9wLGYpb-m5tdMsorPpyS/view?usp=sharing
```

Sau khi tải xong, giải nén để có thư mục dạng `City02/` (chứa các file `.bin`, `xsens_imu.csv`, `data_stamp.csv`, `ouster_stamp.csv`, ...).

---

## 3) Trường hợp dữ liệu là ROS1 bag: convert sang ROS2 bag

Nếu bạn đã có dữ liệu ở dạng ROS1 bag (ví dụ `city02_ros1.bag`), chạy theo thứ tự sau.

### Terminal 3 — source ROS1
```bash
source /opt/ros/noetic/setup.bash
```

### Terminal 4 — source ROS2
```bash
source /opt/ros/$ROS_DISTRO/setup.bash
```

### Terminal 5 — convert bag
```bash
# Ví dụ với công cụ rosbags-convert (Python)
python3 -m pip install --user rosbags
~/.local/bin/rosbags-convert \
  --src /path/to/city02_ros1.bag \
  --dst /path/to/city02_ros2_bag
```

Sau bước này bạn sẽ có thư mục ROS2 bag, có thể phát bằng `ros2 bag play`.

---

## 4) Chạy thuật toán bằng ROS2 (không dùng file .sh)

`mapping_city02.launch.py` mặc định nạp `config/city02.yaml` (config riêng cho City02).

## Cách A — phát City02 bằng `ros2 bag play` (khuyến nghị cho ROS2)

### Terminal 6 — chạy mapping FastLIO2
```bash
cd ~/fastlio2_ws
source /opt/ros/$ROS_DISTRO/setup.bash
source install/setup.bash

# Chọn launch phù hợp sensor chính của dữ liệu đã convert.
# Ví dụ nếu topic point cloud là dạng Livox Avia:
ros2 launch fast_lio mapping_city02.launch.py
```

### Terminal 7 — phát bag City02 ROS2
```bash
cd ~/fastlio2_ws
source /opt/ros/$ROS_DISTRO/setup.bash
source install/setup.bash
ros2 bag play /path/to/city02_ros2_bag --clock
```

### Terminal 8 (tuỳ chọn) — mở RViz2
```bash
cd ~/fastlio2_ws
source /opt/ros/$ROS_DISTRO/setup.bash
source install/setup.bash
rviz2
```

---

## Cách B — dùng dữ liệu raw City02 (bin/csv) trong thư mục MA-LIO

Với dữ liệu raw từ link City02, bạn cần một node phát lại dữ liệu theo ROS2 (publish PointCloud2/IMU).  
Nếu bạn vẫn dùng `MA-LIO/file_player` bản ROS1 thì phải bridge hoặc migrate node này sang ROS2 trước khi dùng trực tiếp với `ros2 launch`.

Quy trình khuyến nghị ROS2 sạch:
1. Dùng player ROS1 để xuất ra ROS1 bag.
2. Convert ROS1 bag -> ROS2 bag theo mục (3).
3. Phát lại bằng `ros2 bag play` theo mục (4) Cách A.

---

## 5) Kiểm tra nhanh topic trước khi chạy

### Terminal 9 — xem danh sách topic
```bash
source /opt/ros/$ROS_DISTRO/setup.bash
source ~/fastlio2_ws/install/setup.bash
ros2 topic list
```

### Terminal 9 — kiểm tra tần số IMU/LiDAR
```bash
ros2 topic hz /imu/data
ros2 topic hz /livox/lidar
```

Nếu topic tên khác, cần sửa remap trong launch hoặc tên topic khi phát bag.

---

## 6) Mẹo xử lý lỗi thường gặp

1. **Không thấy map cập nhật**: kiểm tra frame_id, timestamp, và `--clock` khi play bag.
2. **Lệch topic name**: dùng `ros2 topic list` rồi remap đúng topic trong launch.
3. **Mất TF**: đảm bảo có static transform IMU↔LiDAR đúng theo extrinsic của City dataset (`MA-LIO/Extrinsic.txt`).
4. **Drop message**: giảm tốc độ play (`-r 0.5`) hoặc tăng tài nguyên máy.

---

## 7) Lệnh chạy mẫu đầy đủ theo thứ tự terminal

### Terminal A
```bash
cd ~/fastlio2_ws
source /opt/ros/$ROS_DISTRO/setup.bash
source install/setup.bash
ros2 launch fast_lio mapping_city02.launch.py
```

### Terminal B
```bash
cd ~/fastlio2_ws
source /opt/ros/$ROS_DISTRO/setup.bash
source install/setup.bash
ros2 bag play /path/to/city02_ros2_bag --clock
```

### Terminal C
```bash
cd ~/fastlio2_ws
source /opt/ros/$ROS_DISTRO/setup.bash
source install/setup.bash
rviz2
```

