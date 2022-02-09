package aoc2016d01;

public record Position(
        int x,
        int y) {
    public int distance(){
        return Math.abs(x) + Math.abs(y);
    }
}
