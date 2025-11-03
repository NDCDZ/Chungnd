# Lab 3: Tạo class Config với các biến static lưu thông tin cấu hình hệ thống (APP_NAME, VERSION). Viết hàm in cấu hình.
class Config:
    APP_NAME = "MyApplication"
    VERSION = "1.0.0"

    @staticmethod
    def show_config():
        print(f"App: {Config.APP_NAME}, Version: {Config.VERSION}")

if __name__ == "__main__":
    Config.show_config()
