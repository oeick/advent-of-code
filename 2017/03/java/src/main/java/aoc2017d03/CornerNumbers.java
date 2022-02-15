package aoc2017d03;

import java.util.stream.IntStream;

public record CornerNumbers (
    int southeast,
    int southwest,
    int northwest,
    int northeast) {

    public static CornerNumbers of(int r) {
        var corners = IntStream
                .range(0, 4)
                .boxed()
                .mapToInt(n -> Solver.findStopNumber(r) - 2 * n * r)
                .toArray();
        return new CornerNumbers(corners[0], corners[1], corners[2], corners[3]);
    }
}
