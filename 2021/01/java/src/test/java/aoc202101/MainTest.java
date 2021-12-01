package aoc202101;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MainTest {

    @org.junit.jupiter.api.Test
    void solvePart1() {
        assertEquals(
                7,
                Main.solvePart1(List.of(
                        199,
                        200,
                        208,
                        210,
                        200,
                        207,
                        240,
                        269,
                        260,
                        263
                )));
    }

    @Test
    void solvePart2() {
        assertEquals(
                5,
                Main.solvePart2(List.of(
                        199,
                        200,
                        208,
                        210,
                        200,
                        207,
                        240,
                        269,
                        260,
                        263
                )));
    }
}