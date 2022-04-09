package aoc201706;

import org.apache.commons.lang3.tuple.Pair;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MainTest {

    @Test
    void solve() {
        assertEquals(
                Pair.of(5, 4),
                Main.solve(new int[]{0, 2, 7, 0}));
    }

}