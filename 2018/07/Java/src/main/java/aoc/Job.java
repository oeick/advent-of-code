package aoc;

import org.jetbrains.annotations.NotNull;

public class Job {
    String step;
    int time;

    public Job(
            final @NotNull String step,
            final int time) {
        this.step = step;
        this.time = time;
    }
}
