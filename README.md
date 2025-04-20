# Meteorite Landings Analysis

This project analyzes meteorite landings across the globe using Python, PostgreSQL, and data visualization tools. It consists of a PostgreSQL data loader and a Jupyter notebook for exploratory data analysis (EDA).

## Project Structure

```
├── Meteorite_Landings.ipynb       # Notebook for EDA & visualization
├── postgres_csv_insert.py         # Script to load CSV into PostgreSQL
├── README.md                      # Project documentation
└── data/                          # (Optional) Directory for your CSV data
```

## Dataset Source

- Dataset: [NASA Open Data Portal – Meteorite Landings](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh)

## Technologies Used

- Python 3.8+
- PostgreSQL
- Jupyter Notebook
- Pandas & Matplotlib
- psycopg2 (PostgreSQL adapter)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/meteorite-landings.git
cd meteorite-landings
```

### 2. Install Dependencies

```bash
pip install pandas psycopg2 matplotlib jupyter
```

### 3. PostgreSQL Setup

- Create a PostgreSQL database (e.g., `meteorite_db`)
- Update connection credentials in `postgres_csv_insert.py`
- Place your CSV file in a `data/` directory (or modify path in script)

### 4. Load Data into PostgreSQL

```bash
python postgres_csv_insert.py
```

### 5. Run the Jupyter Notebook

```bash
jupyter notebook Meteorite_Landings.ipynb
```

## Sample Insights

- Most common meteorite classes
- Distribution of meteorite masses
- Meteorite fall types (e.g., "Fell" vs "Found")

## TODO

- [ ] Add folium for map-based visualizations
- [ ] Build a Streamlit dashboard
- [ ] Export filtered results as CSV

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Thanks to NASA for providing open data!

