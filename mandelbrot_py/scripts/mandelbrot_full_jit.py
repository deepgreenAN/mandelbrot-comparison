import numpy as np
from PIL import Image

from numba import jit, uint32, uint8, void, float32
from mandelbrot_py import Range, counter_func


@jit(uint8[:](uint32, uint32), nopython=True)
def count_to_color_jit(count: int, max_count: int) -> np.ndarray:
    if count == max_count:
        return np.array([0, 0, 0], dtype=np.uint8)  # 黒
    else:
        return np.array([
            0,
            int((count / max_count) * 255),
            int((count / max_count) * 255)
        ], dtype=np.uint8)


@jit(void(uint8[:, :, :], float32, float32, float32, float32, uint32), nopython=True)
def mandelbrot(array: np.ndarray, real_start: float, comp_start: float, real_step: float, comp_step: float, max_count: int):
    for j in range(array.shape[0]):
        for i in range(array.shape[1]):
            count = counter_func(i, j, real_start, comp_start,
                                 real_step, comp_step, max_count)
            array[j][i] = count_to_color_jit(count, max_count)


if __name__ == "__main__":
    image_size: tuple[int, int] = (1400, 1200)
    #image_size: tuple[int, int] = (140, 120)
    max_count: int = 100

    real_lim = Range(-2.1, 0.7)
    comp_lim = Range(-1.2, 1.2)

    real_step = (real_lim.end - real_lim.start) / image_size[0]
    comp_step = (comp_lim.end - comp_lim.start) / image_size[1]

    image_row = np.empty([image_size[1], image_size[0], 3], dtype=np.uint8)
    mandelbrot(image_row, real_lim.start, comp_lim.start,
               real_step, comp_step, max_count)

    image = Image.fromarray(image_row)
    image.save("mandelbrot_full_jit.png")
