using System;

namespace PersonalNumberChecker
{
    class PersonalNumberChecker
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("Įvesk asmens kodą: ");

                string personalNumber = Console.ReadLine();

                if (long.TryParse(personalNumber, out _) == false)
                {
                    Console.WriteLine("Asmens kodas turi būti sudarytas tik iš skaičių");
                }
                else if (personalNumber[0] != '3' && personalNumber[0] != '4')
                {
                    Console.WriteLine("Asmens kodas turėtu prasidėti skaičiumi 3 arba 4");
                }
                else if (personalNumber.Length < 11 || personalNumber.Length > 11)
                {
                    Console.WriteLine("Įvedei per mažai arba per daug skaičių - bandyk dar kartą");
                }
                else
                {
                    Console.WriteLine("Tavo asmens kodas yra: " + personalNumber);
                    break;
                }
                    
                
            }
                
        }
    }
}
