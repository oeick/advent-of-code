package aoc;

import org.jetbrains.annotations.NotNull;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


public class Solver {

    @NotNull Map<String, List<String>> instructions;
    final int numberOfWorkers;
    final int baseDuration;


    public Solver(
            final @NotNull Map<String, List<String>> instructions,
            final int numberOfWorkers,
            final int baseDuration) {
        this.instructions = instructions;
        this.numberOfWorkers = numberOfWorkers;
        this.baseDuration = baseDuration;
    }

    @NotNull
    String solvePart1() {
        return String.join("", getOrderlyInstructions(this.instructions));
    }

    @NotNull
    String solvePart2() {
        final CompletedWork completedWork = getParallelizedWorkResult();
        return String.valueOf(completedWork.duration());
    }


    @NotNull
    static List<String> getOrderlyInstructions(
            final @NotNull Map<String, List<String>> instructions) {
        return arrangeStepsFromInstructions(instructions, getAllSteps(instructions));
    }

    @NotNull
    static List<String> arrangeStepsFromInstructions(
            final @NotNull Map<String, List<String>> instructions,
            final @NotNull Set<String> allSteps) {
        Map<String, List<String>> disordered =
                new HashMap<>(instructions);
        List<String> orderly = new ArrayList<>();
        List<String> freeSteps = getFreeSteps(
                allSteps, disordered, orderly);
        while (!disordered.isEmpty() || !freeSteps.isEmpty()) {
            if (!freeSteps.isEmpty()) {
                orderly.add(freeSteps.remove(0));
            }
            reduceDisorderedInstructions(disordered, orderly);
            freeSteps = getFreeSteps(allSteps, disordered, orderly);
        }
        return orderly;
    }

    @NotNull
    static Set<String> getAllSteps(
            final @NotNull Map<String, List<String>> instructions) {
        Set<String> result = new HashSet<>(instructions.keySet());
        for (List<String> preSteps : instructions.values()) {
            result.addAll(preSteps);
        }
        return result;
    }

    @NotNull
    static List<String> getFreeSteps(
            final @NotNull Set<String> allSteps,
            final @NotNull Map<String, List<String>> instructions,
            final @NotNull List<String> orderlyInstructions) {
        return allSteps.stream()
                .filter(s -> !instructions.containsKey(s))
                .filter(s -> !orderlyInstructions.contains(s))
                .distinct()
                .sorted()
                .collect(Collectors.toList());
    }

    static void reduceDisorderedInstructions(
            final @NotNull Map<String, List<String>> disordered,
            final @NotNull List<String> orderly) {
        for (String mainStep : disordered.keySet().stream().toList()) {
            List<String> reduced = disordered.get(mainStep)
                    .stream()
                    .filter(p -> !orderly.contains(p))
                    .toList();
            if (reduced.isEmpty()) {
                disordered.remove(mainStep);
            } else {
                disordered.put(mainStep, reduced);
            }
        }
    }

    @NotNull
    CompletedWork getParallelizedWorkResult() {
        Set<String> todo = getAllSteps(this.instructions);
        List<String> done = new ArrayList<>();
        int t = 0;
        Map<Integer, Optional<Job>> workers =
                prepareWorkers(this.numberOfWorkers);
        while (isStillWorkToDo(todo, workers)) {
            done.addAll(letWorkersWork(workers));
            distributeRemainingWork(todo, done, workers);
            t++;
        }
        return new CompletedWork(String.join("", done), t - 1);
    }

    void distributeRemainingWork(
            final @NotNull Set<String> todo,
            final @NotNull List<String> done,
            final @NotNull Map<Integer, Optional<Job>> workers) {
        for (int freeWorker : findFreeWorkers(workers)) {
            final List<String> nextSteps = todo.stream()
                    .filter(s -> !this.instructions.containsKey(s)
                            || done.containsAll(this.instructions.get(s)))
                    .sorted()
                    .toList();
            if (!nextSteps.isEmpty()) {
                String nextStep = nextSteps.get(0);
                workers.put(
                        freeWorker,
                        Optional.of(new Job(
                                nextStep,
                                calcDuration(nextStep, this.baseDuration))));
                todo.remove(nextStep);
            }
        }
    }

    static List<Integer>
    findFreeWorkers(final @NotNull Map<Integer, Optional<Job>> workers) {
        return workers.entrySet().stream()
                .filter(es -> es.getValue().isEmpty())
                .map(Map.Entry::getKey)
                .toList();
    }

    @NotNull
    static List<String>
    letWorkersWork(
            final @NotNull Map<Integer, Optional<Job>> workers) {
        List<String> done = new ArrayList<>();
        for (int worker : workers.keySet()) {
            if (workers.get(worker).isPresent()) {
                Job job = workers.get(worker).get();
                job.time -= 1;
                if (job.time == 0) {
                    done.add(job.step);
                    workers.put(worker, Optional.empty());
                }
            }
        }
        return done;
    }

    static boolean isStillWorkToDo(
            final @NotNull Set<String> todo,
            final @NotNull Map<Integer, Optional<Job>> workers) {
        return !todo.isEmpty() || isThereAtLeastOneUnfinishedWorker(workers);
    }

    static boolean isThereAtLeastOneUnfinishedWorker(
            Map<Integer, Optional<Job>> workers) {
        return workers.entrySet().stream()
                .anyMatch(es -> es.getValue().isPresent());
    }

    @NotNull
    static Map<Integer, Optional<Job>>
    prepareWorkers(final int numberOfWorkers) {
        return IntStream
                .range(0, numberOfWorkers)
                .boxed()
                .collect(Collectors.toMap(
                        key -> key,
                        value -> Optional.empty()));
    }

    static int calcDuration(final @NotNull String step, final int base) {
        return step.charAt(0) - 64 + base;
    }

}
