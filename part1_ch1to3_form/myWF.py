import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import Application, Form, Label, Button, FormBorderStyle

clr.AddReference("System.Drawing")
from System.Drawing import Point, Color

window = Form(Text="Hello", FormBorderStyle=FormBorderStyle.Fixed3D)
#window.Text = "Hello World"

label = Label(Text="label", BackColor=Color.AliceBlue, ForeColor=Color.Crimson)
window.Controls.Add(label)

#print(len(window.Controls))

button = Button(Text="Click Me", Parent=window, Location=Point(50, 30))


Application.Run(window)
