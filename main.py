import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
 QPushButton, QRadioButton, QButtonGroup, QTabWidget,
 QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

style_sheet = """
 QWidget{
 background-color: #C92108;
 }
 QWidget#Tabs{
 background-color: #FCEBCD;
 border-radius: 4px
 }
 QWidget#ImageBorder{
 background-color: #FCF9F3;
 border-width: 2px;
 border-style: solid;
 border-radius: 4px;
 border-color: #FABB4C
 }
 QWidget#Side{
 background-color: #EFD096;
 border-radius: 4px
 }
 QLabel{
 background-color: #EFD096;
 border-width: 2px;
 border-style: solid;
 border-radius: 4px;
 border-color: #EFD096
 }
 QLabel#Header{
 background-color: #EFD096;
 border-width: 2px;
 border-style: solid;
 border-radius: 4px;
 border-color: #EFD096;
 padding-left: 10px;
 color: #961A07
 }
 QLabel#ImageInfo{
 background-color: #FCF9F3;
 border-radius: 4px;
 }
 QGroupBox{
 background-color: #FCEBCD;
 color: #961A07
 }
 QRadioButton{
 background-color: #FCF9F3
 }
 QPushButton{
 background-color: #C92108;
 border-radius: 4px;
 padding: 6px;
 color: #FFFFFF
 }
 QPushButton:pressed{
 background-color: #C86354;
 border-radius: 4px;
 padding: 6px;
 color: #DFD8D7
 }
"""
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(700, 700)
        self.setWindowTitle("6.1 - GUI заказа еды")

        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.tab_bar = QTabWidget()
        self.pizza_tab = QWidget()
        self.pizza_tab.setObjectName("Tabs")
        self.wings_tab = QWidget()
        self.wings_tab.setObjectName("Tabs")

        self.tab_bar.addTab(self.pizza_tab, "Пицца")
        self.tab_bar.addTab(self.wings_tab, "Крылышки")

        self.pizzaTab()
        self.wingsTab()
        self.side_widget = QWidget()
        self.side_widget.setObjectName("Tabs")

        order_label = QLabel("ВАШ ЗАКАЗ")
        order_label.setObjectName("Header")

        items_box = QWidget()
        items_box.setObjectName("Side")
        pizza_label = QLabel("Тип пиццы: ")
        self.display_pizza_label = QLabel("")
        toppings_label = QLabel("Начинки: ")
        self.display_toppings_label = QLabel("")
        extra_label = QLabel("Дополнительно: ")
        self.display_wings_label = QLabel("")

        items_grid = QGridLayout()
        items_grid.addWidget(pizza_label, 0, 0,
        Qt.AlignmentFlag.AlignRight)
        items_grid.addWidget(self.display_pizza_label, 0, 1)
        items_grid.addWidget(toppings_label, 1, 0,
        Qt.AlignmentFlag.AlignRight)
        items_grid.addWidget(self.display_toppings_label, 1, 1)
        items_grid.addWidget(extra_label, 2, 0,
        Qt.AlignmentFlag.AlignRight)
        items_grid.addWidget(self.display_wings_label, 2, 1)
        items_box.setLayout(items_grid)


        side_v_box = QVBoxLayout()
        side_v_box.addWidget(order_label)
        side_v_box.addWidget(items_box)
        side_v_box.addStretch()
        self.side_widget.setLayout(side_v_box)
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.tab_bar, 1)
        main_h_box.addWidget(self.side_widget)
        self.setLayout(main_h_box)
    def pizzaTab(self):
         tab_pizza_label = QLabel("СОЗДАЙТЕ СВОЮ СОБСТВЕННУЮ ПИЦЦУ")
         tab_pizza_label.setObjectName("Header")
         description_box = QWidget()
         description_box.setObjectName("ImageBorder")
         pizza_image_path = "images/pizza.png"
         pizza_image = self.loadImage(pizza_image_path)
         pizza_desc = QLabel()
         pizza_desc.setObjectName("ImageInfo")
         pizza_desc.setText(
         """<p>Создаем для вас пиццу на заказ. Начните с
         вашего любимого коржа и добавьте любые начинки, а также
         идеальное количество сыра и соуса.</p>""")
         pizza_desc.setWordWrap(True)
         pizza_desc.setContentsMargins(10, 10, 10, 10)
         pizza_h_box = QHBoxLayout()
         pizza_h_box.addWidget(pizza_image)
         pizza_h_box.addWidget(pizza_desc, 1)
         description_box.setLayout(pizza_h_box)
         crust_gbox = QGroupBox()
         crust_gbox.setTitle("ВЫБОР ВАШЕГО КОРЖА")
         self.crust_group = QButtonGroup()
         gb_v_box = QVBoxLayout()
         crust_list = ["Ручной", "Плоский", "Фаршированный"]
         for cr in crust_list:
            crust_rb = QRadioButton(cr)
            gb_v_box.addWidget(crust_rb)
            self.crust_group.addButton(crust_rb)

         crust_gbox.setLayout(gb_v_box)
         toppings_gbox = QGroupBox()
         toppings_gbox.setTitle("ВЫБЕРИТЕ НАЧИНКУ")

         self.toppings_group = QButtonGroup()
         gb_v_box = QVBoxLayout()

         toppings_list = ["Пепперони", "Колбаса", "Бекон",
         "Канадский бекон", "Говядина", "Ананас",
         "Оливки", "Томат", "Зеленый перец",
         "Грибы", "Лук", "Шпинат", "Сыр"]
         for top in toppings_list:
             toppings_rb = QRadioButton(top)
             gb_v_box.addWidget(toppings_rb)
             self.toppings_group.addButton(toppings_rb)
             self.toppings_group.setExclusive(False)

         toppings_gbox.setLayout(gb_v_box)
         add_to_order_button1 = QPushButton("Добавить к заказу")
         add_to_order_button1.clicked.connect(self.displayPizzaInOrder)

         # Создайте макет для вкладки пиццы (страница 1)
         page1_v_box = QVBoxLayout()
         page1_v_box.addWidget(tab_pizza_label)
         page1_v_box.addWidget(description_box)
         page1_v_box.addWidget(crust_gbox)
         page1_v_box.addWidget(toppings_gbox)
         page1_v_box.addStretch()
         page1_v_box.addWidget(add_to_order_button1, alignment=Qt.AlignmentFlag.AlignRight)

         self.pizza_tab.setLayout(page1_v_box)

    def wingsTab(self):
         tab_wings_label = QLabel("ПРОБУЙТЕ НАШИ УДИВИТЕЛЬНЫЕ КРЫЛЫШКИ")
         tab_wings_label.setObjectName("Header")
         description_box = QWidget()
         description_box.setObjectName("ImageBorder")
         wings_image_path = "images/wings.png"
         wings_image = self.loadImage(wings_image_path)
         wings_desc = QLabel()
         wings_desc.setObjectName("ImageInfo")
         wings_desc.setText(
             """<p>6 кусочков белого мяса с насыщенным вкусом
             курицы, которые заставят вас вернуться за добавкой.</p>""")
         wings_desc.setWordWrap(True)
         wings_desc.setContentsMargins(10, 10, 10, 10)
         wings_h_box = QHBoxLayout()
         wings_h_box.addWidget(wings_image)
         wings_h_box.addWidget(wings_desc, 1)
         description_box.setLayout(wings_h_box)
         wings_gbox = QGroupBox()
         wings_gbox.setTitle("ВЫБЕРИТЕ СВОЙ ВКУС")
         self.wings_group = QButtonGroup()
         gb_v_box = QVBoxLayout()
         flavors_list = ["Баффало", "Кисло-сладкий", "Терияки", "Барбекю"]
         for fl in flavors_list:
             flavor_rb = QRadioButton(fl)
             gb_v_box.addWidget(flavor_rb)
             self.wings_group.addButton(flavor_rb)

         wings_gbox.setLayout(gb_v_box)


         add_to_order_button2 = QPushButton("Добавить к заказу")
         add_to_order_button2.clicked.connect(self.displayWingsInOrder)

         page2_v_box = QVBoxLayout()
         page2_v_box.addWidget(tab_wings_label)
         page2_v_box.addWidget(description_box)
         page2_v_box.addWidget(wings_gbox)
         page2_v_box.addWidget(add_to_order_button2,
         alignment=Qt.AlignmentFlag.AlignRight)
         page2_v_box.addStretch()
         self.wings_tab.setLayout(page2_v_box)
    def displayPizzaInOrder(self):
         if self.crust_group.checkedButton():
             text = self.crust_group.checkedButton().text()
             self.display_pizza_label.setText(text)
             toppings = self.collectToppingsInList()
             toppings_str = '\n'.join(toppings)
             self.display_toppings_label.setText(toppings_str)
             self.update()
    def displayWingsInOrder(self):
         if self.wings_group.checkedButton():
             text = self.wings_group.checkedButton().text() +\
             " Крылышки"
         self.display_wings_label.setText(text)
         self.update()


    def collectToppingsInList(self):

        toppings_list = [button.text() for i, button in \
                         enumerate(self.toppings_group.buttons()) if \
                         button.isChecked()]
        return toppings_list
    def loadImage(self, img_path):
         aspect = Qt.AspectRatioMode.KeepAspectRatioByExpanding
         transform = Qt.TransformationMode.SmoothTransformation
         try:
             with open(img_path):
                image = QLabel(self)
                image.setObjectName("ImageInfo")
                pixmap = QPixmap(img_path)
                image.setPixmap(pixmap.scaled(image.size(), aspect, transform))
                return image
         except FileNotFoundError as error:
             print(f"Изображение не найдено. Ошибка: {error}")
        
if __name__ == '__main__':
 app = QApplication(sys.argv)
 app.setStyleSheet(style_sheet)
 window = MainWindow()
 sys.exit(app.exec())