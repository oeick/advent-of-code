package aoc2016d01;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MainTest {

    @Test
    void solvePart1Examples() {
        assertEquals(5, Main.solvePart1(List.of(
                new Instruction(Turn.R, 2),
                new Instruction(Turn.L, 3))));
        assertEquals(2, Main.solvePart1(List.of(
                new Instruction(Turn.R, 2),
                new Instruction(Turn.R, 2),
                new Instruction(Turn.R, 2))));
        assertEquals(12, Main.solvePart1(List.of(
                new Instruction(Turn.R, 5),
                new Instruction(Turn.L, 5),
                new Instruction(Turn.R, 5),
                new Instruction(Turn.R, 3))));
    }

    @Test
    void solvePart2() {
        assertEquals(4, Main.solvePart2(List.of(
                new Instruction(Turn.R, 8),
                new Instruction(Turn.R, 4),
                new Instruction(Turn.R, 4),
                new Instruction(Turn.R, 8))));
    }
}