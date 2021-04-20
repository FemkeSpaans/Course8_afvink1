# Author: Femke Spaans
# Date: 19-04-2021
# Name: Afvink 1
# Version: 1

from flask import Flask, render_template, request, url_for
import mysql.connector

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    bold_searchword=None
    if request.method == "POST":
        searchword = get_searchword()
        rows = filter_searchword(searchword)
        bold_searchword = bold(rows, searchword)
    return render_template("afvink1.html", rows=bold_searchword)


def get_searchword():
    searchword = request.form.get("searchword")
    return searchword


def filter_searchword(searchword):
    conn = mysql.connector.connect(
        host="ensembldb.ensembl.org",
        user="anonymous",
        database="homo_sapiens_core_91_38",
        password="")
    cursor = conn.cursor()
    searchword = searchword.replace("#", "").replace("\'", "")
    cursor.execute(
        "SELECT description FROM gene WHERE description LIKE '%" + searchword + "%'")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def bold(rows, searchword):
    bold_searchword = []
    for row in rows:
        bold_result = str(row[0]).replace(searchword, fr"<b>{searchword}</b>")
        bold_searchword.append(bold_result)
    return bold_searchword


if __name__ == '__main__':
    app.run()

