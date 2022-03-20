from math import frexp
from tkinter import *
from tkinter.messagebox import *
class Caluclator:
    def __init__(self) -> None:
        self.screenText = StringVar()
        self.screenText.set('')
        self.screen = Entry(textvariable=self.screenText, font="Times 20 bold normal", fg='black', bg='white', width=12)
        root.bind('<Key>', self.eventCallback)
        self.screen.grid(row=0, column=0, columnspan=4)
        self.buttonsText = [['OFF', '%', 'CE', 'C'], ['7', '8', '9', '/'], ['4', '5', '6', '*'], ['1', '2', '3', '-'], ['0', '.', '=', '+']]
        self.buttons = [[0 for c in range(4)]for r in range(5)]
        for r in range(5):
            for c in range(4):
                if self.buttonsText[r][c] == 'OFF':
                    self.buttons[r][c] = Button(text=f'{self.buttonsText[r][c]}', font="Times 20 bold normal", bg='red', fg='white', width=3, command = self.off)
                elif self.buttonsText[r][c] == 'C':
                    self.buttons[r][c] = Button(text=f'{self.buttonsText[r][c]}', font="Times 20 bold normal", bg='blue', fg='white', width=3, command = self.clear)
                elif self.buttonsText[r][c] == 'CE':
                    self.buttons[r][c] = Button(text=f'{self.buttonsText[r][c]}', font="Times 20 bold normal", bg='blue', fg='white', width=3, command = self.clearAll)                                   
                elif self.buttonsText[r][c] == '=':
                    self.buttons[r][c] = Button(text=f'{self.buttonsText[r][c]}', font="Times 20 bold normal", bg='green', fg='white', width=3, command = lambda per = False: self.calculate(per))
                elif self.buttonsText[r][c] == '%':
                    self.buttons[r][c] = Button(text=f'{self.buttonsText[r][c]}', font="Times 20 bold normal", bg='grey', fg='white', width=3, command = lambda per = True: self.calculate(per))
                else:
                    self.buttons[r][c] = Button(text=f'{self.buttonsText[r][c]}', font="Times 20 bold normal", bg='grey', fg='white', width=3, command = lambda row=r, col=c: self.screenInput(row, col))
                self.buttons[r][c].grid(row=r+1, column=c)

    def eventCallback(self, event: Event):
        key = event.keysym
        print(key)
        signsEvent = {'plus':'+', 'slash':'/', 'minus':'-', 'asterisk':'*', 'percent':'%', 'period':'.'}
        if key.isdigit():
            pass
#            newText = self.screenText.get() + key
#            if len(newText)<13:
#                self.screenText.set(newText)
        elif key == 'BackSpace':
            pass
#            newText = self.screenText.get()
#            self.screenText.set(newText[:-1])
        elif key in signsEvent.keys():
            pass
#            newText = self.screenText.get() + signsEvent[key]
#            if len(newText)<13:
#                self.screenText.set(newText)            
        elif key == 'Return' or key == 'equal':
            self.calculate(False)
        else:
            pass

    def screenInput(self, r, c):
        text = self.buttonsText[r][c]
        newText = self.screenText.get() + text
#        if len(newText)<13:
        self.screenText.set(newText)

    def off(self):
        root.destroy()

    def clear(self):
        newText = self.screenText.get()
        self.screenText.set(newText[:-1])       

    def clearAll(self):
        self.screenText.set('')

    def calculate(self, per: bool):
        try:
            answer = eval(self.screenText.get())   
            if per == True:
                answer = answer/100
            if type(answer) == int:
                self.screenText.set(str(answer))
            elif type(answer) == float:
                if len(str(answer)[:str(answer).index('.')]) > 9:
                    self.screenText.set(f'{answer:.4e}')
                else:
                    beforePoint = len(str(answer)[:str(answer).index('.')])
                    formatedAnswer = round(answer, 12-(beforePoint+1))
                    self.screenText.set(f'{formatedAnswer}')
                
        except:
            error = showerror(title='Error!', message='Syntax Error')

if __name__ == '__main__':
    root = Tk()
    c = Caluclator()
    mainloop() 