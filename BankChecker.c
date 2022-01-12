using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace BankChecker
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] bank = {"Citadelė","Swedbank","Luminor","Nodea","Revolut","SEB","Medicinos bankas","Šiaulių bankas"};
           
            int[] bankId = {72900,73000,40100,21400,39200,70440,72300,71800};

            while (true)
            {
                Console.WriteLine("Įveskite banko sąskaitos numerį: ");

                string bankNumber = Console.ReadLine();
                bankNumber = Regex.Replace(bankNumber, @"\s", "");

                string lithuanianId = "LT";

                if (bankNumber.Substring(0, 2) != lithuanianId)
                {
                    Console.WriteLine("Lietuviškų bankų sąskaitos prasideda raidėmis LT");
                }
                else if (bankNumber.Length < 20 || bankNumber.Length > 20)
                {
                    Console.WriteLine("Per mažai arba per daug raidžių ar spec. simbolių");
                }
                else if (long.TryParse(bankNumber.Substring(2, 18), out _) == false)
                {
                    Console.WriteLine("Sąskaitos numeris po LT negali turėti simbolių");
                }
                else
                {
                    long bankIdCode = Int64.Parse(bankNumber.Substring(4, 5)); 
                    long bankCodeIndex = Array.IndexOf(bankId, Convert.ToInt32(bankIdCode));

                    string bankName = bank[bankCodeIndex];

                    Console.WriteLine($"Banko sąskaita {bankNumber} patvirtinta. Bankas: {bankName}.");
                    break;
                }

            }
        }
        
    }
}
