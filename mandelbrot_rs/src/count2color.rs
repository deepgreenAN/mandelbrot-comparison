pub fn count_to_color(cnt: usize, max_count: usize) -> [u8; 3] {
    if cnt == max_count {
        [0, 0, 0] // 黒
    } else {
        [
            0,
            ((cnt as f32 / max_count as f32) * 255_f32) as u8,
            ((cnt as f32 / max_count as f32) * 255_f32) as u8,
        ]
    }
}
