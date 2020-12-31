use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
    let input = std::fs::read_to_string(r"..\input.txt")?;
    const SLOPE: usize = 3;
    let counter: usize = input
        .lines()
        .enumerate()
        .filter(|(i, row)| row.chars()
                              .nth(i * SLOPE % row.len()) == Some('#'))
        .count();
    println!("{}", counter);
    Ok(())
}
