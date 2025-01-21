```markdown
# SubGhost

**SubGhost** is a powerful subdomain discovery tool. It helps you discover hidden or less visible subdomains for a given domain using public API services. The tool is designed to be simple to use while offering great flexibility, such as the ability to choose the output format for results.

---

## Features

- Discover subdomains for one or multiple domains.
- Support for different output formats (TXT, CSV).
- Automatic domain format validation.
- Error and exception handling.
- Clear and intuitive user interface.
- Option to display subdomains directly in the console.
- Customizable options for data output.
- Support for bulk domain processing.

---

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/HackfutSec/SubGhost.git
```

Navigate into the project directory:

```bash
cd SubGhost
```

Ensure you have the necessary dependencies installed. You can use `pip` to install the required libraries:

```bash
pip install -r requirements.txt
```

The main libraries required are `requests` and `pystyle`.

---

## Usage

### Running the Tool

After installing the dependencies, you can run the tool by executing the Python script:

```bash
python subghost.py
```

The tool will prompt you to enter one or more domains to explore, as well as your preferred output format (`txt` or `csv`).

### Example Usage

```bash
[] Enter the domain(s) (e.g., google.com or google.com,example.com): google.com
[] Choose file format (txt/csv): txt
[] Searching for subdomains of google.com...
[] Subdomains saved to google.com_subdomains.txt
```

---

## Options

- **Domains**: You can enter one or multiple domains, separated by commas, to search for their subdomains.
- **File format**: Choose between `txt` or `csv` for the output format of the results.
- **Subdomain display**: Option to display the discovered subdomains directly in the console.

---

## Example Output

### `.txt` Format
The `.txt` file will contain a list of discovered subdomains for each domain, one per line:

```
subdomain1.google.com
subdomain2.google.com
subdomain3.google.com
```

### `.csv` Format
The `.csv` file will contain the subdomains in rows with one subdomain per line:

```
subdomain1.google.com
subdomain2.google.com
subdomain3.google.com
```

---

## Contributing

We encourage contributions to this project! If you’d like to contribute, follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit the changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature-branch`).
6. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## Authors

- **HackFutSec** – Lead developer, creator of the tool.

---

## Disclaimer

**SubGhost** is an educational and testing tool designed for use in controlled environments. The use of this tool for malicious purposes is strictly prohibited. The author of the project is not responsible for any damages caused by the use of this tool.
```
