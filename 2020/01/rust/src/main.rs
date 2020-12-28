use itertools::Itertools;

fn main() {
    let input_file_content = std::fs::read_to_string(r"..\input.txt").unwrap();
    let numbers: Vec<u32> = input_file_content
        .lines()
        .map(|l| l.parse::<u32>().unwrap())
        .collect();

    let solution1 = solve(&numbers, 2);
    println!("{}", solution1);

    let solution2 = solve(&numbers, 3);
    println!("{}", solution2);
}

fn solve(numbers: &Vec<u32>, num_of_entries: usize) -> u32{
    numbers
        .iter()
        .combinations(num_of_entries)
        .find(|c| c.iter().map(|x| *x).sum::<u32>() == 2020)
        .unwrap()
        .iter()
        .fold(1, |a, b| a * *b)
}