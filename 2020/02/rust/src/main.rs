use std::fs::File;
use std::io::{BufRead, BufReader};
use regex::Regex;

fn main() {
    let input_file = File::open(r"..\input.txt").unwrap();
    let lines: Vec<String> = BufReader::new(input_file)
        .lines()
        .map(|l| l.unwrap())
        .collect();

    let pattern = Regex::new(r"(\d+)-(\d+) (\w+): (.+)").unwrap();

    let (mut counter1, mut counter2) = (0, 0);
    for line in lines{
        let matches = pattern.captures(&line).unwrap();
        let low: usize = matches[1].parse().unwrap();
        let high: usize = matches[2].parse().unwrap();
        let character = matches[3].chars().next().unwrap();
        let code = &matches[4];
        let character_count = code.chars().filter(|&c| c == character).count();
        if (low..=high).contains(&character_count) {
            counter1 += 1;
        };
        if (code.chars().nth(low - 1).unwrap() == character) != 
           (code.chars().nth(high - 1).unwrap() == character) {
            counter2 += 1;
        }
    }
    println!("{}", counter1);
    println!("{}", counter2);
}
