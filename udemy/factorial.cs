using System;

//3 - write a program and ask the user to enter a number.
//compute the factorial of the number and print it on the console. 
//for example, if the user enters 5, the program should calculate 5 x 4 x 3 x 2 x 1 and display it as 5! = 120.

namespace Udemy
{
    class Program
    {
        static void Main(string[] args)
        {
        Console.Write("Enter a number: ");
        var input = Int32.Parse(Console.ReadLine());

            var factorial = 1;
            for (var i = 1; i <= input; i++)
                factorial *= i;

            Console.WriteLine("{0}! = {1}", input, factorial);
                
        }
    }
}
