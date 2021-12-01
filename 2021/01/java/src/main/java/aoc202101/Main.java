package aoc202101;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


public class Main {

    public static void main(String[] args) throws IOException {
        List<Integer> numbers = Files
                .readAllLines(Path.of("../input.txt"))
                .stream()
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        System.out.println(solvePart1(numbers));
        System.out.println(solvePart2(numbers));
    }

    public static long solvePart1(List<Integer> numbers) {
        return IntStream
                .range(1, numbers.size())
                .filter(i -> numbers.get(i) > numbers.get(i - 1))
                .count();
    }

    public static int tripleSum(List<Integer> numbers, int start) {
        return numbers
                .subList(start, start + 3)
                .stream()
                .reduce(0, Integer::sum);
    }

    public static long solvePart2(List<Integer> numbers) {
        return IntStream
                .range(3, numbers.size())
                .filter(i -> tripleSum(numbers, i - 2) > tripleSum(numbers, i - 3))
                .count();
    }

}
