from monitor import InfoPlatform
import sys

if __name__ == '__main__':
    if sys.platform == 'win32':
        info = InfoPlatform()
        info.save_log(file_log='name_file')