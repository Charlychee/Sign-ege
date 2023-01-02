from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QShortcut, QTableWidgetItem
from PyQt5.QtCore import QDir, Qt, QItemSelectionModel
from PyQt5.QtGui import QPixmap, QKeySequence, QPainter, QColor
from EzLabelUi import Ui_Form

import sys, os
from datetime import datetime

import glob
import numpy as np
import pickle
import warnings

warnings.filterwarnings("ignore")

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
        self.active_index = 0

        # TODO: Image Dimensions
        
        # Draw Bounding Box
        self.click_count = 0
        self.bound_box = None

        self.image_label.mouseReleaseEvent = self.track_bounding_box_clicks
        # Select Class
        

        # Save Labels
        self.class_label_list = None
        self.bounding_box_list = None

        self.save_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        
        self.save_shortcut.activated.connect(self.save_labeled_data)
        self.save_btn.clicked.connect(self.save_labeled_data)

        # Changing Indices
        self.prev_img_btn.clicked.connect(self.open_prev_image)
        self.next_img_btn.clicked.connect(self.open_next_image)

        self.load_selected_btn.clicked.connect(self.open_image_from_table)

        # Save to file and hope no bug
        self.save_to_file_btn.clicked.connect(self.pickle_data)

    def open_prev_image(self):
        if self.active_index-1 < 0:
            self.info_label.setText("Index out of bounds")
            return
        self.active_index -= 1
        self.open_image_idx(self.active_index)

    def open_next_image(self):
        if self.active_index + 1 >= len(self.img_list):
            self.info_label.setText("Index out of bounds")
            return
        self.active_index += 1
        self.open_image_idx(self.active_index)

    def open_image_from_table(self):
        if not self.image_table.currentRow():
            self.info_label.setText("Please select an index to save")
            return
        self.open_image_idx(self.image_table.currentRow())
        self.active_index = self.image_table.currentRow()

    def open_image_idx(self, idx):
        if idx < 0 or idx >= len(self.img_list):
            self.info_label.setText("Index out of bounds")
            return 
        self.open_image(idx)
        self.draw_bounding_box(self.bounding_box_list[idx])

    def pickle_data(self):
        # Get timestamp of file and classify images
        with open(os.path.join(self.save_path_label.text(), 'labeled_images_' + datetime.now().strftime('%Y%m%d_%H%M%S')), 'wb') as file:
            
            pickle.dump(dict({
                'classes' : self.class_label_list,
                'bounding_boxes' : self.bounding_box_list}),
                file)
            

    def update_load_path(self):
        self.load_dir_name = QDir.toNativeSeparators(QFileDialog.getExistingDirectory(self, "Open Folder", self.load_path_label.text(), QFileDialog.ShowDirsOnly
                                             | QFileDialog.DontResolveSymlinks))
        self.load_path_label.setText(self.load_dir_name)
        self.img_list = [os.path.basename(item) for i in [glob.glob(self.load_dir_name + '\\*.%s' % ext) for ext in ["jpg","gif","png","tga"]] for item in i]
        
        # self.image_listview.addItems(self.img_list)
        self.image_table.clearContents()
        self.image_table.setRowCount(0) # Clear table
        self.image_table.setRowCount(len(self.img_list))
        for idx, item in enumerate(self.img_list):
            self.image_table.setItem(idx, 0, QTableWidgetItem(item))

        self.class_label_list = ['' for i in range(len(self.img_list))]
        self.bounding_box_list = np.zeros([len(self.img_list), 4])

        self.active_index = 0
        self.open_image(self.active_index)

    def update_save_path(self):
        dirName = QDir.toNativeSeparators(QFileDialog.getExistingDirectory(self, "Open Folder", self.save_path_label.text(), QFileDialog.ShowDirsOnly
                                             | QFileDialog.DontResolveSymlinks))
        self.save_path_label.setText(dirName)

    def open_image(self, counter):
        if not self.img_list or counter >= len(self.img_list):
            self.info_label.setText("No images left in the folder...")
            return 
        self.set_image(os.path.join(self.load_dir_name, self.img_list[counter]))
        self.image_table.selectionModel().select(self.image_table.model().index(counter, 0), QItemSelectionModel.Select | QItemSelectionModel.Current)

    def set_image(self, path):
        pixmap = QPixmap(path)
        self.image_label.setPixmap(pixmap)

    def track_bounding_box_clicks(self, event):
        self.click_count += 1
        rect = self.image_label.pixmap().rect()
        x = event.pos().x()
        y = event.pos().y()

        if (self.click_count == 1):
            self.bound_box = [y, x, 0, 0]
        else: # 2 clicks
            self.bound_box[2] = y - self.bound_box[0]
            self.bound_box[3] = x - self.bound_box[1]
            self.open_image(self.active_index)
            self.draw_bounding_box(self.bound_box)

        if (self.click_count == 2): # reset
            self.click_count = 0

    def draw_bounding_box(self, bound_box):
        paint = QPainter(self.image_label.pixmap())
        paint.setPen(QColor(255,34,255,255))
        paint.drawRect(bound_box[1], bound_box[0], bound_box[3], bound_box[2])
        self.update()
        
    def save_labeled_data(self):
        if not self.class_selection_combo.currentText() or self.bound_box == None:
            self.info_label.setText("Please select valid class and bounding box")
            return
        
        if self.active_index >= len(self.img_list):
            self.info_label.setText("All data labeled, please save and load new dataset")
            return

        self.class_label_list[self.active_index] = self.class_selection_combo.currentText()
        self.bounding_box_list[self.active_index] = np.array(self.bound_box)
        
        self.image_table.setItem(self.active_index, 1, QTableWidgetItem(" ,".join(map(str, self.bound_box))))
        self.image_table.setItem(self.active_index, 2, QTableWidgetItem(self.class_selection_combo.currentText()))

        self.active_index += 1
        self.open_image(self.active_index)
        self.class_selection_combo.clearEditText()
        self.class_selection_combo.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EzLabelWindow()
    window.show()
    app.exec_()