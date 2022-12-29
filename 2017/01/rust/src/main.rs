use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
    let captcha = std::fs::read_to_string(r"..\input.txt")?;
    println!("{}", solve_part_1(&captcha));
    println!("{}", solve_part_2(&captcha));
    Ok(())
}

fn solve_part_1(captcha: &String) -> u32{
    let mut shifted = String::from(&captcha[1..]);
    shifted.push(captcha.chars().nth(0).unwrap());
    captcha
        .chars()
        .into_iter()
        .zip(shifted.chars().into_iter())
        .filter(|(a, b)| a == b)
        .map(|(a, _)| a.to_digit(10).unwrap())
        .sum()
}

fn solve_part_2(captcha: &String) -> u32{
    let middle = captcha.chars().count() / 2;
    let half_1 = &captcha[..middle];
    let half_2 = &captcha[middle..];
    2 * half_1
        .chars()
        .into_iter()
        .zip(half_2.chars().into_iter())
        .filter(|(a, b)| a == b)
        .map(|(a, _)| a.to_digit(10).unwrap())
        .sum::<u32>()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_part1() {
        let examples = [
            ("1122", 3),
            ("1111", 4),
            ("1234", 0),
            ("91212129", 9)];
        for (example, expected) in examples.iter() {
            assert_eq!(
                expected,
                &solve_part_1(&example.to_string()));
        }
    }

    #[test]
    fn test_example_part2() {
        let examples = [
            ("1212", 6),
            ("1221", 0),
            ("123425", 4),
            ("123123", 12),
            ("12131415", 4)];
        for (example, expected) in examples.iter() {
            assert_eq!(
                expected,
                &solve_part_2(&example.to_string()));
        }
    }
}