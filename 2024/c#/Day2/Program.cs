using System.Globalization;
using System.Net.Mime;

namespace Day2;

class Program{

  static void Main(string[] args){
    var filepath = @"C:\Users\trestenp\OneDrive - City of Corpus Christi\Documents\Github\Advent_of_Code\2024\c#\Day2\input.txt";
    var lines = System.IO.File.ReadAllLines(filepath);

    Part1Solution(lines);
    // Part2Solution(contents);
  }

  static void Part1Solution(string[] lines) {

    var total = 0;
    
    // go through each of the lines
    foreach(var line in lines) {

      // get the numbers from the array
      string[] numbers_str_array = line.Split(" ");
      int[] numbers = numbers_str_array.Select(int.Parse).ToArray();

      // used to determine if the numbers are increasing or decreasing
      bool? isIncreasing = null;

      for(int i = 1; i < numbers.Length; i++) {
        
        // increasing
        if(numbers[i] > numbers[i-1]) {
          if(isIncreasing.HasValue && isIncreasing == false) {
            // unsafe
          }
          else {
            isIncreasing = true;
          }
        }
        else {

        }

      }

    }

  }

  static void Part2Solution(string[] content) {
  }

}
