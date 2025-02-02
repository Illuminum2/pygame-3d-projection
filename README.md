# Pygame 3D Engine

This project is a simple 3D engine written in Python with pygame, and includes projection using matrices and rotation using quaternions.

## How to Run

1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the `main.py` file:
    ```sh
    python main.py
    ```

3. To run the project on a website using `pygbag`:
    ```sh
    cd ..
    pygbag Pygame3DProjection
    ```
    You can access the project at [http://localhost:8000/](http://localhost:8000/).

## Controls

- **W**: Move forward
- **S**: Move backward
- **A**: Move left
- **D**: Move right
- **Q**: Move up
- **E**: Move down
- **Arrow Keys**: Rotate the camera (relative to world)
- **ESC**: Exit

## Technical Details

- **Projection**: Matrices for projecting 3D points onto a 2D screen.
- **Rotation**: Quaternions for rotation of the camera while avoiding gimbal lock.

## License

This project is licensed under the [MIT License](LICENSE.md).