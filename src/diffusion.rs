use rand::Rng;
pub struct DiffusingParticle {
    current_position: u32, // Do i need to make these field public?
    next_position: u32
}

impl Iterator for DiffusingParticle {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        let current = self.current_position;
        let mut rng = rand::thread_rng();
        self.current_position = self.next_position;
        self.next_position = current + rng.gen_range(0..10);
        Some(current)
    }
}

pub fn diffusing_particle() -> DiffusingParticle {
    DiffusingParticle { current_position: 0, next_position: 0 }
}
