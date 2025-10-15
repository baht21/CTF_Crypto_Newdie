Solution:

Mục tiêu của bài này là ta cần chuyển đổi chuỗi hexadecimal sang base64.

Vì vậy quy trình chuyển đổi như sau: Hex → Raw Bytes → Base64
Ví dụ về cách đổi:
- Mỗi kí tự trong Hex được biểu diễn bởi 4 bit
- Mỗi kí tự trong base64 được biểu diễn bởi 6 bit

+) Hex:   49        27       6d

+) Binary: 01001001 00100111 01101101

+) Chia nhóm thành 6 bit cho phù hợp với base64:

010010 010010 011101 101101

→ Base64 index: 18, 18, 29, 45 → Chuyển sang chuỗi ký tự: S S d t

------
Code
---
import base64: Sử dụng thư viện base64 tích hợp sẵn của Python

bytes.fromhex(CH_hex): Đọc mỗi 2 ký tự hex và chuyển thành giá trị byte thật

base64.b64encode(CH_bytes): Mã hóa dữ liệu nhị phân sang chuỗi base64

.decode(): Chuyển kết quả từ bytes sang string để in ra

--> Trong python có sẵn các hàm chuyển hex sang bytes, chuyển bytes sang base64 trong thư viện chuẩn nên khá thuận tiện cho việc giải challenge này.