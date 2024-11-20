# PDF Combiner and Watermark Script

This Python script combines multiple PDF files into one and applies a watermark to the combined PDF.

## Features

- Combines multiple PDFs into a single file (`super.pdf`).
- Adds a watermark to the combined PDF, generating a new file (`super_wtr.pdf`).

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Install the required Python library:
   ```bash
   pip install PyPDF2
   ```

## Usage

### Combine PDFs

Run the script and pass the names of the PDF files to combine as arguments:
```bash
python pdf.py file1.pdf file2.pdf file3.pdf
```

This generates a combined PDF named `super.pdf`.

### Add a Watermark

Make sure you have a watermark file (`wtr.pdf`) with a single page.

The script automatically applies the watermark to the combined PDF and saves the result as `super_wtr.pdf`.

## File Outputs

- **`super.pdf`**: The combined PDF file.
- **`super_wtr.pdf`**: The combined PDF with the watermark applied.

## Example

```bash
python pdf.py document1.pdf document2.pdf
```

Output files:
- `super.pdf`
- `super_wtr.pdf`

## Contributing

Feel free to fork this repository and submit pull requests to enhance its functionality.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
