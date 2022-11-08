def count_to_color(count: int, max_count: int) -> tuple[int, int, int]:
    if count == max_count:
        return (0, 0, 0)  # 黒
    else:
        return (
            0,
            int((count / max_count) * 255),
            int((count / max_count) * 255)
        )
