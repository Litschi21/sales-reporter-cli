import argparse
import logging
import os
import pandas as pd

"""
Dash Reporter: combines sales, customer and products data to create a
sales report
"""

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_SALES_PATH = os.path.join(SCRIPT_DIR, 'sales.csv')
DEFAULT_CUSTOMER_PATH = os.path.join(SCRIPT_DIR, 'customer.csv')
DEFAULT_PRODUCTS_PATH = os.path.join(SCRIPT_DIR, 'products.csv')
DEFAULT_REPORT_PATH = os.path.join(SCRIPT_DIR, 'sales_report.csv')

logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), 'sales_report.log'),
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

parser = argparse.ArgumentParser()
parser.add_argument('--sales_path', default=DEFAULT_SALES_PATH, help='Path to your sales data')
parser.add_argument('--customer_path', default=DEFAULT_CUSTOMER_PATH, help='Path to your customer data')
parser.add_argument('--products_path', default=DEFAULT_PRODUCTS_PATH, help='Path to your products data')
parser.add_argument('--sales_report_path', default=DEFAULT_REPORT_PATH, help='Path you would like to save sales report to')
parser.add_argument('--version', action='version', version='Dash Reporter 1.0')

args = parser.parse_args()

def load_data(sales_csv, customer_csv, products_csv):
    """
    Creates 3 dataframes from 3 csv file paths

    Args:
        str: sales csv filepath
        str: customer csv filepath
        str: products csv filepath
    
    Returns:
        DataFrame: sales dataframe
        DataFrame: customer dataframe
        DataFrame: products dataframe
    """
    
    logging.info('Reading csv files...')
    try:
        sales_df = pd.read_csv(sales_csv)
        customer_df = pd.read_csv(customer_csv)
        products_df = pd.read_csv(products_csv)
    except Exception as e:
        logging.error(f'An error occured while trying to read csv files: {e}')
        return None

    return sales_df, customer_df, products_df

def merge_data(sales, customer, products):
    """
    Merges data from all 3 csvs

    Args:
        DataFrame: sales dataframe
        DataFrame: customer dataframe
        DataFrame: products dataframe
    
    Returns:
        DataFrame: merged df from all 3
    """

    logging.info('Merging data...')
    try:
        merged_df = pd.merge(sales, customer, on='customer_id')
        merged_df = pd.merge(merged_df, products, on='product_id')
    except Exception as e:
        logging.error(f'Merge failed: {e}')
        return None

    return merged_df

def sales_report(merged_df, sales_report_path):
    """
    Creates sales report ranking revenue, quantity,
    customers, etc in descending order

    Args:
        DataFrame: merged df to extract from
    
    Returns:
        DataFrame: sorted sales report df
    """

    logging.info('Generating sales report...')
    merged_df['total_revenue'] = round(merged_df['quantity'] * merged_df['price'], 2)

    sorted_df = merged_df.sort_values(by='total_revenue', ascending=False)
    sorted_df.to_csv(sales_report_path)
    return sorted_df

def main():
    """
    Loads csvs, merges csvs, then prints head() and info()

    Args:
        None
    
    Returns:
        None
    """

    sales, customer, products = load_data(args.sales_path, args.customer_path, args.products_path)
    
    merged_df = merge_data(sales, customer, products)

    sales_report(merged_df, args.sales_report_path)

if __name__ == '__main__':
    main()
