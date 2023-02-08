package J1;
import java.io.*;
import java.util.Scanner;

public class Puzzle1 {

    public static void main (String[] args) throws FileNotFoundException {

      File file = new File("/Users/barna/Desktop/AdventOfCode/input1");
      Scanner scannedFile = new Scanner(file);
      
      while (scannedFile.hasNextLine()) {
        System.out.println(scannedFile.nextLine());
        if (scannedFile.nextLine() == ""){
          System.out.println("New Elf :");
        }
      }
      scannedFile.close();
    }
}