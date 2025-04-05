### CÁCH SỬ DỤNG CODE ỨNG DỤNG THỊ GIÁC MÁY TÍNH NHẬN DIỆN VÀ QUẢN LÝ SÁCH TRÊN KỆ BẰNG YOLOV5

#### THƯ MỤC DỮ LIỆU TRONG DỰ ÁN
- `bookshelf-data`: Thư mục chứa dữ liệu bao gồm các tệp `train`, `test`, `val`. Các tệp này chứa các ảnh đã được gán nhãn để huấn luyện, kiểm tra và xác nhận mô hình.
- `data.yaml`: Tệp này mô tả cấu trúc dữ liệu trong dự án và cung cấp thông tin về các lớp đối tượng và đường dẫn đến các tệp ảnh trong thư mục.

#### HUẤN LUYỆN MÔ HÌNH
Để huấn luyện mô hình YOLOv5, bạn có thể sử dụng tệp `training.py`. Tệp này được thiết kế để tự động hóa quá trình huấn luyện mô hình YOLOv5 trên dữ liệu của bạn.

Tệp `training.py` có nội dung sau:
```python
import os

# Đường dẫn đến thư mục YOLOv5
YOLOV5_PATH = os.path.join(os.getcwd(), "yolov5")

# Các tham số huấn luyện
img_size = 640  
batch_size = 16  
epochs = 50 
data_file = "bookshelf-data/data.yaml"  
weights_file = "yolov5s.pt" 
device = "cpu"  

# Lệnh huấn luyện mô hình
train_command = f"python {YOLOV5_PATH}/train.py --img {img_size} --batch {batch_size} --epochs {epochs} --data {data_file} --weights {weights_file} --device {device}" 

# Chạy lệnh huấn luyện
os.system(train_command)

```

### CÁCH SỬ DỤNG FILE `main.py` ĐỂ TEST MÔ HÌNH NHẬN DIỆN SÁCH

#### MÔ TẢ
Tệp `main.py` cho phép bạn sử dụng mô hình YOLOv5 đã huấn luyện để nhận diện sách trong ảnh hoặc video. Bạn có thể chọn chế độ nhận diện giữa ảnh và video và lưu kết quả vào thư mục `outputs`.

#### CÁC BƯỚC SỬ DỤNG

1. **Cài đặt các phụ thuộc**:
   Bạn cần cài đặt các thư viện sau nếu chưa có:
   ```bash
   pip install torch opencv-python
