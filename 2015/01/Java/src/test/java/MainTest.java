import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.*;

class MainTest {

    @ParameterizedTest
    @CsvSource({
            "(()),     0",
            "()(),     0",
            "(((,      3",
            "(()(()(,  3",
            "))(((((,  3",
            "()),     -1",
            "))(,     -1",
            "))),     -3",
            ")())()), -3"
    })
    void solvePart1(String example, int floor) {
        assertEquals(floor, Main.solvePart1(example));
    }

    @org.junit.jupiter.api.Test
    void solvePart2() {
        assertEquals(1, Main.solvePart2(")"));
        assertEquals(5, Main.solvePart2("()())"));
        assertEquals(5, Main.solvePart2("()()))"));
        assertEquals(5, Main.solvePart2("()())(("));
    }
}