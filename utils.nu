export def bench [
    command: block  # Run this block
    n: int  # Repeat this number of times
    --ignore(-i)  # Ignore the stdout and stderr
    --echo(-e)  # Echo the list of benchmark
] {
    let times = for _ in 0..$n {
        if ($ignore) {
            benchmark {do -i $command} | $in / 1.0sec  # 秒で割る
        } else {
            benchmark $command | $in / 1.0sec  # 秒で割る
        }
    }
    if ($echo) { echo $times }
    {mean: ($times | math avg ), std: ($times | math stddev)}
}