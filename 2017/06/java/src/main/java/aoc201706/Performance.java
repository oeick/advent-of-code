package aoc201706;

import java.io.IOException;
import java.nio.file.Path;
import java.time.Duration;
import java.time.Instant;

public class Performance {

    public static void main(String[] args) throws IOException {
        int[] banks = Main.parseInput(Path.of("..", "input.txt"));
        Instant t0 = Instant.now();
        Main.solve(banks);
        Instant t1 = Instant.now();
        System.out.printf("%d ms\n", Duration.between(t0, t1).toMillis());
    }
}
