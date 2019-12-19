import tkinter as tk
from functools import partial

from lab_9.tools.calculator import Calculator


class CalculatorGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.variables = {}
        self.state = tk.BooleanVar(value=True)
        self.init_variables()
        self.calculator = Calculator()

        self.screen = tk.Label(self, bg='white')
        self.screen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottom_pad = self.init_bottom_pad()
        self.bottom_pad.pack(side=tk.BOTTOM)

        

    def init_variables(self):
        self.variables['var_1'] = ''
        self.variables['var_2'] = ''
        self.variables['operator'] = ''
        self.state.set(True)

    def init_bottom_pad(self):
        bottom_pad = tk.Frame(self)

        # klawiatura numeryczna
        num_pad = tk.Frame(bottom_pad)
        num_pad.pack(side=tk.LEFT)
        ii = 0
        for ii, num in enumerate(range(9, 0, -1)):
            tk.Button(
                num_pad, text=num, width=5,
                command=partial(self.update_var, num)
            ).grid(row=ii // 3, column=(2-ii) % 3 +1)
        ii += 1
        tk.Button(
            num_pad, text='MC', width=5,
            command=self.calculator.clean_memory
        ).grid(row=0, column= 0)
        tk.Button(
            num_pad, text='MR', width=5,
            command=self.memory_load
        ).grid(row=1, column= 0)
        tk.Button(
            num_pad, text='M+', width=5,
            command=self.calculator.memorize
        ).grid(row=2, column= 0)
        ii += 3
        tk.Button(
            num_pad, text='C', width=5,
            command=self.clear
        ).grid(row=ii // 4, column=ii % 4)
        ii += 1
        tk.Button(
            num_pad, text='0', width=5,
            command=partial(self.update_var, '0')
        ).grid(row=ii // 4, column=ii % 4)
        ii += 1
        tk.Button(
            num_pad, text='.', width=5,
            command=partial(self.update_var, '.')
        ).grid(row=ii // 4, column=ii % 4)
        ii += 1
        tk.Button(
            num_pad, text='=', width=5,
            command=self.calculate_result
        ).grid(row=ii // 4, column=ii % 4)

        

        # klawiatura operacji
        operation_pad = tk.Frame(bottom_pad)
        operation_pad.pack(side=tk.RIGHT)
        for ii, operation in enumerate(self.calculator.operations.keys()):
            tk.Button(
                operation_pad, text=operation, width=5,
                command=partial(self.set_operator, operation),
            ).grid(row=ii, column=0)

        return bottom_pad

    def update_screen(self):
        text = f"{self.variables['var_1']}"
        if self.variables['operator']:
            text += f" {self.variables['operator']}"
        if self.variables['var_2']:
            text += f" {self.variables['var_2']}"
        self.screen['text'] = text

    def clear(self):
        state = self.state.get()
        if state:
            self.variables['var_1'] = ''
        else:
            self.variables['var_2'] = ''
        self.update_screen()

    def update_var(self, num):
        state = self.state.get()

        if state:
            if num == "." and num in self.variables['var_1']:
                return None
            self.variables['var_1'] += str(num)
            self.variables['var_1'] = self.variables['var_1'].lstrip('0')
        else:
            if num == "." and num in self.variables['var_2']:
                return None
            self.variables['var_2'] += str(num)
            self.variables['var_2'] = self.variables['var_2'].lstrip('0')
        self.update_screen()

    def set_operator(self, operator):
        if self.variables['var_1']:
            self.variables['operator'] = operator
            self.state.set(not self.state.get())
            self.update_screen()

    def calculate_result(self):
        if self.variables['var_1'] and self.variables['var_2']:
            var_1 = float(self.variables['var_1'])
            var_2 = float(self.variables['var_2'])
            self.screen['text'] = self.calculator.run(
                self.variables['operator'], var_1, var_2
            )
            self.init_variables()

    def memory_load(self):
        state = self.state.get()
        if state:
            self.variables['var_1'] += str(self.calculator.memory)
            self.variables['var_1'] = self.variables['var_1'].lstrip('0')
            self.state.set(not self.state.get())
        else:
            self.variables['var_2'] += str(self.calculator.memory)
            self.variables['var_2'] = self.variables['var_2'].lstrip('0')
        self.update_screen()
        
def keyEq(event):
    event.widget.calculate_result()
    
def keyMul(event):
    event.widget.set_operator("*")
    
def keyDiv(event):
    event.widget.set_operator("/")
    
def keyAdd(event):
    event.widget.set_operator("+")
    
def keySub(event):
    event.widget.set_operator("-")

def key(event):
    if event.keycode == 48:
        event.widget.update_var(0)
    elif event.keycode == 49:
        event.widget.update_var(1)
    elif event.keycode == 50:
        event.widget.update_var(2)
    elif event.keycode == 51:
        event.widget.update_var(3)
    elif event.keycode == 52:
        event.widget.update_var(4)
    elif event.keycode == 53:
        event.widget.update_var(5)
    elif event.keycode == 54:
        event.widget.update_var(6)
    elif event.keycode == 55:
        event.widget.update_var(7)
    elif event.keycode == 56:
        event.widget.update_var(8)
    elif event.keycode == 57:
        event.widget.update_var(9)
    elif event.keycode == 188 or event.keycode == 190:
        event.widget.update_var(".")

if __name__ == '__main__':
    root = tk.Tk()
    cal = CalculatorGUI(root)
    cal.focus_set()
    cal.bind("<Return>", keyEq)
    cal.bind("/", keyDiv)
    cal.bind("*", keyMul)
    cal.bind("+", keyAdd)
    cal.bind("-", keySub)
    cal.bind("<Key>", key)
    cal.pack()

    root.mainloop()