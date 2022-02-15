package aoc2017d03;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;

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

    @ParameterizedTest
    @CsvSource({
            "  2,   1",
            "  4,   2",
            "  4,   3",
            "  5,   4",
            " 10,   5",
            "806, 800"})
    void solvePart2(int expected, int square) {
        assertEquals(expected, Solver.solvePart2(square));
    }
}