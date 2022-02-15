package aoc2017d03;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;

public class Solver {

    static public int solvePart1(int square) {
        return findLocation(square).calcDistance();
    }

    static public int solvePart2(int square) {
        Map<Location, Integer> priorSums = new HashMap<>();
        priorSums.put(new Location(0, 0), 1);
        int number = 2;
        int currentSum = 1;
        while (currentSum <= square) {
            Location loc = findLocation(number);
            currentSum = loc.getNeighbors().stream()
                    .filter(priorSums::containsKey)
                    .mapToInt(priorSums::get)
                    .sum();
            priorSums.put(loc, currentSum);
            number++;
        }
        return currentSum;
    }

    static Location findLocation(int square) {
        int r = findRectangleFor(square);
        CornerNumbers corners = CornerNumbers.of(r);
        if (square <= corners.northeast()) {
            return new Location(r, square + r - corners.northeast());
        } else if (square <= corners.northwest()) {
            return new Location(corners.northwest() - square - r, r);
        } else if (square <= corners.southwest()) {
            return new Location(-r, corners.southwest() - square - r);
        } else {
            return new Location(square + r - corners.southeast(), -r);
        }
    }

    static int findRectangleFor(int square) {
        return IntStream
                .iterate(0, n -> n + 1)
                .filter(n -> Solver.findStopNumber(n) >= square)
                .findFirst()
                .orElse(0);
    }

    static int findStopNumber(int rectangleNumber) {
        return (int) Math.pow(2 * rectangleNumber + 1, 2);
    }

}
