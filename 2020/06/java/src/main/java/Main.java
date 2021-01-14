import io.vavr.collection.HashSet;
import io.vavr.collection.List;
import io.vavr.collection.Stream;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

import static org.apache.commons.lang3.StringUtils.isNotEmpty;

public class Main {

    public static void main(String[] args) throws IOException {
        var lines = Stream.ofAll(
                Files.lines(Path.of("..", "input.txt")));

        int count1 = 0;
        int count2 = 0;
        List<String> group = List.empty();
        lines.forEach(line -> {
            if(isNotEmpty(line)){
                group.append(line);
            }
            else{
                counter1 += HashSet.of(group.mkString().chars()).size();
                counter2 += group.map(groupLine -> HashSet.of(group.mkString().chars()))
                                 .reduce(HashSet::intersect)
                                 .size();
                group.removeAll();
            }
        });

        System.out.println(count1);
        System.out.println(count2);
    }
}
