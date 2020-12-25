use std::time::Instant;

fn main() {
    let ids = String::from("29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,661,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,521,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19");
    let id_list: Vec<(usize, i64)> = ids
        .split(',')
        .enumerate()
        .filter(|(_i, s)| *s != "x")
        .map(|(i, s)| (i, s.parse::<i64>().unwrap()))
        .collect();

    let (max_id_index, max_id_value) = id_list
                                        .iter()
                                        .max_by_key(|i| i.1)
                                        .unwrap();

    println!("{}, {}", max_id_index, max_id_value);
    
    let id_list_relative: Vec<(i64, i64)> = id_list
        .iter()
        .map(|(i, v)| (*i as i64 - *max_id_index as i64, *v))
        .collect();
    
    let mut id_list_rel_sort = id_list_relative;
    id_list_rel_sort.sort_by_key(|i| i.1);
    id_list_rel_sort.reverse();
    
    println!("{:?}", id_list_rel_sort);

    let start_value: i64 = 100_000_000_000_000;

    let mut relative_t: Vec<i64> = id_list_rel_sort
        .iter()
        .map(|(_i, v)| start_value / *v * *v)
        .collect();

    println!("{:?}", relative_t);

    let mut t0 = Instant::now();
    loop {
        relative_t[0] += id_list_rel_sort[0].1;
        let mut valid = true;
        for (n, (i, v)) in id_list_rel_sort.iter().enumerate().skip(1){
            while relative_t[n] < relative_t[0] + *i{
                relative_t[n] += v;
            }
            if relative_t[n] > relative_t[0] + *i {
                valid = false;
                break;
            }
        }
        if valid {
            break;
        }
        if t0.elapsed().as_secs() >= 10{
            println!("{:?}", relative_t);
            t0 = Instant::now();
        }
    }

    println!("{:?}", relative_t);
    println!("{}", relative_t.iter().min().unwrap());
}
