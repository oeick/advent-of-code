package aoc2015d02;

import java.util.List;
import java.util.stream.Stream;

public record Dimension(
        int x,
        int y,
        int z
) {
    public Stream<Integer> areas() {
        return Stream.of(x * y, x * z, y * z);
    }

    public Stream<Integer> perimeters() {
        return Stream.of(x + y, x + z, y + z);
    }

    public static Dimension of(List<Integer> ints) {
        return new Dimension(ints.get(0), ints.get(1), ints.get(2));
    }
}
