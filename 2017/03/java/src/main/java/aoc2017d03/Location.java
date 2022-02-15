package aoc2017d03;

import java.util.List;

public record Location(
        int x,
        int y) {

    int calcDistance() {
        return Math.abs(x) + Math.abs(y);
    }

    List<Location> getNeighbors() {
        return List.of(
                new Location(x - 1, y - 1),
                new Location(x, y - 1),
                new Location(x + 1, y - 1),
                new Location(x - 1, y),
                new Location(x + 1, y),
                new Location(x - 1, y + 1),
                new Location(x, y + 1),
                new Location(x + 1, y + 1)
        );
    }
}
