# Image to GIF Converter

This project is a simple Python script that converts a list of images into an animated GIF using the `imageio` library. It runs with **Python 3.5 or later**. Example input and output images are provided for reference.

***

## Features

- Converts multiple images (PNG or JPG) into a GIF
- Easy-to-modify code for custom animation timing
- Example images included for immediate testing

***

## Requirements

- **Python version:** 3.5+
- **Library:** [imageio](https://imageio.github.io/)

***

## Installation

1. Clone the repository or download the code.
2. Ensure you have Python 3.5 or above installed.
3. Install the required library:

```bash
pip install imageio
```

4. Place your input images (e.g., `team-pic1.png`, `team-pic2.png`) in the project directory.

***

## Usage

1. Update the `filenames` list in the script to include your desired images.
2. Run the script:

```bash
python Image-gif.py
```

3. The script will create an `output.gif` in the project directory.

***

## Example

- **Input images:**
    - ![team-pic1 sample input]
    - ![team-pic2 sample input]
- **Output GIF:**
    - ![output sample GIF]

***

## How it Works

The script reads the provided images using `imageio.v3`, stores them in a list, and then writes them as frames to an animated GIF file.

```python
import imageio.v3 as iio

filenames = ['team-pic1.png', 'team-pic2.png']

images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('output.gif', images, duration=0.5)
```

*Edit `filenames` as needed and adjust `duration` for frame timing.*

***

## Contributing

Feel free to open issues or submit pull requests to add new features or fix bugs.

***

## License

This project is licensed under the MIT License.

***

**For any questions or support, contact the repository owner through GitHub.**

<div style="text-align: center">⁂</div>

[^1]: Image-gif.py

[^2]: output.jpg

[^3]: team-pic1.jpg

[^4]: team-pic2.jpg

