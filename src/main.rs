use rand::Rng;
pub mod diffusion;
pub mod utils;

fn main() {
    let mut rng = rand::thread_rng();
    let dp1 = diffusion::diffusing_particle();
    // dp1.
    println!("Hello world! {}", rng.gen::<u32>());
    for i in dp1.take(25) {
        println!("Test {}", i);
    }
}