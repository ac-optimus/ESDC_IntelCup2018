
To prototype the idea implementation of pre-trained model of AOD-Net was first done on ASUS
laptop with Intel(R) Core(TM) i5-6200U CPU, 2.30GHz and later deployed on
UP Square board with Intel(R) Celeron(R) CPU N3350, 1.10GHz. The time taken to
perform dehaze CNN on a 300x300 image was 0.20658s on laptop while on UP Square it took
0.47023s. The CPU usage involved in both the cases were close to 95% which left no room for
any other process to perform simultaneously on UP Square. This was the reason why going with intel Movidus NCS was a good idea.
