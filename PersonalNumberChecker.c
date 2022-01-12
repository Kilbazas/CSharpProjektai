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

                string asmensKodas = Console.ReadLine();

                if (long.TryParse(asmensKodas, out _) == false)
                {
                    Console.WriteLine("Asmens kodas turi būti sudarytas tik iš skaičių");
                }
                else if (asmensKodas[0] != '3' && asmensKodas[0] != '4')
                {
                    Console.WriteLine("Asmens kodas turėtu prasidėti skaičiumi 3 arba 4");
                }
                else if (asmensKodas.Length < 11 || asmensKodas.Length > 11)
                {
                    Console.WriteLine("Įvedei per mažai arba per daug skaičių - bandyk dar kartą");
                }
                else
                {
                    Console.WriteLine("Tavo asmens kodas yra: " + asmensKodas);
                    break;
                }
                    
                
            }
                
        }
    }
}
