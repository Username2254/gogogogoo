from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox
from random import shuffle

class question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3 ):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def next_question():
    print(main_win.counter)
    main_win.counter += 1
    if main_win.counter == len(gg):
        main_win.counter = -1
    q=gg[main_win.counter]
    ask(q)

q1 = question ('лучший герой марвел', 'человек паук', 'доктор стрэндж', 'железный чебурек', 'капитан Россия' )
q2 = question ('лучший человек(мем)', 'дядя Серёжа', 'шрек', 'мама я в ютубе', 'я батю в танки выиграл' )
q3 = question ('Лучшая бомба', 'поко', 'пачка Стендофф', 'математичка', 'голодная собака' )

gg = []
gg.append(q1)
gg.append(q2)
gg.append(q3)

def show_correct(res):
    text2.setText(res)
    text1.setText(answers[3].text())

def check_answers():
    if answers[3].isChecked():
       res = 'Правильный ответ'
    else:
        res = 'Неправельный ответ'
    show_correct(res)
def ask (q: question):
    answers[3].setText(q.right_answer)
    answers[0].setText(q.wrong1)
    answers[1].setText(q.wrong2)
    answers[2].setText(q.wrong3)
    text.setText(q.question)
def show_result():
    RadioGroupBox.hide()
    textGroupBox.show()
    button.setText('Следуйщий вопрос')
    # RadioGroupBox.setExclusive(False)
    # Usa.setChecked(False)
    # Usa1.setChecked(False)
    # Usa2.setChecked(False)
    # Usa3.setChecked(False)
    # RadioGroupBox.setExclusive(True)
def show_question():
    textGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')

def start_test():
    if button.text() == 'Ответить':
        check_answers()
        show_result()
    else:
        next_question()
        show_question()

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('текст в канаве')

text = QLabel('лучший мем')
button = QPushButton ('Ответить')
Usa = QRadioButton('шайлушай')
Usa1 = QRadioButton('шрек')
Usa2 = QRadioButton('я в париже')
Usa3 = QRadioButton('скибиди туалет')
text1 = QLabel('Правильный ответ')
text2 = QLabel('правильно/неправильно')
main_win.counter = -1

answers = [Usa, Usa1, Usa2, Usa3]
shuffle(answers)
next_question()
line1 = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()
line4 = QVBoxLayout()
line5 = QHBoxLayout()
line6 = QVBoxLayout()

RadioGroupBox = QGroupBox('Варианты ответов')
textGroupBox = QGroupBox('Результат теста')

line4.addWidget(text, alignment = Qt.AlignHCenter)

line1.addWidget(Usa1)
line1.addWidget(Usa)

line2.addWidget(Usa2)
line2.addWidget(Usa3)

line4.addWidget(textGroupBox)


line4.addWidget(RadioGroupBox)
line4.addLayout(line5)
line4.setSpacing(25)

line5.addStretch(1)
line5.addWidget(button, stretch = 10)
line5.addStretch(1)

line3.addLayout(line1)
line3.addLayout(line2)
RadioGroupBox.setLayout(line3)

line6.addWidget(text2,alignment = (Qt.AlignTop | Qt.AlignLeft))
line6.addWidget(text1, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
textGroupBox.setLayout(line6)

textGroupBox.hide()
button.clicked.connect(start_test)
main_win.setLayout(line4)
main_win.show()
app.exec()