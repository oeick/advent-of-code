package aoc2016d01;

import org.apache.commons.lang3.tuple.Pair;

import java.util.Map;

public enum Direction {
    NORTH,
    EAST,
    SOUTH,
    WEST;

    public Direction rotate(Turn turn) {
        final Pair<Direction, Direction> turns = Map.of(
                NORTH, Pair.of(WEST, EAST),
                EAST, Pair.of(NORTH, SOUTH),
                SOUTH, Pair.of(EAST, WEST),
                WEST, Pair.of(SOUTH, NORTH)).get(this);
        return switch (turn) {
            case L -> turns.getLeft();
            case R -> turns.getRight();
        };
    }
}