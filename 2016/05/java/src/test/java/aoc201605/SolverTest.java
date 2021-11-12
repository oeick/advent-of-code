package aoc201605;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverTest {

    Solver solver;

    @BeforeEach
    void setUp() {
        solver = new Solver();
    }

    @Test
    void solvePart1() {
        assertEquals("18f47a30", solver.solvePart1("abc"));
    }
}