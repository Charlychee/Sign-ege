# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EZ-label.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1081, 719)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.class_selection_combo = QtWidgets.QComboBox(self.frame)
        self.class_selection_combo.setEditable(True)
        self.class_selection_combo.setObjectName("class_selection_combo")
        self.horizontalLayout_5.addWidget(self.class_selection_combo)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.remove_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_btn.sizePolicy().hasHeightForWidth())
        self.remove_btn.setSizePolicy(sizePolicy)
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout_4.addWidget(self.remove_btn)
        self.save_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_4.addWidget(self.save_btn)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.img_dim_combo = QtWidgets.QComboBox(self.frame)
        self.img_dim_combo.setObjectName("img_dim_combo")
        self.gridLayout.addWidget(self.img_dim_combo, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.reset_to_default_btn = QtWidgets.QPushButton(self.frame)
        self.reset_to_default_btn.setObjectName("reset_to_default_btn")
        self.gridLayout_2.addWidget(self.reset_to_default_btn, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.load_path_btn = QtWidgets.QPushButton(self.frame)
        self.load_path_btn.setObjectName("load_path_btn")
        self.gridLayout_4.addWidget(self.load_path_btn, 1, 1, 1, 1)
        self.load_path_label = QtWidgets.QLabel(self.frame)
        self.load_path_label.setObjectName("load_path_label")
        self.gridLayout_4.addWidget(self.load_path_label, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 4, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.save_path_btn = QtWidgets.QPushButton(self.frame)
        self.save_path_btn.setObjectName("save_path_btn")
        self.gridLayout_3.addWidget(self.save_path_btn, 1, 1, 1, 1)
        self.save_path_label = QtWidgets.QLabel(self.frame)
        self.save_path_label.setObjectName("save_path_label")
        self.gridLayout_3.addWidget(self.save_path_label, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.use_camera_cbox = QtWidgets.QCheckBox(self.frame)
        self.use_camera_cbox.setObjectName("use_camera_cbox")
        self.gridLayout_5.addWidget(self.use_camera_cbox, 0, 1, 1, 1)
        self.auto_load_next_img_cbox = QtWidgets.QCheckBox(self.frame)
        self.auto_load_next_img_cbox.setChecked(True)
        self.auto_load_next_img_cbox.setObjectName("auto_load_next_img_cbox")
        self.gridLayout_5.addWidget(self.auto_load_next_img_cbox, 0, 0, 1, 1)
        self.use_fixed_sz_cbox = QtWidgets.QCheckBox(self.frame)
        self.use_fixed_sz_cbox.setObjectName("use_fixed_sz_cbox")
        self.gridLayout_5.addWidget(self.use_fixed_sz_cbox, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.height_sbox = QtWidgets.QSpinBox(self.frame)
        self.height_sbox.setObjectName("height_sbox")
        self.horizontalLayout_2.addWidget(self.height_sbox)
        self.label_11 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.width_sbox = QtWidgets.QSpinBox(self.frame)
        self.width_sbox.setObjectName("width_sbox")
        self.horizontalLayout_2.addWidget(self.width_sbox)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 2, 1, 1)
        self.switch_class_selection_cbox = QtWidgets.QCheckBox(self.frame)
        self.switch_class_selection_cbox.setObjectName("switch_class_selection_cbox")
        self.gridLayout_5.addWidget(self.switch_class_selection_cbox, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.image_label.setText(_translate("Form", "TextLabel"))
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.remove_btn.setText(_translate("Form", "Remove Selected"))
        self.save_btn.setText(_translate("Form", "Save (Ctrl+S)"))
        self.label_6.setText(_translate("Form", "Load Path"))
        self.label_2.setText(_translate("Form", "Image Dimensions"))
        self.label_9.setText(_translate("Form", "Class Selection"))
        self.label_4.setText(_translate("Form", "Save Path"))
        self.reset_to_default_btn.setText(_translate("Form", "Reset to Default"))
        self.label.setText(_translate("Form", "Click on Image to Select Bounding Box"))
        self.label_7.setText(_translate("Form", "Options"))
        self.load_path_btn.setText(_translate("Form", "File..."))
        self.load_path_label.setText(_translate("Form", "Load Dir"))
        self.save_path_btn.setText(_translate("Form", "File..."))
        self.save_path_label.setText(_translate("Form", "Save Directory"))
        self.label_3.setText(_translate("Form", "Keep Bounding Box"))
        self.use_camera_cbox.setText(_translate("Form", "Use Camera"))
        self.auto_load_next_img_cbox.setText(_translate("Form", "Auto Load Next Image"))
        self.use_fixed_sz_cbox.setText(_translate("Form", "Use Fixed Size Box"))
        self.label_10.setText(_translate("Form", "H:"))
        self.label_11.setText(_translate("Form", "W:"))
        self.switch_class_selection_cbox.setText(_translate("Form", "Switch Class Selection to Buttons"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())