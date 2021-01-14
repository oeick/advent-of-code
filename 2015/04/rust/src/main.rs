fn main() -> Result<(), Box<dyn std::error::Error>>{
    let input = std::fs::read_to_string(r"..\input.txt")?;
    println!("{}", solve1(&input));
    println!("{}", solve2(&input));
    Ok(())
}

fn solve1(input: &String) -> u32{
    let mut n = 1;
    loop {
        let b = md5::compute(input.to_owned() + &n.to_string()).0;
        if b[0] == 0 && b[1] == 0 && b[2] < 16 { break; }
        n += 1;
    }
    n
}

fn solve2(input: &String) -> u32{
    let mut n = 1;
    loop {
        let b = md5::compute(input.to_owned() + &n.to_string()).0;
        if b[0] == 0 && b[1] == 0 && b[2] == 0 { break; }
        n += 1;
    }
    n
}