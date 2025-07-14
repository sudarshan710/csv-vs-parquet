# 📦 CSV vs Parquet Data Format Comparison

This is a small demonstration that compares the **CSV** and **Parquet** data formats in terms of size, compression, and integrity. It demonstrates how to:

- Convert a CSV file to Parquet with different compression methods.
- Compare file sizes.
- Verify data integrity after conversion.
- View raw binary content of a Parquet file.

---


## 📖 Overview

Parquet is a columnar storage format often used in big data and analytics applications. Compared to CSV, it offers:

✅ Better compression  
✅ Faster I/O performance  
✅ Support for complex nested data structures

This script illustrates a practical comparison between:

- Uncompressed CSV
- Parquet with **Zstandard (ZSTD)** compression
- Parquet with **GZIP** compression

---

## ⚙️ Requirements

- Python 3.7+
- `pandas`
- `pyarrow`

---

## 💾 Installation

Install the required libraries using pip:

```bash
pip install pandas pyarrow

```

## Sample Result Output

<img width="1396" height="635" alt="results" src="https://github.com/user-attachments/assets/42f021c5-da7e-40fe-a773-58f32acb4542" />
