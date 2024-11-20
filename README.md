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

MIT License

Copyright (c) 2024 Agostina Svenson.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

