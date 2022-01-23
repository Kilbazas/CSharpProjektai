using System;
using System.Collections.Generic;

//Write a program and ask the user to continuously enter a number or type "Quit" to exit. 
//The list of numbers may include duplicates. 
//Display the unique numbers that the user has entered.

namespace Udemy
{
    class Program
    {
        static void Main(string[] args)
        {
            var numbers = new List<int>();

            while(true)
            {
                Console.WriteLine("Enter the number (or quit to stop): ");

                var input = Console.ReadLine();

                if (input.ToLower() == "quit")
                {
                    break;
                }
                numbers.Add(Int32.Parse(input));

            }
            var uniqueNumber = new List<int>();
            foreach (var number in numbers)
            {
                if (!uniqueNumber.Contains(number))
                {
                    uniqueNumber.Add(number);
                }
            }

            foreach (var number in numbers)
            {
                Console.WriteLine(number);
            }
            Console.WriteLine("Unique numbers:");
            foreach (var number in uniqueNumber)
            {
                Console.WriteLine(number);
            }
        }
    }
}
