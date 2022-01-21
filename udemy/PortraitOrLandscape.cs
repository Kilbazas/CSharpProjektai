using System;

namespace Udemy
{
    class Program
    {
        static void Main(string[] args)
        {
            int width;
            int height;
            string answer;

            Console.WriteLine("Enter the width: ");
            width = Int32.Parse(Console.ReadLine());
            Console.WriteLine("Enter the height: ");
            height = Int32.Parse(Console.ReadLine());

            if (width > height)
            {
                Console.WriteLine("Your image is landscape.");
            }
            else 
            {
                Console.WriteLine("Your image is portrait.");
            }
        }
    }
}
