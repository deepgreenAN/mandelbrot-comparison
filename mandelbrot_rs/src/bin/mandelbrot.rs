use image::RgbImage;
use mandelbrot_rs::count_to_color;
use mandelbrot_rs::MandelbrotCounter;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let image_size = (1400_usize, 1200_usize); // width, height
    let max_count = 100_usize;

    let mandelbrot_counter = MandelbrotCounter::new(
        -2.1_f64..0.7_f64, // 実部の範囲
        -1.2_f64..1.2_f64, // 虚部の範囲
        image_size,
        max_count,
    );

    let count_iter = (0..image_size.0 * image_size.1).map(|i| {
        let x = i % image_size.0;
        let y = i / image_size.0;
        (x, y, mandelbrot_counter.count(x, y))
    });

    let mut img = RgbImage::new(image_size.0 as u32, image_size.1 as u32);

    for (x, y, cnt) in count_iter {
        img.put_pixel(x as u32, y as u32, count_to_color(cnt, max_count).into());
    }

    img.save("mandelbrot_rust.png")?;
    Ok(())
}
