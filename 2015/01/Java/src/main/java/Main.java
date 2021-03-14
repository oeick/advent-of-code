import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.NoSuchElementException;


public class Main {

    public static void main(String[] args) throws IOException {
        var instructions = Files
                .readString(Path.of("..", "input.txt"));
        System.out.println(solvePart1(instructions));
        System.out.println(solvePart2(instructions));
    }

    public static int solvePart1(String instructions){
        return instructions
                .chars()
                .reduce(0, (f, p) -> f + (p == '(' ? 1 : -1));
    }

    public static int solvePart2(String instructions){
        int floor = 0;
        for(int i = 0; i <= instructions.length(); i++){
            if(instructions.charAt(i) == '(') floor++;
            else if (--floor < 0) return i + 1;
        }
        throw new NoSuchElementException("never reached basement");
    }
}
