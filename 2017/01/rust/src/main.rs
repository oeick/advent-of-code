use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
    let input = std::fs::read_to_string(r"..\input.txt")?;
    let mut shifted = String::from(&input[1..]);
    shifted.push(input.chars().last().unwrap());
    let zipped: u32 = input
        .chars()
        .into_iter()
        .zip(shifted.chars().into_iter())
        .filter(|(a, b)| a == b)
        .map(|(a, _)| a.to_digit(10).unwrap())
        .sum();
    println!("{}", zipped);
    Ok(())
}
