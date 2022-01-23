using System;
using System.Collections.Generic;

//Write a program and ask the user to enter 5 numbers. 
//If a number has been previously entered, display an error message and ask the user to re-try. 
//Once the user successfully enters 5 unique numbers, sort them and display the result on the console.

namespace Udemy
{
    class Program
    {
        static void Main(string[] args)
        {
            var numbers = new List<int>();

            while(numbers.Count < 5)
            {
                Console.WriteLine("Enter the number: ");

                var number = Int32.Parse(Console.ReadLine());

                if (numbers.Contains(number))
                {
                    Console.WriteLine("You have already enterd number {0}", number);
                    continue;
                }
                numbers.Add(number);
            }
            numbers.Sort();

            foreach (var number in numbers)
            {
                Console.WriteLine(number);
            }
        
        }
    }
}
