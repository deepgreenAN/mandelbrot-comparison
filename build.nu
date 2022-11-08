# rustのビルド
cd mandelbrot_rs
cargo build --bin mandelbrot --release
cargo build --bin mandelbrot_multi_thread --release
cd ..
print "mandelbrot_rs build finished."

# pythonのビルド
cd mandelbrot_py
poetry install
cd ..
print "mandelbrot_py install finished."
