use std::ops::Range;

#[derive(Clone)]
pub struct MandelbrotCounter {
    real_lim: Range<f64>,
    complex_lim: Range<f64>,
    step: (f64, f64),
    max_count: usize,
}

impl MandelbrotCounter {
    pub fn new(
        real_lim: Range<f64>,
        complex_lim: Range<f64>,
        image_size: (usize, usize), // width, height
        max_count: usize,
    ) -> Self {
        let step = (
            (real_lim.end - real_lim.start) / image_size.0 as f64,
            (complex_lim.end - complex_lim.start) / image_size.1 as f64,
        );
        Self {
            real_lim,
            complex_lim,
            step,
            max_count,
        }
    }
    pub fn count(&self, pixel_x: usize, pixel_y: usize) -> usize {
        let c = (
            self.real_lim.start + (pixel_x as f64) * self.step.0,
            self.complex_lim.start + (pixel_y as f64) * self.step.1,
        );

        let mut z = (0.0, 0.0); // 更新用の複素数
        let mut cnt = 0_usize;

        while cnt < self.max_count && z.0 * z.0 + z.1 * z.1 <= 1e10 {
            z = (z.0 * z.0 - z.1 * z.1 + c.0, 2.0 * z.0 * z.1 + c.1);
            cnt += 1;
        }
        cnt
    }
}
