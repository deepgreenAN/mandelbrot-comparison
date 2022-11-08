use image::RgbImage;
use mandelbrot_rs::count_to_color;
use mandelbrot_rs::MandelbrotCounter;
use std::error::Error;
use std::sync::mpsc::channel;
use std::thread;

fn main() -> Result<(), Box<dyn Error>> {
    let image_size = (1400_usize, 1200_usize); // width, height
    let max_count = 100_usize;

    let mandelbrot_counter = MandelbrotCounter::new(
        -2.1_f64..0.7_f64, // 実部の範囲
        -1.2_f64..1.2_f64, // 虚部の範囲
        image_size,
        max_count,
    );

    let (tx, rx) = channel::<(usize, usize, usize)>();

    let n_cpus = num_cpus::get();

    let chunks_range = (0..n_cpus).map(|i| {
        i * image_size.0 * image_size.1 / n_cpus..(i + 1) * image_size.0 * image_size.1 / n_cpus
    });

    for range in chunks_range {
        let tx = tx.clone();
        let mandelbrot_counter = mandelbrot_counter.clone();
        thread::spawn(move || {
            for i in range {
                let x = i % image_size.0;
                let y = i / image_size.0;
                tx.send((x, y, mandelbrot_counter.count(x, y))).unwrap();
            }
        });
    }

    let mut img = RgbImage::new(image_size.0 as u32, image_size.1 as u32);

    for _ in 0..image_size.0 * image_size.1 {
        // rx.recvをイテレータとするとエラーを補足できない
        let (x, y, cnt) = rx.recv()?;
        img.put_pixel(x as u32, y as u32, count_to_color(cnt, max_count).into());
    }

    img.save("mandelbrot_multi_thread.png")?;

    Ok(())
}
