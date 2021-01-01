use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
    let input = std::fs::read_to_string("input.txt")?;

    let floor = input.chars()
                     .fold(0, |f, p| f + if p == '(' {1} else {-1});
    println!("{}", floor);
    
    let mut floor = 0;
    let mut basement_index = None;
    let mut step = input.chars().enumerate();
    while floor >= 0 {
        match step.next() {
            Some((_, '(')) => floor += 1,
            Some((i @ _, ')')) => {
                floor -= 1;
                basement_index = Some(i);
            }
            Some(_) => (),
            None => break
        };
    };

    match basement_index {
        Some(i) => println!("{}", i + 1),
        None => println!("never reached basement")};

    Ok(())
}
