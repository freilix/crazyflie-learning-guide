// copyright Nick Polyak 2008

using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;

namespace DragDropTest
{
    // object behind the List Items (ItemsSource of the list is set to
    // a collection of Shape objects)
    public class Shape
    {
        string _name = null;
        string _numSides = null;

        public Shape()
        {
        }

        public Shape(string name, string description)
        {
            this._name = name;
            this._numSides = description;
        }

        public string Name
        {
            get
            {
                return _name;
            }

            set
            {
                _name = value;
            }
        }

        public string NumSides
        {
            get
            {
                return _numSides;
            }

            set
            {
                _numSides = value;
            }
        }
    }

    // Collection of Shape objects
    public class Shapes : ObservableCollection<Shape>
    {
        public Shapes()
        {
            Add(new Shape("Circle", "0"));
            Add(new Shape("Triangle", "3"));
            Add(new Shape("Rectangle", "4"));
            Add(new Shape("Pentagon", "5"));
        }
    }
}