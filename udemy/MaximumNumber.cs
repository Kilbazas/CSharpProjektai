using System;

namespace Udemy
{
    class Program
    {
        static void Main(string[] args)
        {
            int firstNumber;
            int secondNumber;
            int maximum;

            Console.WriteLine("What is your first number? ");
            firstNumber = Int32.Parse(Console.ReadLine());
            Console.WriteLine("What is your second number? ");
            secondNumber = Int32.Parse(Console.ReadLine());

            if (firstNumber > secondNumber)
            {
                maximum = firstNumber;
            }
            else
            {
                maximum = secondNumber;
            }
            Console.WriteLine("Maximum number = {0}", maximum);
        }
    }
}
