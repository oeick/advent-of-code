import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.regex.Pattern;

import io.vavr.collection.Stream;

public class Main {

    public static void main(String[] args) throws IOException {
        var lines = Stream.ofAll(
                Files.lines(Path.of("..", "input.txt")));
        var pattern = Pattern.compile("(\\d+)-(\\d+) (\\w+): (.+)");

        int counter1 = 0;
        int counter2 = 0;
        for (String line : lines) {
            var matcher = pattern.matcher(line);
            matcher.matches();
            var low = Integer.parseInt(matcher.group(1));
            var high = Integer.parseInt(matcher.group(2));
            var character = matcher.group(3).charAt(0);
            var code = matcher.group(4);
            var characterCount = code
                    .chars()
                    .filter(c -> c == character)
                    .count();
            if (characterCount <= high && characterCount >= low)
                counter1 += 1;
            if ((code.charAt(low - 1) == character) !=
                    (code.charAt(high - 1) == character))
                counter2 += 1;
        }

        System.out.println(counter1);
        System.out.println(counter2);
    }
}