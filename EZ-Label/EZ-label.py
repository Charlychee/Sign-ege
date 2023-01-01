from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QShortcut
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QPixmap, QKeySequence
from EzLabelUi import Ui_Form

import sys, os
import glob

class EzLabelWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # File Browser Stuff
        self.load_path_label.setText(os.getcwd())
        self.save_path_label.setText(os.getcwd())
        self.load_path_btn.clicked.connect(self.update_load_path)
        self.save_path_btn.clicked.connect(self.update_save_path)
        self.img_list = []

        # Image Dimensions
        
        # Save Labels
        self.class_label_list = []
        self.bounding_box_list = []

        self.save_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        
        self.save_shortcut.activated.connect(self.save_labeled_data)
        self.save_btn.clicked.connect(self.save_labeled_data)

    def update_load_path(self):
        dirName = QDir.toNativeSeparators(QFileDialog.getExistingDirectory(self, "Open Folder", self.load_path_label.text(), QFileDialog.ShowDirsOnly
                                             | QFileDialog.DontResolveSymlinks))
        self.load_path_label.setText(dirName)
        self.img_list = [item for i in [glob.glob(dirName + '\\*.%s' % ext) for ext in ["jpg","gif","png","tga"]] for item in i]
        self.open_image()

    def update_save_path(self):
        dirName = QDir.toNativeSeparators(QFileDialog.getExistingDirectory(self, "Open Folder", self.save_path_label.text(), QFileDialog.ShowDirsOnly
                                             | QFileDialog.DontResolveSymlinks))
        self.save_path_label.setText(dirName)

    def open_image(self):
        if not self.img_list:
            self.image_label.setText("No images left in the folder...")
            return
        self.set_image(self.img_list.pop(0))

    def set_image(self, path):
        pixmap = QPixmap(path)
        self.image_label.setPixmap(pixmap)
        # TODO: rescale dimensions

    def save_labeled_data(self):
        # get bounding box
        # get class label
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EzLabelWindow()
    window.show()
    app.exec_()