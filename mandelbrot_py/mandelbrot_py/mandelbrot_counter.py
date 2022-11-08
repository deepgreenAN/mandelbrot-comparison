from numba import float32, uint32, jit


class Range:
    def __init__(self, start: float, end: float):
        self.start = start
        self.end = end


@jit(uint32(uint32, uint32, float32, float32, float32, float32, uint32), nopython=True)
def counter_func(pixel_x: int, pixel_y: int, real_start: float, comp_start: float, real_step: float, comp_step: float, max_count: int) -> int:
    c_real: float = real_start + pixel_x * real_step
    c_comp: float = comp_start + pixel_y * comp_step

    z_real: float = 0.0
    z_comp: float = 0.0

    counter: int = 0
    while counter < max_count and z_real * z_real + z_comp * z_comp < 1e10:
        z_real, z_comp = z_real * z_real - z_comp * \
            z_comp + c_real, 2 * z_real * z_comp + c_comp
        counter = counter + 1

    return counter


class MandelbrotCounter:
    def __init__(self, real_lim: Range, comp_lim: Range, image_size: tuple[int, int], max_count: int) -> None:
        self.real_lim = real_lim
        self.comp_lim = comp_lim
        self.step: tuple[float, float] = (
            (real_lim.end - real_lim.start) / image_size[0],
            (comp_lim.end - comp_lim.start) / image_size[1]
        )
        self.max_count = max_count

    def count(self, pixel_x: int, pixel_y: int) -> int:
        return counter_func(pixel_x, pixel_y, self.real_lim.start, self.comp_lim.start, self.step[0], self.step[1], self.max_count)

    def count_v2(self, pixel_x: int, pixel_y: int) -> int:
        c_real, c_comp = self.real_lim.start + pixel_x * \
            self.step[0], self.comp_lim.start + pixel_y * self.step[1]
        z_real, z_comp = 0.0, 0.0

        counter: int = 0
        while counter < self.max_count and z_real * z_real + z_comp * z_comp < 1e10:
            z_real, z_comp = z_real * z_real - z_comp * \
                z_comp + c_real, 2 * z_real * z_comp + c_comp
            counter = counter + 1

        return counter
