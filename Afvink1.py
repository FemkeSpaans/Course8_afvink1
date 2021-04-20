# Author: Femke Spaans
# Date: 19-04-2021
# Name: Afvink 1
# Version: 1

from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)

@app.route('/')
def database_connection():
    conn = mysql.connector.connect(
        host="ensembldb.ensembl.org",
        user="anonymous",
        database="homo_sapiens_core_91_38",
        password="")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT description FROM gene;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

@app.route('/', methods=["POST","GET"])
def get_searchword():
    found_searchword = ""
    searchword = ""
    if request.method == "POST":
        searchword = request.form.get("searchword")
        print (searchword)
        found_searchword = filter_searchword(searchword)

def filter_searchword(searchword):
    conn = mysql.connector.connect(
        host="ensembldb.ensembl.org",
        user="anonymous",
        database="homo_sapiens_core_91_38",
        password="")
    cursor = conn.cursor()
    searchword = searchword.replace("#", "").replace("\'", "")
    cursor.execute(
        "SELECT description FROM gene WHERE description LIKE '%" + search_word + "%'")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

if __name__ == '__main__':
    app.run()
