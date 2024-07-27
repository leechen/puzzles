using System;
using System.Collections.Generic;
using System.Linq;

// To execute C#, please define "static void Main" on a class
// named Solution.

// Input => [ "cat", "dog", "tac", "god", "act", "bat" ]

// Output => [["cat", "tac", "act"], ["dog", "god"], ["bat"]]

// c: 1, a: 1, t: 1; 
// act: cat, tac, act
// dgo: dog, god
// nlog(n) n: length of word (max)
// linear: length of Input
// total: K*Nlog(N) [Time]
// space: 2*K*N [space]

// No of words - 1000
// Each word - 10^6 characters



// calc of hash

// ad -> 97 + 100 = 197
// bc -> 98 + 99  = 197

// 26 total:
// a: 1
// b: 50
// c: 50^2
// z: 50^26

class Solution
{
    static void Main(string[] args)
    {   
        List<string> words = new List<string> { "cat", "dog", "tac", "god", "act", "bat" };
        var result = GetAnagrams(words);
        foreach(var group in result) {
            foreach(var word in group) {
                Console.Write(word);
                Console.Write(", ");
            }
            Console.WriteLine();
        }
    }
// [5000, 0 , 1, 0, ... 1, 0,..,50,0] = ....500
//                             0,500] = ....0500
1, 11
11, 1
// "5000,0,1"


// [4000, 1000, 1, 0, ... 1, 0,...] 

    static IList<IList<string>> GetAnagrams(IList<string> input)
    {
        var dict = new Dictionary<string, IList<string>>();
        var map = new int[26];
        
        foreach (var word in input) {            
            var sorted = String.Concat(word.OrderBy(c => c));
            foreach(char ch in word) {
                map[ch - 'a']++;
            }
            var s = constructStringFromMap(map);
            dict[s].Add(word);
        }

        var result = new List<IList<string>>();
        foreach (var entry in map) {
            var group = new List<string>();
            group.AddRange(entry.Value);
            result.Add(group);
        }
        return result;
    }
}


// Your previous Plain Text content is preserved below:

// This is just a simple shared plaintext pad, with no execution capabilities.

// When you know what language you'd like to use for your interview,
// simply choose it from the dots menu on the tab, or add a new language
// tab using the Languages button on the left.

// You can also change the default language your pads are created with
// in your account settings: https://app.coderpad.io/settings

// Enjoy your interview!