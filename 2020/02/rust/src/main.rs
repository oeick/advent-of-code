use std::error::Error;
use regex::Regex;

fn main() -> Result<(), Box<dyn Error>> {
    let input_file_content = std::fs::read_to_string(r"..\input.txt")?;

    let pattern = Regex::new(r"(\d+)-(\d+) (\w+): (.+)")?;

    let (mut counter1, mut counter2) = (0, 0);
    for line in input_file_content.lines(){
        let matches = pattern.captures(&line)
                             .expect(&format!("Unparsable line: '{}'", line));
        let low: usize = matches[1].parse()?;
        let high: usize = matches[2].parse()?;
        let character = matches[3].chars().next().unwrap();
        let code = &matches[4];
        let character_count = code.chars().filter(|&c| c == character).count();
        if (low..=high).contains(&character_count) {
            counter1 += 1;
        };
        if (code.chars().nth(low - 1) == Some(character)) != 
           (code.chars().nth(high - 1) == Some(character)) {
            counter2 += 1;
        }
    }
    println!("{}", counter1);
    println!("{}", counter2);

    Ok(())
}
