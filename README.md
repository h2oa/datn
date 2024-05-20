# Hướng dẫn cài đặt

Tải về source code full

```
git clone https://github.com/h2oa/datn.git
```

Cài đặt thư viện `pymetasploit3`:

```
pip3 install -r requirements.txt
```

Đi tới thư mục:

`cd /usr/share/metasploit-framework/modules/auxiliary`

Tạo folder `customs`, ở đây sẽ lưu các custom modul:

```
sudo mkdir customs
```

Đi vào folder `customs`:

```
cd customs
```

Thêm các module trong folder `custom-modules` vào đây, kết quả:

![image](https://github.com/h2oa/datn/assets/114990730/1ab1e734-859d-429f-93d3-32414ad96325)

Trong Kali, chạy lệnh `msfrpcd -P password -S` để chạy server metasploit, mặc định port lắng nghe tại 55553:

![image](https://github.com/h2oa/datn/assets/114990730/6adc7934-d02f-4ac4-949d-585f3a3a509e)

Dùng lệnh `ip a` trong Kali để xem IP hiện tại:

![image](https://github.com/h2oa/datn/assets/114990730/b2656d64-ef8b-43f5-84ff-f1a4d83bab7d)

Thay đổi IP trong `package/functions.py`, ví dụ hiện tại máy server có IP `192.168.81.130`:

![image](https://github.com/h2oa/datn/assets/114990730/cfcbf6db-4e24-4820-a166-e42081bcd1ee)

Chạy vulnerability web local, đi vào `custom-vul-website/php-website`, chạy lệnh `sudo php -S 0.0.0.0:80` (nên chạy web server test scan trong Kali luôn).

Biến `domain` trong hàm `main()` của file `main.py` chính là địa chỉ IP của web server sẽ scan, trường hợp này là `192.168.81.130`:

![image](https://github.com/h2oa/datn/assets/114990730/b8bcbd4b-199a-4a6a-a597-76ab3747ff4a)

Bắt đầu scan, chạy lệnh `python3 main.py`.

Nếu chạy thấy thiếu thư viện nào thì `pip3 install` + `tên thư viện thiếu`, hoặc google
