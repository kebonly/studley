use pyo3::prelude::*;
pub mod diffusion;
use rand::Rng;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// Returns an array of the first 100 time steps of 1-dimensional diffusion
#[pyfunction]
fn simulate_diffusion(diffusivity_constant: f64, x_0: f64, t: usize) -> PyResult<Vec<f64>> {

    let mut res: Vec<f64> = vec![0.; t];
    let mut rng = rand::thread_rng();
    let mut current: f64 = x_0;

    for x in res.iter_mut() {
        *x = current;
        current += rng.gen_range(-diffusivity_constant..diffusivity_constant);
    }
    Ok(res)
}

/// A Python module implemented in Rust.
#[pymodule]
fn string_sum(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(simulate_diffusion, m)?)?;
    Ok(())
}