# CÁCH SỬ DỤNG CODE ỨNG DỤNG THỊ GIÁC MÁY TÍNH NHẬN DIỆN VÀ QUẢN LÝ SÁCH TRÊN KỆ BẰNG YOLOV5

### THƯ MỤC DỮ LIỆU TRONG DỰ ÁN
- `bookshelf-data` - Thư mục chứa dữ liệu (train, val, test).
- `data.yaml` - Tệp mô tả cấu trúc dữ liệu, số lớp và đường dẫn ảnh.
- `yolov5` - Thư mục chứa mã nguồn mô hình YOLOv5.
- `wandb` - Theo dõi và quản lý các thử nghiệm trong dự án.
- `training.py` - Code huấn luyện mô hình.
- `main.py` - Dùng để kiểm tra mô hình đã huấn luyện với ảnh hoặc video.
- `mobile.py` - Dùng để kiểm tra mô hình đã huấn luyện với camera.
- `app.py` - Dùng để sử dụng nhận diện trên website.
- `outputs` - Thư mục lưu kết quả nhận diện (ảnh/video).
- `static` - Thư mục chứa ảnh và video đầu ra của website và style.css cho HTML.
- `templates` - Thư mục chứa giao diện HTML.
- `yolov5s.pt` - Tệp trọng số (weights file) của mô hình YOLOv5.

### HUẤN LUYỆN MÔ HÌNH
Để huấn luyện mô hình YOLOv5, có thể sử dụng tệp `training.py`.

Tệp `training.py` bạn có thể xem trong dự án.

### CÁCH SỬ DỤNG FILE `main.py` ĐỂ TEST MÔ HÌNH NHẬN DIỆN SÁCH

1. **Cài đặt các phụ thuộc**

Bạn cần cài đặt các thư viện sau nếu chưa có:
   ```bash
   pip install torch opencv-python
   ```
2. **Chạy code huấn luyện mô hình**

Bạn cần chạy code:
   ```python
   python main.py

   ```
Sau khi huấn luyện xong, tệp trọng số tốt nhất (best.pt) sẽ nằm trong:

   ```bash
   yolov5/runs/train/exp4/weights/best.pt
   ```
### KIỂM TRA MÔ HÌNH VỚI FILE `main.py`
1. **Chuẩn bị mô hình**

Đảm bảo bạn đã huấn luyện mô hình và có tệp best.pt tại:
   ```bash
   yolov5/runs/train/exp4/weights/best.pt
   ```

2. **Cấu hình thư mục đầu ra**

Thư mục outputs/ sẽ được tạo tự động để lưu kết quả đầu ra từ ảnh hoặc video.


3. **Chạy tệp main.py**
```python
python main.py
```

4. **Chọn chế độ image hay video để nhận diện ảnh**

Khi chạy `python main.py` xong sẽ hiện lệnh cho người dùng nhập vào image hay video, thì bạn có thể chọn 1 trong 2.

Sau đó dán đường dẫn link ảnh mà bạn muốn nhận diện sách.

### CÓ THỂ MỞ CAMERA ĐỂ NHẬN DIỆN SÁCH VỚI FILE `mobile.py`
1. **Chạy tệp mobile.py**
```python
python mobile.py
```

2. **Chọn chế độ camera để nhận diện ảnh**

Khi chạy `python main.py` xong sẽ hiện lệnh cho người dùng nhập vào camera.

Sau đó camera sẽ mở và bạn có thể thử với các cuốn sách có sẵn.

### SỬ DỤNG FLASK ĐỂ NHẬN DIỆN ẢNH TRÊN WEBSITE VỚI `app.py`

1. **Chạy tệp main.py**
```python
python app.py
```
2. **Sử dụng website để nhận diện ảnh**

Trên website sẽ cho người dùng nhập ảnh tử máy, và sẽ nhận diện trực tiếp.

Có thể kiểm tra ảnh trong thư mục `static`.

#### Cảm ơn bạn đã sử dụng mô hình YOLOv5 của tôi!
##### Chúng tôi rất vui khi mô hình này có thể hỗ trợ bạn trong việc nhận diện và quản lý sách trên kệ. 






