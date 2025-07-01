**Dash Reporter** - The quick and easy to use sales report generator
This project is (obviously) useful for generating sales reports by merely
adding the customer info, the product info and then your sales (report example at the end)

**Why Dash Reporter?**
Dash Reporter is the ultimate tool for creating a sales report in mere seconds!
You can spare yourself money AND time by simply using Dash Reporter.
Just enter the paths to your data and you're done! (arguments in the cli are supported using argparse!)

This project runs with the following dependencies:
- *Python 3.x*
- *Pandas*

You can run this script simply by downloading the pandas library using
*pip install pandas*
and then just run it using Python.

Example customer csv:
customer_id,name,email
101,Alice Smith,alice@example.com
102,Bob Johnson,bob@example.com
103,Charlie Lee,charlie@example.com
104,Diana King,diana@example.com
105,Edward Scott,edward@example.com

Example products csv:
product_id,product_name,category
201,Wireless Mouse,Electronics
202,Notebook,Stationery
203,Pen,Stationery
204,Headphones,Electronics

Example sales csv:
sale_id,customer_id,product_id,quantity,price,date
1,101,201,2,19.99,2024-01-15
2,102,203,1,5.49,2024-01-17
3,103,202,5,3.99,2024-01-18
4,101,202,3,3.99,2024-01-20
5,104,204,1,49.99,2024-01-21
6,102,201,2,19.99,2024-01-22
7,105,203,4,5.49,2024-01-23

**Important: Only the ids are needed for this to work, the rest is optional**
**Make sure your you have spelled the columns correctly**
