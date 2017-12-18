using System;
using System.Windows;
using System.Windows.Controls;
using Test01.Elements;

namespace Test01
{
    public partial class MyStackPanel : StackPanel
    {
        public MyStackPanel()
        {
            DataContext = this;
            InitializeComponent();
        }

        public void Up(IElement source)
        {
            if (!(source is UIElement uiElement))
                throw new Exception("source not an UIElement");

            var index = Children.IndexOf(uiElement);
            if (index == 0)
                return;
            
            Children.RemoveAt(index);
            Children.Insert(index - 1, uiElement);
        }

        public void Down(IElement source)
        {
            if (!(source is UIElement uiElement))
                throw new Exception("source not an UIElement");

            var index = Children.IndexOf(uiElement);
            var childrenCount = Children.Count;
            if (index == childrenCount - 1)
                return;

            Children.RemoveAt(index);
            Children.Insert(index + 1, uiElement);
        }
    }
}
