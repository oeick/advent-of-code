use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
    let input = std::fs::read_to_string(r"..\input.txt")?;

    let floor = solve_part_1(&input);
    println!("{}", floor);

    let basement_index = solve_part_2(&input);
    println!("{}", basement_index);

    Ok(())
}

fn solve_part_1(input: &String) -> i32{
    input.chars()
         .fold(0, |f, p| f + if p == '(' {1} else {-1})
}

fn solve_part_2(input: &String) -> usize{
    let mut floor = 0;
    let mut basement_index = 0;
    let mut step = input.chars().enumerate();
    while floor >= 0 {
        match step.next() {
            Some((_, '(')) => floor += 1,
            Some((i, ')')) => {
                floor -= 1;
                basement_index = i;
            }
            Some(_) => (),
            None => break
        };
    };
    basement_index + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_part1() {
        let examples = [
            ("(())", 0),
            ("()()", 0),
            ("(((", 3),
            ("(()(()(", 3),
            ("))(((((", 3),
            ("())", -1),
            ("))(", -1),
            (")))", -3),
            (")())())", -3)];
        for (example, floor) in examples.iter() {
            assert_eq!(
                floor,
                &solve_part_1(&String::from(example.to_string())));
        }
    }

    #[test]
    fn test_example_part2() {
        assert_eq!(1, solve_part_2(&String::from(")")));
        assert_eq!(5, solve_part_2(&String::from("()())")));
    }
}