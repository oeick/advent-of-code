import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

import io.vavr.collection.Seq;
import io.vavr.collection.Stream;

public class Main {

    public static void main(String[] args) throws IOException {
        var numbers = Stream.ofAll(
                Files.lines(Path.of("..", "input.txt")))
                .map(Integer::parseInt);

        System.out.println(solve(numbers, 2));
        System.out.println(solve(numbers, 3));
    }

    public static int solve(Seq<Integer> numbers, int numOfEntries) {
        return numbers
                .combinations(numOfEntries)
                .find(arr -> arr.sum().intValue() == 2020)
                .get()
                .reduce((a, b) -> a * b);
    }
}