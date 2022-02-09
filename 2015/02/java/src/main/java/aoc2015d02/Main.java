package aoc2015d02;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        var input = Files.readAllLines(Path.of("..\\input.txt"))
                .stream()
                .map(l -> Arrays.stream(l.split("x"))
                        .map(Integer::parseInt)
                        .toList())
                .map(Dimension::of)
                .toList();
        System.out.println(solvePart1(input));
        System.out.println(solvePart2(input));
    }

    public static int solvePart1(List<Dimension> dimensions) {
        return dimensions.stream()
                .mapToInt(Main::calcPaper)
                .sum();
    }

    public static int solvePart2(List<Dimension> dimensions) {
        return dimensions.stream()
                .mapToInt(Main::calcRibbon)
                .sum();
    }

    static int calcPaper(Dimension dimension) {
        var smallest = dimension
                .areas()
                .min(Integer::compareTo)
                .orElse(0);
        return 2 * dimension.areas().reduce(0, Integer::sum) + smallest;
    }

    static int calcRibbon(Dimension dimension) {
        var smallest = dimension
                .perimeters()
                .min(Integer::compareTo)
                .orElse(0);
        return 2 * smallest + dimension.x() * dimension.y() * dimension.z();
    }
}
