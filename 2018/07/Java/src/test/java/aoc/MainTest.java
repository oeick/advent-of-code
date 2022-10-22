package aoc;

import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MainTest {

    @Test
    void parseInput() {
        assertEquals(
                Map.of(
                        "A", List.of("B"),
                        "B", List.of("C", "D")),
                Main.parseInput(List.of(
                        "Step B must be finished before step A can begin.",
                        "Step C must be finished before step B can begin.",
                        "Step D must be finished before step B can begin."))
        );
    }
}