# Google Dork Scanner

A command-line tool for automating Google dork searches against specific domains and saving the results.

## Overview

This tool allows you to run a list of Google dorks against a target domain, collecting and saving the search results. It's useful for security researchers, penetration testers, and system administrators who want to discover potentially sensitive information exposed on their domains.

## Features

- Run multiple Google dorks against a specific domain
- Customize the number of results per search
- Configurable delay between searches to avoid rate limiting
- Progress tracking with rich console output
- Save results in JSON format for further analysis

### Prerequisites

- Python 3.6+
- pip (Python package manager)

### Setup

1. Clone this repository or download the source code:

```bash
git clone https://github.com/yourusername/google-dork-scanner.git
cd google-dork-scanner
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

If you don't have a requirements.txt file, you can install the dependencies directly:

```bash
pip install typer googlesearch-python rich
```

## Usage

Run the tool using the following command:

```bash
python main.py --dorks-file DORKS_FILE --domain DOMAIN --output-file OUTPUT_FILE [OPTIONS]
```

### Required Arguments

- `--dorks-file`: Path to a text file containing Google dorks (one per line)
- `--domain`: The target domain to search within
- `--output-file`: Path to save the JSON results

### Optional Arguments

- `--num-results`: Number of results to retrieve per search (default: 10)
- `--delay-range`: Delay range in seconds between requests, format: "min,max" (default: "2,5")

### Example

```bash
python main.py --dorks-file dorks.txt --domain example.com --output-file results.json --num-results 15 --delay-range "3,7"
```

## Creating a Dorks File

Create a text file with one Google dork per line. For example:

```
inurl:admin
intitle:"Index of"
filetype:pdf
intext:password
ext:sql
```

## Output Format

The tool saves results in JSON format:

```json
[
    {
        "dork": "inurl:admin",
        "result": "https://example.com/admin/login.php"
    },
    {
        "dork": "filetype:pdf",
        "result": "https://example.com/documents/report.pdf"
    }
]
```

## How It Works

The tool performs the following steps:
1. Reads the list of dorks from the specified file
2. For each dork, constructs a Google search query combining the dork with the target domain
3. Executes the search and collects the results
4. Adds a random delay between searches to avoid triggering Google's rate limiting
5. Saves all collected results to a JSON file

## Troubleshooting

### Common Issues

1. **Google blocking requests**: If you see errors related to search requests, Google might be temporarily blocking your IP. Try increasing the delay between requests.

2. **Module not found errors**: Ensure all dependencies are installed correctly using the installation commands above.

3. **Permission errors**: Make sure you have write permissions for the output file location.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Caution

- Use this tool responsibly and only on domains you own or have permission to test
- Excessive queries to Google may result in your IP being temporarily blocked
- Adjust the delay between requests to avoid triggering Google's rate limiting

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is provided for educational and legitimate security testing purposes only. The authors are not responsible for any misuse or damage caused by this program.
```