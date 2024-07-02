internal class Program
{
    private static void Main(string[] args)
    {
        var solution = new ReverseOnlyLettersSolution();
        solution.ReverseOnlyLetters("7_28]");
    }
}

public class ReverseOnlyLettersSolution {


    public string ReverseOnlyLetters(string s) {
        if (string.IsNullOrWhiteSpace(s)) {return s;}

        int len = s.Length;
        int i = 0;
        int j = len - 1;
        var res = new char[len];

        while (i < j) {
            while (!Char.IsLetter(s[i]) && i < j) {
                res[i] = s[i];
                i++; 
            }
            while (!Char.IsLetter(s[j]) && i < j) { 
                res[j] = s[j];
                j--;
            }

            res[i] = s[j];
            res[j] = s[i];
            i++;
            j--;
        }
        if (i == j) {
            res[i] = s[i];
        }

        return new String(res);
    }
}