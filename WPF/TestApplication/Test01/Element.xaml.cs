using System;

namespace Test01
{
    public partial class Element
    {
        public Element()
        {
            DataContext = this;
            InitializeComponent();
            UpEnabled = true;
            DownEnabled = true;
        }
        public int Index { get; set; }

        public bool UpEnabled { get; set; }

        public bool DownEnabled { get; set; }

        public ElementType Type { get; }
        public int Value { get; set; }
        
        private void Button_Click_Down(object sender, System.Windows.RoutedEventArgs e)
        {
        }

        private void Button_Click_Up(object sender, System.Windows.RoutedEventArgs e)
        {
        }
    }
}
