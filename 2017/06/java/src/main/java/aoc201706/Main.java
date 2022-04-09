package aoc201706;

import com.google.common.primitives.Ints;
import org.apache.commons.lang3.tuple.Pair;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        int[] banks = parseInput(Path.of("..", "input.txt"));
        Pair<Integer, Integer> solutions = solve(banks);
        System.out.println(solutions.getLeft());
        System.out.println(solutions.getRight());
    }

    static int[] parseInput(Path path) throws IOException {
        String input = Files.readString(path);
        return Arrays.stream(input.split("\t"))
                .mapToInt(Integer::parseInt)
                .toArray();
    }

    static Pair<Integer, Integer> solve(int[] banks) {
        List<int[]> configs = new ArrayList<>();
        configs.add(banks);
        int[] new_banks = redistributeBlocks(banks);
        while (!contains(configs, new_banks)) {
            configs.add(new_banks);
            new_banks = redistributeBlocks(new_banks);
        }
        int loopStart = indexOf(configs, new_banks);
        return Pair.of(configs.size(), configs.size() - loopStart);
    }

    static int[] redistributeBlocks(int[] banks) {
        int blocksToRedistribute = Ints.max(banks);
        int targetBank = Ints.indexOf(banks, blocksToRedistribute);
        int[] result = banks.clone();
        result[targetBank] = 0;
        for (int i = 0; i < blocksToRedistribute; i++) {
            targetBank = (targetBank + 1) % result.length;
            result[targetBank] += 1;
        }
        return result;
    }

    static boolean contains(List<int[]> list, int[] array) {
        return list.stream().anyMatch(a -> Arrays.equals(a, array));
    }

    static int indexOf(List<int[]> list, int[] array) {
        return list.stream()
                .filter(a -> Arrays.equals(a, array))
                .findFirst()
                .map(list::indexOf)
                .orElse(-1);
    }

}
