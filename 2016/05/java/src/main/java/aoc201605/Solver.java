package aoc201605;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solver {

    public MessageDigest hashCoder;

    public Solver() {
        hashCoder = getHashCoder("MD5");
    }

    public String solvePart1(String doorId) {
        StringBuilder pwBuilder = new StringBuilder();
        for (int i = 0; pwBuilder.length() < 8; i++) {
            byte[] bytes = hashCoder.digest((doorId + i).getBytes());
            if (startsWithFiveZeros(bytes)) {
                pwBuilder.append(String.format("%x", bytes[2] & 0x0F));
            }
        }
        return pwBuilder.toString();
    }

    public String solvePart2(String doorId) {
        Map<Integer, Character> pwMap = new HashMap<>();
        for (int i = 0; pwMap.size() < 8; i++) {
            byte[] bytes = hashCoder.digest((doorId + i).getBytes());
            if (startsWithFiveZeros(bytes)) {
                placeCharToMap(
                        pwMap,
                        String.format("%02x", bytes[3]).charAt(0),
                        bytes[2] & 0x0F);
            }
        }
        return buildStringFromPw(pwMap);
    }

    public boolean startsWithFiveZeros(byte[] bytes) {
        return bytes[0] == 0 && bytes[1] == 0 && (bytes[2] & 0xF0) == 0;
    }

    public void placeCharToMap(Map<Integer, Character> map, char character, int position) {
        if (position < 8 && !map.containsKey(position)) {
            map.put(position, character);
        }
    }

    public String buildStringFromPw(Map<Integer, Character> pw) {
        return IntStream
                .range(0, pw.size())
                .mapToObj(i -> pw.get(i).toString())
                .collect(Collectors.joining());
    }

    public MessageDigest getHashCoder(String type) {
        MessageDigest messageDigest;
        try {
            messageDigest = MessageDigest.getInstance(type);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Hash algorithm not found: " + type, e);
        }
        return messageDigest;
    }
}
