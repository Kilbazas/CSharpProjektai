using System;
using System.Collections.Generic;

//Write a program and continuously ask the user to enter different names,
//until the user presses Enter (without supplying a name). 
//Depending on the number of names provided, display a message based on the above pattern.

namespace Udemy
{
    class Program
    {
        static void Main(string[] args)
        {
            var names = new List<string>();

            while (true)
            {
                Console.WriteLine("What is the name? (If you want to break press ENTER): ");

                var input = Console.ReadLine();
                if (input == "")
                {
                    break;
                }
                names.Add(input);
            }
            if (names.Count > 2)
            {
                Console.WriteLine("{0}, {1} and {2} liked your post", names[0], names[1], names[2]);
            }
            else if (names.Count == 2)
            {
                Console.WriteLine("{0} and {1} liked your post", names[0], names[1]);
            }
            else if (names.Count == 1)
            {
                Console.WriteLine("{0} liked your post", names[0]);
            }
            else
            {
                Console.WriteLine();
            }
        }
    }
}
