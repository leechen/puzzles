

class RegexParseSolution
{
    public  bool IsMatch(string text, string pattern)
    {
        
        bool?[,] cache = new bool?[text.Length+1, pattern.Length+1];

        bool Helper(int index, int pIndex) {
            if (cache[index, pIndex].HasValue) {return cache[index, pIndex].Value;}

            if (pIndex == pattern.Length && index == text.Length) {
                return true;
            }
            
            if (pIndex >= pattern.Length) {
                return false;
            }
            
            var match = (index < text.Length) && ((text[index] == pattern[pIndex]) || pattern[pIndex] == '.');
            
            if (pIndex < pattern.Length-1 && pattern[pIndex+1] == '*') {
                cache[index, pIndex] = (match && Helper(index + 1, pIndex))
                    || Helper(index, pIndex+2);
                return cache[index, pIndex].Value;
            }      
            if (match) {
                cache[index, pIndex] = Helper(index+1, pIndex+1);
                return cache[index, pIndex].Value;
            }

            cache[index, pIndex] =  false;
            return cache[index, pIndex].Value;
        }
      
        return Helper(0, 0);
    } 
}

