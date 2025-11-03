# Lab 3: Config Class (Static Config Info)
class Config:
    APP_NAME = "MyApplication"
    VERSION = "1.0.0"

    @staticmethod
    def show_config():
        print(f"App: {Config.APP_NAME}, Version: {Config.VERSION}")

if __name__ == "__main__":
    Config.show_config()
