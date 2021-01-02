use std::collections::HashSet;

fn main() -> Result<(), Box<dyn std::error::Error>>{
    let input = std::fs::read_to_string(r"input.txt")?;
    println!("{}", solve_part1(&input));
    println!("{}", solve_part2(&input));
    Ok(())
}

fn solve_part1(input: &String) -> usize{
    get_locations(input, 0, 1).len()
}

fn solve_part2(input: &String) -> usize{
    let locations_santa = get_locations(&input, 0, 2);
    let locations_robot = get_locations(&input, 1, 2);
    locations_santa.union(&locations_robot)
        .collect::<Vec<&(i32, i32)>>()
        .len()
}

fn get_locations(input: &String, skip: usize, step: usize) -> HashSet<(i32, i32)>{
    let (mut x, mut y) = (0, 0);
    let mut locations: HashSet<(i32, i32)> = HashSet::new();
    locations.insert((0, 0));
    input.chars().skip(skip).step_by(step)
        .for_each(|direction| {
            match direction {
                '^' => y += 1,
                '>' => x += 1,
                'v' => y -= 1,
                '<' => x -= 1,
                _ => ()}
            locations.insert((x, y));
        });
    locations
}
