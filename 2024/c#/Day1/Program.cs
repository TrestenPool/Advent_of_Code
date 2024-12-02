using System.Numerics;

namespace Day1;
class Program{
  static void Main(string[] args){
    string filePath = @"C:\Users\trestenp\OneDrive - City of Corpus Christi\Documents\Github\Advent_of_Code\2024\c#\Day1\input.txt";
    var lines = ReadFile(filePath);

    // Day1Answer(lines);
    Day2Answer(lines);
  }

  static string[] ReadFile(string filePath) {
    string[] content = System.IO.File.ReadAllLines(filePath);
    return content;
  }

  static void Day1Answer(string[] lines) {
    var list1 = new List<int>();
    var list2 = new List<int>();

    foreach(var line in lines) {
      // split the array
      var segments = line.Split(" ");
      // remove the empty elements
      segments = segments.Where(s => !string.IsNullOrEmpty(s)).ToArray();

      // add to the list
      list1.Add(Convert.ToInt32( segments[0] ));
      list2.Add(Convert.ToInt32( segments[1] ));
    }

    // sort the list
    list1.Sort();
    list2.Sort();

    var total = 0;
    for(var i=0; i < list1.Count; i++) {
      var num1 = list1[i];
      var num2 = list2[i];
      total += Math.Abs(num1 - num2);
    }

    Console.WriteLine(total);
  }

  static void Day2Answer(string[] lines) {
    var list1 = new List<int>();
    var list2 = new List<int>();

    // parse into the lists
    foreach(var line in lines) {
      var segments = line.Split(" ");
      segments = segments.Where(s => !string.IsNullOrEmpty(s)).ToArray();

      list1.Add(Convert.ToInt32( segments[0] ));
      list2.Add(Convert.ToInt32( segments[1] ));
    }

    list1.Sort();
    list2.Sort();

    
    // key/value => num/count
    var dict = new Dictionary<int,int>();

    var total = 0;

    foreach(var num in list1) {
      // already computed total, just add again
      if(dict.ContainsKey(num)) {
        total += ( dict[num] * num );
      }
      else {
        int count = list2.Count(n => n==num);
        total += (count * num);
        dict.Add(num, count);
      }
    }

    Console.WriteLine(total);
  }

}
