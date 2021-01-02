use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
    let input = std::fs::read_to_string(r"..\input.txt")?;
    println!("{}", solve(&input, vec!((3, 1))));
    println!("{}", solve(&input, vec!((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))));
    Ok(())
}

fn solve(input: &String, slopes: Vec<(usize, usize)>) -> usize{
    slopes.iter()
          .map(|&(right, down)| count_trees(&input, right, down))
          .fold(1, |p, x| p * x)
}

fn count_trees(input: &String, right: usize, down: usize) -> usize{
    input.lines()
         .step_by(down)
         .enumerate()
         .filter(|(i, row)| row.chars()
                               .nth(i * right % row.len()) == Some('#'))
         .count()
}
