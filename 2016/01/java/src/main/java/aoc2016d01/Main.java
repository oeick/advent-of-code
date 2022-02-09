package aoc2016d01;

import org.eclipse.collections.impl.list.mutable.FastList;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

import static aoc2016d01.Direction.NORTH;

public class Main {
    public static void main(String[] args) throws IOException {
        final var input = Arrays.stream(
                        Files.readString(Path.of("..", "input.txt"))
                                .split(", "))
                .map(s -> new Instruction(
                        Turn.valueOf(s.substring(0, 1)),
                        Integer.parseInt(s.substring(1))))
                .toList();
        System.out.println(solvePart1(input));
        System.out.println(solvePart2(input));
    }

    public static int solvePart1(final List<Instruction> instructions) {
        return buildPath(instructions)
                .getLast()
                .distance();
    }

    public static int solvePart2(final List<Instruction> instructions) {
        final var path = buildPath(instructions);
        return path
                .detect(p -> path.count(p::equals) == 2)
                .distance();
    }

    private static FastList<Position> buildPath(final List<Instruction> instructions) {
        Direction face = NORTH;
        var path = new FastList<>(List.of(new Position(0, 0)));
        for (Instruction instruction : instructions) {
            face = face.rotate(instruction.turn());
            int x = path.getLast().x();
            int y = path.getLast().y();
            path.addAll(switch (face) {
                case NORTH -> IntStream.rangeClosed(1, instruction.distance())
                        .mapToObj(d -> new Position(x, y + d)).toList();
                case EAST -> IntStream.rangeClosed(1, instruction.distance())
                        .mapToObj(d -> new Position(x + d, y)).toList();
                case SOUTH -> IntStream.rangeClosed(1, instruction.distance())
                        .mapToObj(d -> new Position(x, y - d)).toList();
                case WEST -> IntStream.rangeClosed(1, instruction.distance())
                        .mapToObj(d -> new Position(x - d, y)).toList();
            });
        }
        return path;
    }
}
