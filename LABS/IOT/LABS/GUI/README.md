# GUI by Python

## PyQt5
[เขียนโปรแกรมแบบ GUI ด้วย Python(PyQt5)](https://www.youtube.com/playlist?list=PLltVQYLz1BMCsJDDj7jj3Ea0vGVOCv4Nr)

การแปลง Code จาก .ui ไปเป็น .py


        pyuic5 -x [file.ui] -o [file.py]

Example


        pyuic5 -x IotApp-BAS.ui -o IotApp-BAS.py

Example ใส่ Event ให้ปุ๋ม  ดังนี้

        def function_x(self):
            print('Hello')

        def retranslateUi(self, MyApp):
            self.btnStart.clicked.conect(self.[function_x])
