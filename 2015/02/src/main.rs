use std::error::Error;

struct Dimensions { x: u32, y: u32, z: u32 }

fn main() -> Result<(), Box<dyn Error>>{
    let input = std::fs::read_to_string("input.txt")?;

    let solution1: u32 = input
        .lines()
        .map(|a| a.split('x')
                  .map(|n| n.parse::<u32>().unwrap())
                  .collect())
        .map(|v: Vec<u32>| calc_paper(Dimensions{x: v[0], y: v[1], z: v[2]}))
        .sum();

    println!("{}", solution1);

    let solution2: u32 = input
        .lines()
        .map(|a| a.split('x')
                  .map(|n| n.parse::<u32>().unwrap())
                  .collect())
        .map(|v: Vec<u32>| calc_ribbon(Dimensions{x: v[0], y: v[1], z: v[2]}))
        .sum();

    println!("{}", solution2);

    Ok(())
}

fn calc_paper(d: Dimensions) -> u32{
    let areas = vec!(d.x*d.y, d.x*d.z, d.y*d.z);
    let smallest: u32 = areas.iter().min().unwrap().clone();
    2 * areas.iter().sum::<u32>() + smallest
}

fn calc_ribbon(d: Dimensions) -> u32{
    let perimeters = vec!(d.x+d.y, d.x+d.z, d.y+d.z);
    let smallest: u32 = perimeters.iter().min().unwrap().clone();
    2 * smallest + d.x*d.y*d.z
}