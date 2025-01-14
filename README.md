# Vulnerability Scanner

## Overview
Vulnerability Scanner is a Python-based static code analysis tool designed to identify potential vulnerabilities in C++ source code. By scanning through the file, it detects unsafe function usages, unchecked inputs, and other common security issues, providing developers with actionable insights to improve code security.

## Features
- Identifies vulnerabilities such as:
  - Unchecked input (`cin`)
  - Buffer overflows (`strcpy`, `strcat`)
  - Unsafe function usage (`gets`)
  - Hardcoded credentials (`password`)
  - Command injection (`system`)
  - Unchecked memory allocation (`malloc`, `new`)
  - Null pointer dereference (`nullptr`)
  - Use-after-free vulnerabilities (`free`)
  - Insecure random number generation (`rand`)
  - Integer overflow/underflow (`+`)
- Highlights the line number and specific token causing the issue.
- Avoids duplicate reporting of vulnerabilities.

## Prerequisites
- Python 3.6+
- `ply` library for Python (can be installed using `pip install ply`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd VulnerabilityScanner
   ```
2. Install dependencies:
   ```bash
   pip install ply
   ```

## Usage
1. Run the script:
   ```bash
   python3 vulnerability_scanner.py
   ```
2. Enter the path to the C++ file when prompted:
   ```
   Enter the path to the C++ file: /path/to/your/code.cpp
   ```
3. The tool scans the file and provides a detailed report of vulnerabilities, including line numbers and descriptions.

### Example Output
```plaintext
Vulnerabilities Found:
Line 10: Potential buffer overflow vulnerability. (Token: strcpy)
Line 22: Command injection vulnerability. (Token: system)
Line 45: Potential null pointer dereference. (Token: nullptr)
```

## How It Works
1. **Lexical Analysis:**
   - Tokenizes the input C++ code to identify key elements such as identifiers, operators, keywords, and symbols.
   - Reserved keywords like `if`, `for`, `while`, and `include` are handled separately.

2. **Vulnerability Detection:**
   - Matches tokens (identifiers) against a predefined list of vulnerabilities.
   - Avoids duplicate reports by tracking previously reported issues using a set.

3. **Reporting:**
   - Outputs a clear and concise report highlighting vulnerabilities with line numbers and descriptions.

## Limitations
- The tool does not execute the code and cannot detect runtime vulnerabilities.
- It is tailored for C++ code and may not support other languages.

## Contributing
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to improve the tool.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any questions or feedback, please reach out to the repository maintainer.

