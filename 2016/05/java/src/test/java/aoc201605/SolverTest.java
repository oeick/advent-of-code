package aoc201605;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

class SolverTest {

    Solver solver;

    @BeforeEach
    void setUp() {
        solver = new Solver();
    }

    @Test
    void testSolvePart1() {
        assertEquals("18f47a30", solver.solvePart1("abc"));
    }

    @Test
    void testSolvePart2() {
        assertEquals("05ace8e3", solver.solvePart2("abc"));
    }

    @Test
    void testStartsWithFiveZeros_YES() {
        assertTrue(solver.startsWithFiveZeros(new byte[]{0, 0, 0}));
        assertTrue(solver.startsWithFiveZeros(new byte[]{0, 0, 0x0f}));
    }

    @Test
    void testStartsWithFiveZeros_NO() {
        assertFalse(solver.startsWithFiveZeros(new byte[]{0, 0, 0x10}));
        assertFalse(solver.startsWithFiveZeros(new byte[]{0, 1, 0}));
        assertFalse(solver.startsWithFiveZeros(new byte[]{1, 0, 0}));
    }

    @Test
    void testBuildStringPwMap() {
        assertEquals("abcdefgh", solver.buildStringFromPw(Map.of(
                0, 'a',
                1, 'b',
                2, 'c',
                3, 'd',
                4, 'e',
                5, 'f',
                6, 'g',
                7, 'h'
        )));
    }

    @Test
    void testPlaceCharToMap_NEW_POSITION() {
        Map<Integer, Character> map = new HashMap<>(Map.of(
                0, 'a',
                1, 'b'
        ));
        solver.placeCharToMap(map, 'c', 2);
        assertEquals(Map.of(
                        0, 'a',
                        1, 'b',
                        2, 'c'),
                map);
    }

    @Test
    void testPlaceCharToMap_EXISTING_POSITION() {
        Map<Integer, Character> map = new HashMap<>(Map.of(
                0, 'a',
                1, 'b'
        ));
        solver.placeCharToMap(map, 'z', 0);
        assertEquals(Map.of(
                        0, 'a',
                        1, 'b'),
                map);
    }
}