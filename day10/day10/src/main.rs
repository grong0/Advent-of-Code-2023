use std::collections::HashMap;
use std::fs::File;
use std::io::prelude::*;
use std::str::FromStr;

struct Pos {
    value: char,
    row: usize,
    col: usize,
}
impl Pos {
    fn get_value(&self) -> char {
        return self.value;
    }
    fn get_row(&self) -> usize {
        return self.row;
    }
    fn get_col(&self) -> usize {
        return self.col;
    }
    fn to_string(&self) -> &'static str {
        return String::from_str("Value of '").unwrap() + self.value.to_string() + String::from_str("' at row ").unwrap() + self.row.to_string() + String::from_str(" and col ").unwrap() + self.col.to_string() + String::from_str(".").unwrap();
    }
}

struct GridHandler {
    grid: Vec<Vec<Pos>>
}
impl GridHandler {
    fn get_grid(self) -> Vec<Vec<Pos>> {
        return self.grid;
    }
    fn get_neighbors(&self, pos: &Pos) -> HashMap<&str, &Pos> {
        let mut neighbors = HashMap::new();
        if let Some(row) = self.grid.get(pos.get_row()-1) {
            if let Some(col) = row.get(pos.get_col()) {
                neighbors.insert("north", col);
            }
        }
        if let Some(row) = self.grid.get(pos.get_row()) {
            if let Some(col) = row.get(pos.get_col()+1) {
                neighbors.insert("east", col);
            }
        }
        if let Some(row) = self.grid.get(pos.get_row()+1) {
            if let Some(col) = row.get(pos.get_col()) {
                neighbors.insert("south", col);
            }
        }
        if let Some(row) = self.grid.get(pos.get_row()) {
            if let Some(col) = row.get(pos.get_col()-1) {
                neighbors.insert("west", col);
            }
        }
        return neighbors;
    }
}

fn main() {
    let mut file = File::open("../day10.txt").expect("no file");

    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("cant read files");

    let mut grid: Vec<Vec<Pos>> = vec![];
    for (row_index, line) in contents.split("\n").enumerate() {
        let mut row: Vec<Pos> = vec![];
        for (col_index, char) in line.chars().enumerate() {
            let pos = Pos{ value: char, row: row_index, col: col_index };
            row.push(pos);
        }
        grid.push(row);
    }
    let grid = GridHandler { grid };

    for row in grid.get_grid() {
        for col in row {
            print!("{}", col.);
        }
    }
}
