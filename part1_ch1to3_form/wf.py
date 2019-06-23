import clr
clr.AddReference("System.Windows.Forms", "System.Drawing")

from System.Windows.Forms import (
    Application, Form, 
    FormBorderStyle, Label
)

from System.Drawing import (
    Color, Font, FontStyle, Point
)

win = Form(Text="Hello World", FormBorderStyle=FormBorderStyle.Fixed3D, Height=150)

newFont = Font("Verdana", 16, FontStyle.Bold | FontStyle.Italic)

label = Label(AutoSize=True, Text="My Hello World Label", Location=Point(10, 50), BackColor=Color.Aquamarine, ForeColor=Color.DarkMagenta, Font=newFont)

win.Controls.Add(label)

print(len(win.Controls))

Application.Run(win)
