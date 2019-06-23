import wpf

from System.Windows import Application, Window
from System.Windows.Controls import Label, StackPanel


class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, r'D:\git\ipy\ch9_wpf\wpfFromXAML.xaml')
        
    def button_Click(self, sender, e):
        print('clicked', sender.Content, e, self)

        msg = Label(Content='Welcome to IronPython!', FontSize=26)
        
        for c in self.LogicalChildren:
            if isinstance(c,StackPanel) and c.Name == "stackPanel":
                print(c)
                c.AddChild(msg)


def main():
    Application().Run(MyWindow())


if __name__ == '__main__':
    main()
