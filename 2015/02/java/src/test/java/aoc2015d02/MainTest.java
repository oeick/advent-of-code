package aoc2015d02;

import org.junit.jupiter.api.Test;

import java.util.List;

import static aoc2015d02.Main.*;
import static org.junit.jupiter.api.Assertions.assertEquals;

class MainTest {

    @Test
    void calcPaperExample1() {
        assertEquals(58, calcPaper(new Dimension(2, 3, 4)));
    }

    @Test
    void calcPaperExample2() {
        assertEquals(43, calcPaper(new Dimension(1, 1, 10)));
    }

    @Test
    void calcRibbonExample1() {
        assertEquals(34, calcRibbon(new Dimension(2, 3, 4)));
    }

    @Test
    void calcRibbonExample2() {
        assertEquals(14, calcRibbon(new Dimension(1, 1, 10)));
    }

    @Test
    void solvePart1WithExamples1And2() {
        assertEquals(101, solvePart1(List.of(
                new Dimension(2, 3, 4),
                new Dimension(1, 1, 10))));
    }

    @Test
    void solvePart2WithExamples1And2() {
        assertEquals(48, solvePart2(List.of(
                new Dimension(2, 3, 4),
                new Dimension(1, 1, 10))));
    }

}