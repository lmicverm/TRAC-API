from flask import Flask
from flask import request, Response
# import pandas as pd

app = Flask(__name__)

# df = pd.read_csv("./data.csv", delimiter=",") 


@app.route("/")
def hello():
    return "Hello, this is a simple API app for the delaware TRAC!"

@app.route("/api/productSalesDetails", methods=["POST"])
def get_product_sales_details():
    print(">>> get_product_sales_details got a request")
    # post_data = request.get_json()
    # product_id = post_data.get("product_id", None)
    # if product_id is not None:
    #     print(f"Product ID = {product_id}")
    #     return Response(str(df[df["product_id"]==int(product_id)].to_json(orient="records")), status=200, mimetype="application/json")
    # else:
    #     print("Nonetype as product_id")
    return Response("No product_id was given in the request", status=403, mimetype="application/json")

