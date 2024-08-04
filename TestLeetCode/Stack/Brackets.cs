// return true if the input string has balanced brackets, otherwise false
// (a))(
// ((){[]}[>)
// ({foo: [bar}]) -> invalid
// ({foo: [bar]}) -> valid
// (double Sum, int Count) t2 = (4.5, 3);
// Console.WriteLine($"Sum of {t2.Count} elements is {t2.Sum}.");
using System.Collections.Generic;

class ValidBracketSolution
{

bool HasValidBrackets(string input) {
    var stack = new Stack<char>();
    var maps = new Dictionary<char, char>
    {
        { ')', '(' },
        { ']', '[' },
        { '}', '{' },
        { '>', '<' }
    };
    var openBrackets =  new HashSet<char>{ '(', '[', '{', '<' };
    var closeBrackets = new HashSet<char>{')', ']', '}',  '>' };
    
    foreach (var c in input) {
        if (openBrackets.Contains(c)) {
            stack.Push(c);
        }
        else if (closeBrackets.Contains(c)) {
            if (!stack.Any()) { return false; }
            var matching = stack.Pop();
            if (maps[c] != matching) { return false; }
        }
    }
    
    return !stack.Any();
}
}