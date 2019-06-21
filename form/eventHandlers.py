import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import (
Application, Form,
FormBorderStyle, Label
)

from System.Drawing import (
Color, Font, FontStyle, Point
)

from System import Random
random = Random()

form = Form()
form.Text = "Hello World"
form.FormBorderStyle = FormBorderStyle.Fixed3D
form.Height = 150
newFont = Font("Verdana", 16,
FontStyle.Bold | FontStyle.Italic)
label = Label()
label.AutoSize = True
label.Text = "My Hello World Label"
label.Font = newFont
label.BackColor = Color.Aquamarine
label.ForeColor = Color.DarkMagenta
label.Location = Point(10, 50)
form.Controls.Add(label)

def GetNewColor():
    r = random.Next(256)
    g = random.Next(256)
    b = random.Next(256)
    return Color.FromArgb(r,g,b)

def ChangeColor(sender, event):
    print("X: {0}, Y: {1}".format(event.X, event.Y))
    sender.BackColor = GetNewColor()
    sender.ForeColor = GetNewColor()

label.MouseMove += ChangeColor

Application.Run(form)