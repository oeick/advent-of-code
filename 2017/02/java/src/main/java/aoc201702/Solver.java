package aoc201702;

import java.util.List;
import java.util.stream.Collectors;

public class Solver {

    public static int solvePart1(List<List<Integer>> spreadsheet) {
        return spreadsheet.stream()
                .mapToInt(Solver::minMaxDiff)
                .sum();
    }

    public static int solvePart2(List<List<Integer>> spreadsheet) {
        return spreadsheet.stream()
                .mapToInt(Solver::evenlyDiv)
                .sum();
    }

    private static int minMaxDiff(List<Integer> row) {
        var stats = row.stream()
                .collect(Collectors.summarizingInt(i -> i));
        return stats.getMax() - stats.getMin();
    }

    private static int evenlyDiv(List<Integer> row) {
        for (var x : row)
            for (var y : row)
                if (x > y && x % y == 0) return x / y;
        return 0;
    }
}
