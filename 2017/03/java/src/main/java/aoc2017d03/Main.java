package aoc2017d03;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Main {

    public static void main(String[] args) throws IOException {
        int square = Integer.parseInt(
                Files.readString(Path.of("..", "input.txt")));
        System.out.println(Solver.solvePart1(square));
        System.out.println(Solver.solvePart2(square));
    }
}
