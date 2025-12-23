import cv2
from ultralytics import YOLO
#!ping ultralytics

# Memuat model YOLO (Anda bisa mengganti model, misalnya 'yolov8n.pt', 'yolov8s.pt', dll.)
#model = YOLO('yolov8n.pt')  # Gunakan model lebih kecil seperti 'yolov8n.pt' untuk deteksi real-time yang lebih cepat
#model = YOLO('best_bukpen.pt')
model = YOLO('yolo11m.pt')
# Inisialisasi kamera (webcam)
cap = cv2.VideoCapture(0)  # Ganti indeks menjadi 1 atau lebih tinggi jika menggunakan webcam eksternal

# Periksa apakah kamera berhasil dibuka
if not cap.isOpened():
    print("Error: Tidak dapat membuka webcam.")
    exit()

while True:
    # Tangkap frame dari webcam
    ret, frame = cap.read()
    if not ret:
        print("Gagal mengambil frame")
        break

    # Jalankan YOLO pada frame
    results = model(frame)

    # Anotasi frame dengan hasil deteksi
    annotated_frame = results[0].plot()  # Visualisasi deteksi pada frame

    # Tampilkan frame hasil deteksi
    cv2.imshow('YOLO Deteksi Real-Time', annotated_frame)

    # Hentikan loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan kamera dan tutup jendela
cap.release()
cv2.destroyAllWindows()
