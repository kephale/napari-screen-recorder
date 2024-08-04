import napari
import imageio
import numpy as np
from qtpy.QtWidgets import QPushButton, QVBoxLayout, QWidget, QSpinBox, QLabel, QCheckBox, QLineEdit, QFileDialog
from qtpy.QtCore import QTimer

class ScreenRecorder:
    def __init__(self, viewer):
        self.viewer = viewer
        self.recording = False
        self.frames = []
        self.timer = QTimer()
        self.file_path = 'recording.mp4'
        self.canvas_only = True

    def start_recording(self, duration, continuous):
        self.recording = True
        self.frames = []
        self.timer.timeout.connect(self.capture_frame)
        self.timer.start(int(1000 / 30))
        if not continuous:
            QTimer.singleShot(duration * 1000, self.stop_recording)

    def stop_recording(self):
        self.recording = False
        self.timer.stop()
        self.save_video()

    def capture_frame(self):
        if not self.recording:
            return
        # Capture the Napari viewer content
        frame = self.viewer.screenshot(canvas_only=self.canvas_only, flash=False)
        self.frames.append(frame)

    def save_video(self):
        if self.frames:
            imageio.mimwrite(self.file_path, self.frames, fps=30)
            print(f"Video saved as {self.file_path}")

    def set_file_path(self, file_path):
        self.file_path = file_path

    def set_canvas_only(self, canvas_only):
        self.canvas_only = canvas_only

class RecordingWidget(QWidget):
    def __init__(self, viewer):
        super().__init__()
        self.viewer = viewer
        self.recorder = ScreenRecorder(viewer)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.duration_label = QLabel("Duration (seconds):")
        layout.addWidget(self.duration_label)

        self.duration_spinbox = QSpinBox()
        self.duration_spinbox.setMinimum(1)
        self.duration_spinbox.setMaximum(3600)
        self.duration_spinbox.setValue(10)
        layout.addWidget(self.duration_spinbox)

        self.continuous_checkbox = QCheckBox("Record until stopped")
        layout.addWidget(self.continuous_checkbox)

        self.canvas_only_checkbox = QCheckBox("Canvas only")
        self.canvas_only_checkbox.setChecked(True)
        self.canvas_only_checkbox.stateChanged.connect(self.update_canvas_only)
        layout.addWidget(self.canvas_only_checkbox)

        self.filepath_label = QLabel("Save file as:")
        layout.addWidget(self.filepath_label)

        self.filepath_edit = QLineEdit("recording.mp4")
        layout.addWidget(self.filepath_edit)

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_file)
        layout.addWidget(self.browse_button)

        self.record_button = QPushButton("Start Recording")
        self.record_button.clicked.connect(self.start_recording)
        layout.addWidget(self.record_button)

        self.stop_button = QPushButton("Stop Recording")
        self.stop_button.clicked.connect(self.stop_recording)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def start_recording(self):
        duration = self.duration_spinbox.value()
        continuous = self.continuous_checkbox.isChecked()
        self.recorder.set_file_path(self.filepath_edit.text())
        self.recorder.start_recording(duration, continuous)

    def stop_recording(self):
        self.recorder.stop_recording()

    def browse_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Video", "", "MP4 Files (*.mp4);;All Files (*)")
        if file_path:
            self.filepath_edit.setText(file_path)

    def update_canvas_only(self, state):
        self.recorder.set_canvas_only(self.canvas_only_checkbox.isChecked())

def main():
    viewer = napari.Viewer()
    widget = RecordingWidget(viewer)
    viewer.window.add_dock_widget(widget, area='right')
    napari.run()

if __name__ == "__main__":
    main()
