// Copyright Nick Polyak 2008

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Controls.Primitives;

namespace DragDropTest
{
    // delegate for GetPosition function of DragEventArgs and
    // MouseButtonEventArgs event argument objects. This delegate is used to reuse the code
    // for processing both types of events.
    delegate Point GetPositionDelegate(IInputElement element);

    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class Window1 : Window
    {
        int oldIndex = -1;

        public Window1()
        {
            InitializeComponent();

            ListView1.PreviewMouseLeftButtonDown += new MouseButtonEventHandler(ListView1_PreviewMouseLeftButtonDown);
            ListView1.Drop += new DragEventHandler(ListView1_Drop);
        }

        // function called during drop operation
        void ListView1_Drop(object sender, DragEventArgs e)
        {
            if (oldIndex < 0)
                return;

            int index = this.GetCurrentIndex(e.GetPosition);

            if (index < 0)
                return;

            if (index == oldIndex)
                return;

            Shapes myShapes = Resources["MyShapes"] as Shapes;

            Shape movedShape = myShapes[oldIndex];
            myShapes.RemoveAt(oldIndex);

            myShapes.Insert(index, movedShape);
        }

        void ListView1_PreviewMouseLeftButtonDown(object sender, MouseButtonEventArgs e)
        {
            oldIndex = this.GetCurrentIndex(e.GetPosition);

            if (oldIndex < 0)
                return;

            ListView1.SelectedIndex = oldIndex;
            Shape selectedItem = this.ListView1.Items[oldIndex] as Shape;

            if (selectedItem == null)
                return;

            // this will create the drag "rectangle"
            DragDropEffects allowedEffects = DragDropEffects.Move;
            if (DragDrop.DoDragDrop(this.ListView1, selectedItem, allowedEffects) != DragDropEffects.None)
            {
                // The item was dropped into a new location,
                // so make it the new selected item.
                this.ListView1.SelectedItem = selectedItem;
            }
        }

        ListViewItem GetListViewItem(int index)
        {
            if (ListView1.ItemContainerGenerator.Status != GeneratorStatus.ContainersGenerated)
                return null;

            return ListView1.ItemContainerGenerator.ContainerFromIndex(index) as ListViewItem;
        }

        // returns the index of the item in the ListView
        int GetCurrentIndex(GetPositionDelegate getPosition)
        {
            int index = -1;
            for (int i = 0; i < this.ListView1.Items.Count; ++i)
            {
                ListViewItem item = GetListViewItem(i);
                if (this.IsMouseOverTarget(item, getPosition))
                {
                    index = i;
                    break;
                }
            }
            return index;
        }

        bool IsMouseOverTarget( Visual target, GetPositionDelegate getPosition)
		{
			Rect bounds = VisualTreeHelper.GetDescendantBounds( target );
			Point mousePos = getPosition((IInputElement) target);
			return bounds.Contains( mousePos );
		}
    }
}
