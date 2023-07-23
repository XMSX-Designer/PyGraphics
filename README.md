# Spectrax

Spectrax is a powerful graphics rendering library for Python that allows you to create stunning visualizations and graphics with ease. This library provides a range of features to simplify the process of rendering graphics, making it ideal for game development, data visualization, and other graphic-intensive applications.

## Features

- High-performance rendering engine for smooth and fast graphics.
- Supports multiple backends, including Pygame and PIL (Pillow), to fit your specific requirements.
- Simplified interface for handling mouse and keyboard events with the EventLoop class.
- Convenient Font class for rendering text with various options.
- Easily create windows, draw textures, and present the rendered graphics.

## Installation

To use Spectrax, you need to have Python installed on your system. You can then install the library using pip:

```bash
pip install spectrax
```

## Getting Started

### Example 1: Creating a Basic Window

```python
from spectrax import display

# Create a window with the title "My Spectrax Window"
window = display.Window("My Spectrax Window")

# Clear the window and render
window.clear()
window.render()
```

### Example 2: Drawing a Texture

```python
from spectrax import display, texture

# Create a window with the title "My Spectrax Window"
window = display.Window("My Spectrax Window")

# Load an image and create a texture
texture = texture.Texture(filename="path/to/image.png")

# Draw the texture on the window
window.clear()
window.draw(texture)
window.render()
```

## Documentation

For detailed documentation and usage instructions, check out the [Spectrax Documentation](https://github.com/XMSX-Designer/spectrax/wiki).

## Contributions

We welcome contributions from the community! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

Spectrax is released under the [MIT License](https://github.com/XMSX-Designer/spectrax/blob/main/LICENSE).
