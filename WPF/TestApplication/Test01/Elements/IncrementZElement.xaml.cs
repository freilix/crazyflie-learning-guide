using System.Windows.Controls;

namespace Test01.Elements
{
    public partial class IncrementZElement : UserControl, IElement
    {
        public IncrementZElement()
        {
            DataContext = this;
            InitializeComponent();
            UpEnabled = true;
            DownEnabled = true;
        }

        public ElementType Type => ElementType.IncrementZ;
        public int Value { get; set; }
        public int Index { get; set; }
        public bool UpEnabled { get; set; }
        public bool DownEnabled { get; set; }

        public string Serialize()
        {
            return "\"IncrementZElement\": " + Value;
        }

        private void Button_Click_Down(object sender, System.Windows.RoutedEventArgs e)
        {
        }

        private void Button_Click_Up(object sender, System.Windows.RoutedEventArgs e)
        {
        }
    }
}
