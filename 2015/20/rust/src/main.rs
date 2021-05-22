use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
    let input = std::fs::read_to_string(r"..\input.txt")?;
    let presents: usize = input.parse()?;
    println!("{:?}", solve_part_1(presents));
    println!("{:?}", solve_part_2(presents));
    Ok(())
}

fn solve_part_1(presents: usize) -> usize{
    let mut house: Vec<usize> = vec![10; presents/10];
    for elf in 2..=presents/10{
        for delivery in (elf..presents/10).step_by(elf){
            house[delivery] += elf * 10;
        }
    }
    house.iter().position(|p| p >= &presents).unwrap()
}

fn solve_part_2(presents: usize) -> usize{
    let mut house: Vec<usize> = vec![11; presents/11];
    for elf in 2..=presents/11{
        for delivery in (elf..presents/11).step_by(elf).take(50){
            house[delivery] += elf * 11;
        }
    }
    house.iter().position(|p| p >= &presents).unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(8, solve_part_1(130usize));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(4, solve_part_2(77usize));
    }
}