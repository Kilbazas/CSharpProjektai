using System;

namespace Udemy
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("What is your lucky number? ");
            var number = Int32.Parse(Console.ReadLine());

            if(number > 0 && number < 10)
            {
                Console.WriteLine("Valid");
            }
            else
            {
                Console.WriteLine("Invalid");
            }
        }
    }
}
