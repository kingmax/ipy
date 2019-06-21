import clr
clr.AddReference("PresentationFramework", "PresentationCore")

from System.Windows import (
    Application, SizeToContent, Thickness, Window
    )

from System.Windows.Controls import (
    Button, Label, StackPanel
    )

from System.Windows.Media.Effects import DropShadowBitmapEffect


win = Window(Title="Welcome to IronPython", Width=450)
win.SizeToContent = SizeToContent.Height

stack = StackPanel()
stack.Margin = Thickness(15)
win.Content = stack

button = Button(Content = "Push Me", FontSize=24, BitmapEffect = DropShadowBitmapEffect())

def onClick(sender, event):
    msg = Label()
    msg.FontSize = 36
    msg.Content = 'Welcome to IronPython!'

    stack.Children.Add(msg)

button.Click += onClick
stack.Children.Add(button)

app = Application()
app.Run(win)



