using System;

/// Write a program that picks a random number between 1 and 10. Give the user 4 chances to guess the number. 
/// If the user guesses the number, display “You won". Otherwise, display “You lost".

namespace Udemy
{
    class Program
    {
        static void Main(string[] args)
        {
        var number = new Random().Next(1, 10);

        for (var i = 0; i < 4; i++)
            {
                Console.Write("Guess the number from 1-10: ");
                var guess = Int32.Parse(Console.ReadLine());

                if (guess == number)
                {
                    Console.WriteLine("Correct! The number was {0}", number);
                }
            }
        Console.WriteLine("Almost... The number was {0}", number);
        }
    }
}
