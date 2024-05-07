from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup)
from random import shuffle

class Question():
    def __init__(self, question, right_answer,wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

btn_OK = QPushButton("Ответить")
lb_Question = QLabel("!Вопрос!")

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("1")
rbtn_2 = QRadioButton("2")
rbtn_3 = QRadioButton("3")
rbtn_4 = QRadioButton("4")

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

#панель результата
AnsGroupBox = QGroupBox("Результаты экзамена")
lb_Result = QLabel("прав / неправ")
lb_Correct = QLabel("ответы тут")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

#размещаем линию в окне
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
#RadioGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 2)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    window.cur_question += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

window.cur_question = -1

question_list = []   


question_list.append(Question('Государственный язык Бразилии', 'Бразильский', 'Португальский','Итальянский', 'Испанский'))
question_list.append(Question('В каком году вышла игра "maincraft"', '2011', '2009','2010', '2012'))
question_list.append(Question('Как по-украински будет "зонтик"', 'Парасолька', 'Дощовик','Зонтiк', 'Шпалери'))
question_list.append(Question('В каком году распался СССР', '1991', '1992','1981', '1990'))
question_list.append(Question('Сколько лет в году', '1', '2','3', 'нет правильного ответа'))
question_list.append(Question('Сколько хромосом у человека', '46', '59','34', '28'))
question_list.append(Question('"ЗАЧЕМ" вода в бутылке', 'за стеклом', 'просто так','за водой', 'чтобы пить'))
question_list.append(Question('корень из 121', '11', '12','9', 'нет правильного ответа'))
question_list.append(Question('САмый богатый человек в мире', 'Илон Маск', 'Президент','Космонавт', 'сАмый богатый человек'))
question_list.append(Question('В каком классе заканчивается технология', '7', '8','9', 'НИКОГДА'))
question_list.append(Question('"Основатель" Wildberris', 'Татьяна Бакальчук', 'Илон Маск','Даниэль Фет', 'Испанский'))
question_list.append(Question('"Сколько букв в алфавите', '33','34', '32', "31"))
question_list.append(Question('"кокие цифры входят в двоичный код', '1 0 ', '2 0 ','2 1', '1 2 0'))







btn_OK.clicked.connect(click_OK)
window.resize(400, 300)
next_question()
window.show()

app.exec()



#^-^ \^-^/ /^-^\ -^-^- =^-^= 




#создай приложение для запоминания информации