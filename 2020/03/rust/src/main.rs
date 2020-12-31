use std::error::Error;

fn main() -> Result<(), Box<dyn Error>>{
    let input_file = std::fs::read_to_string(r"..\input.txt")?;
    // let mut col = 0;
    // let mut counter = 0;
    // for line in input_file.lines(){
    //     if line.chars().nth(col) == Some('#'){
    //         counter += 1;
    //     }
    //     col = (col + 3) % line.len();
    // }
    let counter: usize = input_file
        .lines()
        .enumerate()
        .filter(|(i, line)| line.chars().nth(i*3 % line.len()) == Some('#') )
        .count();
    println!("{}", counter);
    Ok(())
}
