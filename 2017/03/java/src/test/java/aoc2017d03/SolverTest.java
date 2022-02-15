package aoc2017d03;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolverTest {

    @Test
    void findStopNumber() {
        assertEquals(1, Solver.findStopNumber(0));
        assertEquals(9, Solver.findStopNumber(1));
        assertEquals(25, Solver.findStopNumber(2));
    }

    @Test
    void findRectangleFor() {
        assertEquals(0, Solver.findRectangleFor(1));
        assertEquals(1, Solver.findRectangleFor(2));
        assertEquals(1, Solver.findRectangleFor(9));
        assertEquals(2, Solver.findRectangleFor(10));
    }

    @Test
    void cornerNumbers() {
        assertEquals(
                new CornerNumbers(1, 1, 1, 1),
                CornerNumbers.of(0));
        assertEquals(
                new CornerNumbers(9, 7, 5, 3),
                CornerNumbers.of(1));
        assertEquals(
                new CornerNumbers(25, 21, 17, 13),
                CornerNumbers.of(2));
    }

    @Test
    void solvePart1() {
        assertEquals(0, Solver.solvePart1(1));
        assertEquals(3, Solver.solvePart1(12));
        assertEquals(2, Solver.solvePart1(23));
        assertEquals(31, Solver.solvePart1(1024));
    }

    @Test
    void solvePart2() {
        assertEquals(2, Solver.solvePart2(1));
        assertEquals(4, Solver.solvePart2(2));
        assertEquals(4, Solver.solvePart2(3));
        assertEquals(5, Solver.solvePart2(4));
        assertEquals(10, Solver.solvePart2(5));
        assertEquals(806, Solver.solvePart2(800));
    }
}