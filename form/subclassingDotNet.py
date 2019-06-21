import clr

clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import (
Application, Form,
FormBorderStyle, Label, Button
)

from System.Drawing import (
Color, Font, FontStyle, Point
)

class MainForm(Form):
    def __init__(self):
        self.Text = "Hello World"
        self.FormBorderStyle = FormBorderStyle.Fixed3D
        self.Height = 150
        newFont = Font("Verdana", 16,
        FontStyle.Bold | FontStyle.Italic)
        label = Label()
        label.AutoSize = True
        label.Text = "My Hello World Label"
        label.Font = newFont
        label.BackColor = Color.Aquamarine
        label.ForeColor = Color.DarkMagenta
        label.Location = Point(10, 50)
        self.Controls.Add(label)

        btn = Button(Text="Click", Location=Point(50, 20), Parent=self)
        btn.Click += self.on_click

    def on_click(self, sender, event):
        print('clicked')
        print(sender, event)


mainForm = MainForm()
Application.Run(mainForm)