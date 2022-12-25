package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	input := readInput()
	fmt.Println(solvePart1(input))
	fmt.Println(solvePart2(input))
}

func readInput() string {
	input_raw, err := os.ReadFile("../input.txt")
	if err != nil {
		fmt.Print(err)
	}
	return string(input_raw)
}

func solvePart1(input string) int {
	return strings.Count(input, "(") - strings.Count(input, ")")
}

func solvePart2(input string) int {
	floor := 0
	for n, c := range input {
		if string(c) == "(" {
			floor += 1
		} else {
			floor -= 1
			if floor == -1 {
				return n + 1
			}
		}
	}
	return 0
}
