use std::error::Error;

const UNLIMITED: usize = usize::MAX;

fn main() -> Result<(), Box<dyn Error>>{
    let input = std::fs::read_to_string(r"..\input.txt")?;
    let presents: usize = input.parse()?;
    println!("{:?}", solve(presents, 10, UNLIMITED));
    println!("{:?}", solve(presents, 11, 50));
    Ok(())
}

fn solve(presents: usize, capacity: usize, limit: usize) -> usize{
    let mut house: Vec<usize> = vec![0; presents/capacity];
    for elf in 1..=presents/capacity{
        for delivery in (elf-1..presents/capacity).step_by(elf).take(limit){
            house[delivery] += elf * capacity;
        }
    }
    match house.iter().position(|p| p >= &presents) {
        Some(house_number) => house_number + 1,
        None               => 0
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_1() {
        assert_eq!(8, solve(130, 10, UNLIMITED));
    }

    #[test]
    fn test_part_2() {
        assert_eq!(4, solve(71, 11, UNLIMITED));
        assert_eq!(6, solve(71, 11, 3));
    }
}