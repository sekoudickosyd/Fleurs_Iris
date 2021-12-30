import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import iris_flowers_prediction as iris_fp
import sys
import  pickle
import numpy as np
import  warnings
warnings.filterwarnings('ignore')

# Fonctions

def reset():
    # Line Edit Sepal Length
    ui.le_sl.setStyleSheet(""" color: rgb(214, 214, 214);
                           font: 12pt MS Shell Dlg 2""")
    ui.le_sl.setText('Enter a value between 4.3 and 7.9')

    # Line Edit Sepal Width
    ui.le_sw.setStyleSheet(""" color: rgb(214, 214, 214);
                           font: 12pt MS Shell Dlg 2""")
    ui.le_sw.setText('Enter a value between 2.0 and 4.4')

    # Line Edit Petal Length
    ui.le_pl.setStyleSheet(""" color: rgb(214, 214, 214);
                           font: 12pt MS Shell Dlg 2""")
    ui.le_pl.setText('Enter a value between 1.0 and 6.9')

    # Line Edit Petal Width
    ui.le_pw.setStyleSheet(""" color: rgb(214, 214, 214);
                           font: 12pt MS Shell Dlg 2""")
    ui.le_pw.setText('Enter a value between 0.1 and 2.5')



def quit_method():
    w.close()

def le_sl_text_method():
    ui.le_sl.setStyleSheet("""color: rgb(104, 104, 104);
                           font: 14pt MS Shell Dlg 2""")

def le_sw_text_method():

    ui.le_sw.setStyleSheet("""color: rgb(104, 104, 104);
                           font: 14pt MS Shell Dlg 2""")

def le_pl_text_method():

    ui.le_pl.setStyleSheet("""color: rgb(104, 104, 104);
                           font: 14pt MS Shell Dlg 2""")

def le_pw_text_method():

    ui.le_pw.setStyleSheet("""color: rgb(104, 104, 104);
                           font: 14pt MS Shell Dlg 2""")

def prediction():
    with open('./Ressources/model.pickle', 'rb') as pic:
        model = pickle.load(pic)

    sepal_length = ui.le_sl.text()
    sepal_width = ui.le_sw.text()
    petal_length = ui.le_pl.text()
    petal_width = ui.le_pw.text()

    if (sepal_length!='Enter a value between 4.3 and 7.9'
            and sepal_width!='Enter a value between 2.0 and 4.4'
            and petal_length!='Enter a value between 1.0 and 6.9'
            and petal_width!='Enter a value between 0.1 and 2.5'):

        sepal_length = float(sepal_length)
        sepal_width = float(sepal_width)
        petal_length = float(petal_length)
        petal_width = float(petal_width)

        classe = ['setosa', 'versicolor', 'virginica']
        X = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape((1, 4))
        y = model.predict(X)[0] - 1

        photo = './Ressources/' + classe[y] + '.png'
        ui.lbl_classe.setPixmap(QtGui.QPixmap(photo))

    else :
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Données d'Iris")
        msg.setText("SVP, veuillez entrer tous les champs !")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        x = msg.exec_()

        reset()



# Interface graphique

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = iris_fp.Ui_MainWindow()
ui.setupUi(MainWindow)

reset()

ui.le_sl.textChanged.connect(le_sl_text_method)

ui.le_sw.textChanged.connect(le_sw_text_method)

ui.le_pl.textChanged.connect(le_pl_text_method)

ui.le_pw.textChanged.connect(le_pw_text_method)

# Bouton Quitter
ui.btn_quit.clicked.connect(quit_method)

# Predict
ui.btn_predict.clicked.connect(prediction)

w = QtWidgets.QStackedWidget()
w.setFixedWidth(838)
w.setFixedHeight(549)
w.addWidget(MainWindow)
w.setWindowTitle('IRIS FLOWERS PREDICTION')
w.setWindowIcon(QtGui.QIcon('./Ressources/logo.png'))
w.show()
sys.exit(app.exec_())