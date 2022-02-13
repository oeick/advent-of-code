package aoc201702;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class SolverTest {

    @Test
    void solvePart1Example1() {
        assertEquals(
                18,
                Solver.solvePart1(List.of(
                        List.of(5, 1, 9, 5),
                        List.of(7, 5, 3),
                        List.of(2, 4, 6, 8))));
    }

    @Test
    void solvePart2Example2() {
        assertEquals(
                9,
                Solver.solvePart2(List.of(
                        List.of(5, 9, 2, 8),
                        List.of(9, 4, 7, 3),
                        List.of(3, 8, 6, 5))));
    }

}