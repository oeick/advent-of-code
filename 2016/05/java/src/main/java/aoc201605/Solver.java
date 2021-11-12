package aoc201605;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Solver {

    public MessageDigest hashCoder;

    public Solver() {
        hashCoder = getHashCoder("MD5");
    }

    public String solvePart1(String doorId) {
        StringBuilder pwBuilder = new StringBuilder();
        for (int i = 0; pwBuilder.length() < 8; i++) {
            byte[] bytes = hashCoder.digest((doorId + i).getBytes());
            if (bytes[0] == 0 && bytes[1] == 0 && (bytes[2] & 0xF0) == 0) {
                pwBuilder.append(String.format("%x", bytes[2] & 0x0F));
            }
        }
        return pwBuilder.toString();
    }

    public static MessageDigest getHashCoder(String type) {
        MessageDigest messageDigest;
        try {
            messageDigest = MessageDigest.getInstance(type);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Hash algorithm not found: " + type, e);
        }
        return messageDigest;
    }
}
