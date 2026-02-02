import sys
import os
import subprocess

from PySide6.QtCore import QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox
from designer.main_ui import Ui_VideoCoverApp


class VideoCoverApp(QMainWindow):

    start_ffmpge_cover = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_VideoCoverApp()
        self.ui.setupUi(self)

        # 文件路径存储
        self.mp4_path = ""
        self.image_path = ""

        self.ui.mp4_btn.clicked.connect(lambda: self.select_file("mp4"))
        self.ui.image_btn.clicked.connect(lambda: self.select_file("image"))
        self.ui.process_btn.clicked.connect(lambda: self.process_files())

        self.worker = Worker()
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        self.start_ffmpge_cover.connect(self.worker.ffmpeg_cover)

        self.worker.error.connect(self.show_error)
        self.worker.success.connect(self.show_success)
        self.worker.working.connect(lambda: self.set_process_btn(False))
        self.worker.finish.connect(lambda: self.set_process_btn(True))

    def select_file(self, file_type):
        """文件选择对话框"""
        dialog = QFileDialog()
        if file_type == "mp4":
            path, _ = dialog.getOpenFileName(
                self, "选择 MP4 文件", "",
                "MP4 视频 (*.mp4)"
            )
            if path:
                self.mp4_path = path
                self.ui.mp4_label.setText(os.path.basename(path))
        else:
            path, _ = dialog.getOpenFileName(
                self, "选择封面图片", "",
                "图片文件 (*.jpg *.jpeg *.png)"
            )
            if path:
                self.image_path = path
                self.ui.image_label.setText(os.path.basename(path))

        # 启用处理按钮
        if self.mp4_path and self.image_path:
            self.ui.process_btn.setEnabled(True)

    def process_files(self):
        """执行 FFmpeg 命令处理文件"""
        try:
            subprocess.run(["ffmpeg.exe", "-version"],
                           check=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        except Exception as e:
            # QMessageBox.warning(self, 'Warning', f'{e}\n请到 https://www.gyan.dev/ffmpeg/builds 下载 Windows 系统下的 FFmpeg 执行文件，并将执行文件路径放置在系统环境中。')
            msg = QMessageBox(self)
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Warning)  # noqa
            msg.setText(str(e))
            msg.setDetailedText(
                '请到 https://www.gyan.dev/ffmpeg/builds 下载 Windows 系统下的 FFmpeg 执行文件，并将执行文件路径放置在系统环境中。')
            msg.exec()
            return 0
        self.start_ffmpge_cover.emit(self.mp4_path, self.image_path)
        return 0

    def set_process_btn(self, flag: bool):
        self.ui.process_btn.setEnabled(flag)

    def show_error(self, error):
        msg = QMessageBox(self)
        msg.setWindowTitle("Warning")
        msg.setIcon(QMessageBox.Warning)  # noqa
        msg.setText(str(error))
        msg.setDetailedText(
            '请到 https://www.gyan.dev/ffmpeg/builds 下载 Windows 系统下的 FFmpeg 执行文件，并将执行文件路径放置在系统环境中。')
        msg.exec()

    def show_success(self, msg):
        QMessageBox.information(self, "Success", msg)


class Worker(QObject):
    # 定义工作线程的完成信号
    working = Signal()
    finish = Signal()
    success = Signal(str)
    error = Signal(str)

    @Slot(str, str)
    def ffmpeg_cover(self, mp4_path, image_path):
        base_name = os.path.splitext(os.path.basename(mp4_path))[0]
        output_name = f"{base_name}_with_cover.mp4"
        cmd = [
            "ffmpeg",
            "-i", mp4_path,
            "-i", image_path,
            "-map", "0",
            "-map", "1",
            "-c", "copy",
            "-disposition:v:1", "attached_pic",
            output_name
        ]
        try:
            self.working.emit()
            subprocess.run(cmd, check=True)
            self.success.emit('转换成功！')
        except subprocess.CalledProcessError as e:
            self.error.emit(str(e))
        finally:
            self.finish.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = VideoCoverApp()
    window.show()

    sys.exit(app.exec())
