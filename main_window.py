from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500, 400)
        self.init_ui()
        self.connect_signals()
        self.update_counter()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        input_label = QLabel("Новая задача")
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.add_button = QPushButton("Добавить")
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        self.task_list = QListWidget()

        self.delete_button = QPushButton("Удалить")
        self.clear_button = QPushButton("Очистить всё")
        delete_layout = QHBoxLayout()
        delete_layout.addWidget(self.delete_button)
        delete_layout.addWidget(self.clear_button)

        self.complete_button = QPushButton("Выполнить / вернуть")
        self.edit_button = QPushButton("Редактировать")
        edit_layout = QHBoxLayout()
        edit_layout.addWidget(self.complete_button)
        edit_layout.addWidget(self.edit_button)

        self.counter_label = QLabel()
        self.completed_label = QLabel()
        counter_layout = QHBoxLayout()
        counter_layout.addWidget(self.counter_label)
        counter_layout.addStretch()
        counter_layout.addWidget(self.completed_label)

        main_layout.addWidget(input_label)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list, 1)
        main_layout.addLayout(delete_layout)
        main_layout.addLayout(edit_layout)
        main_layout.addLayout(counter_layout)

    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.clear_button.clicked.connect(self.clear_tasks)
        self.complete_button.clicked.connect(self.toggle_task_completion)
        self.edit_button.clicked.connect(self.edit_task)
        self.task_list.itemChanged.connect(self.update_counter)

    def add_task(self):
        text = self.task_input.text().strip()
        if not text:
            QMessageBox.warning(self, "Пустая задача", "Введите название задачи")
            return

        item = QListWidgetItem(text)
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        item.setCheckState(Qt.CheckState.Unchecked)
        self.task_list.addItem(item)
        self.task_input.clear()
        self.update_counter()

    def delete_task(self):
        row = self.task_list.currentRow()
        if row < 0 or not self.task_list.selectedItems():
            QMessageBox.warning(self, "Удаление задачи", "Выберите задачу для удаления")
            return

        answer = QMessageBox.question(
            self,
            "Удаление задачи",
            "Удалить выбранную задачу?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.takeItem(row)
            self.update_counter()

    def clear_tasks(self):
        if self.task_list.count() == 0:
            return

        answer = QMessageBox.question(
            self,
            "Очистка списка",
            "Удалить все задачи?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.clear()
            self.update_counter()

    def toggle_task_completion(self):
        item = self.task_list.currentItem()
        if item is None or not item.isSelected():
            QMessageBox.warning(self, "Выполнение задачи", "Выберите задачу")
            return

        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)

    def edit_task(self):
        item = self.task_list.currentItem()
        if item is None or not item.isSelected():
            QMessageBox.warning(self, "Редактирование задачи", "Выберите задачу")
            return

        text, accepted = QInputDialog.getText(
            self, "Редактирование задачи", "Название задачи:", text=item.text()
        )
        if not accepted:
            return
        text = text.strip()
        if not text:
            QMessageBox.warning(self, "Пустая задача", "Введите название задачи")
            return

        item.setText(text)

    def update_counter(self):
        count = self.task_list.count()
        completed = sum(
            self.task_list.item(row).checkState() == Qt.CheckState.Checked
            for row in range(count)
        )
        self.counter_label.setText(f"Количество задач: {count}")
        self.completed_label.setText(f"Выполнено задач: {completed}")
