package aoc;

import org.jetbrains.annotations.NotNull;

public record CompletedWork(
    @NotNull String resultingSteps,
    int duration){
}
