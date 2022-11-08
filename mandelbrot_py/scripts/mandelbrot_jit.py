from PIL import Image
import numpy as np
from mandelbrot_py import Range, MandelbrotCounter, count_to_color

if __name__ == "__main__":
    image_size: tuple[int, int] = (1400, 1200)
    #image_size: tuple[int, int] = (140, 120)
    max_count: int = 100

    mandelbrot_counter = MandelbrotCounter(
        Range(-2.1, 0.7),
        Range(-1.2, 1.2),
        image_size,
        max_count
    )

    image_raw = np.empty([image_size[1], image_size[0], 3], dtype=np.uint8)

    for j in range(0, image_size[1]):  # pixel_x
        for i in range(0, image_size[0]):  # pixel_y
            image_raw[j, i] = count_to_color(
                mandelbrot_counter.count(i, j), max_count)

    image = Image.fromarray(image_raw)

    image.save("mandelbrot_py.png")
