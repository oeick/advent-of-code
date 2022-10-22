package aoc;

import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverTest {

    @Test
    void solvePart1() {
        assertEquals(
                "CABDFE",
                new Solver(Map.of(
                        "A", List.of("C"),
                        "F", List.of("C"),
                        "B", List.of("A"),
                        "D", List.of("A"),
                        "E", List.of("B", "D", "F")),
                        2,
                        0).solvePart1());
    }

    @Test
    void getAllSteps() {
        assertEquals(
                Set.of("A", "B", "C", "D"),
                Solver.getAllSteps(Map.of(
                        "A", List.of("B"),
                        "B", List.of("C", "D"))));
    }

    @Test
    void getFreeSteps() {
        assertEquals(
                List.of("A", "D"),
                Solver.getFreeSteps(
                        Set.of("A", "B", "C", "D"),
                        Map.of("B", List.of("X")),
                        List.of("C")));
    }

    @Test
    void getOrderlyInstructions_Simple() {
        assertEquals(
                List.of("B", "A"),
                Solver.getOrderlyInstructions(Map.of("A", List.of("B"))));
    }

    @Test
    void getOrderlyInstructions_Part1Example() {
        assertEquals(
                List.of("C", "A", "B", "D", "F", "E"),
                Solver.getOrderlyInstructions(Map.of(
                        "A", List.of("C"),
                        "F", List.of("C"),
                        "B", List.of("A"),
                        "D", List.of("A"),
                        "E", List.of("B", "D", "F"))));
    }

    @Test
    void getParallelizedWorkResult() {
        Solver solver = new Solver(
                Map.of(
                        "A", List.of("C"),
                        "F", List.of("C"),
                        "B", List.of("A"),
                        "D", List.of("A"),
                        "E", List.of("B", "D", "F")),
                2,
                0);
        assertEquals(
                new CompletedWork("CABFDE", 15),
                solver.getParallelizedWorkResult());
    }

}