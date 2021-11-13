package aoc201605;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Main {

    public static void main(String[] args) throws IOException {
        var doorId = Files
                .readString(Path.of("..", "input.txt"))
                .strip();
        Solver solver = new Solver();
        System.out.println(solver.solvePart1(doorId));
        System.out.println(solver.solvePart2(doorId));
    }

}
