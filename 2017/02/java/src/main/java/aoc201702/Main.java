package aoc201702;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        var input = Files
                .readAllLines(Path.of("..", "input.txt")).stream()
                .map(line -> Arrays.stream(line
                        .split("\\t"))
                        .map(Integer::parseInt)
                        .toList())
                .toList();
        System.out.println(Solver.solvePart1(input));
        System.out.println(Solver.solvePart2(input));
    }
}
