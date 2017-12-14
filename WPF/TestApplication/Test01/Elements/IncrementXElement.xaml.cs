using System.Windows.Controls;

namespace Test01.Elements
{
    public partial class IncrementXElement : UserControl, IElement
    {
        public IncrementXElement()
        {
            DataContext = this;
            InitializeComponent();
            UpEnabled = true;
            DownEnabled = true;
        }

        public ElementType Type => ElementType.IncrementX;
        public int Value { get; set; }
        public int Index { get; set; }
        public bool UpEnabled { get; set; }
        public bool DownEnabled { get; set; }

        public string Serialize()
        {
            return "\"IncrementXElement\": " + Value;
        }

        private void Button_Click_Down(object sender, System.Windows.RoutedEventArgs e)
        {
        }

        private void Button_Click_Up(object sender, System.Windows.RoutedEventArgs e)
        {
        }
    }
}
