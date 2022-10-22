package aoc;

import org.jetbrains.annotations.NotNull;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {

    static Pattern pattern = Pattern.compile(
            "Step (.) must be finished before step (.) can begin.");

    public static void
    main(String[] args) throws IOException {
        final Map<String, List<String>> input = readInput(
                Path.of("..", "input.txt"));
        final Solver solver = new Solver(input, 5, 60);
        System.out.println(solver.solvePart1());
        System.out.println(solver.solvePart2());
    }

    @NotNull
    static Map<String, List<String>>
    readInput(final @NotNull Path path) throws IOException {
        List<String> lines = Files.readAllLines(path);
        return parseInput(lines);
    }

    @NotNull
    static Map<String, List<String>>
    parseInput(final @NotNull List<String> input) {
        final Map<String, List<String>> map = new HashMap<>();
        for (String line : input) {
            parseLine(line).ifPresent(t -> appendToInstructions(map, t));
        }
        return map;
    }

    @NotNull
    static Optional<Map.Entry<String, String>>
    parseLine(final @NotNull String line) {
        final Matcher matcher = pattern.matcher(line);
        if (matcher.find()) {
            return Optional.of(new AbstractMap.SimpleImmutableEntry<>(
                    matcher.group(2),
                    matcher.group(1)));
        }
        return Optional.empty();
    }

    static void
    appendToInstructions(
            final @NotNull Map<String, List<String>> map,
            final @NotNull Map.Entry<String, String> instruction) {
        if (map.containsKey(instruction.getKey())) {
            map.get(instruction.getKey()).add(instruction.getValue());
        } else {
            map.put(instruction.getKey(),
                    new ArrayList<>(List.of(instruction.getValue())));
        }
    }
}
