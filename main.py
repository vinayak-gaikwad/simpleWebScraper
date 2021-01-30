# PL LAB ESE
# TOPIC: Python List
# PRN: 2019BTECS00032
# NAME: VINAYAK DNYANESHWAR GAIKWAD

from bs4 import BeautifulSoup
import requests

popular_movies_list = []
top_movies_list = []
top_shows_list = []
popular_shows_list = []


def getTopShows():
    popular_shows = "https://www.imdb.com/chart/toptv"
    html_page = requests.get(popular_shows).text
    page_info = BeautifulSoup(html_page, 'lxml')
    shows = page_info.find_all("tr")
    i = 1
    for show in shows:
        titleColumn = show.find('td', class_="titleColumn")
        ratingColumn = show.find('td', class_="ratingColumn")

        if titleColumn == None:
            continue
        title = titleColumn.a
        rating = ratingColumn.strong

        if rating != None:
            top_shows_list.append(
                {"Rank": i, "Name": title.text, "Rating": rating.text})
            i += 1


def getTopMovies():
    popular_shows = "https://www.imdb.com/chart/top"
    html_page = requests.get(popular_shows).text
    page_info = BeautifulSoup(html_page, 'lxml')
    shows = page_info.find_all("tr")
    i = 1
    for show in shows:
        titleColumn = show.find('td', class_="titleColumn")
        ratingColumn = show.find('td', class_="ratingColumn")

        if titleColumn == None:
            continue
        title = titleColumn.a
        rating = ratingColumn.strong

        if rating != None:
            top_movies_list.append(
                {"Rank": i, "Name": title.text, "Rating": rating.text})
            i += 1


def getPopularMovies():
    popular_shows = "https://www.imdb.com/chart/moviemeter"
    html_page = requests.get(popular_shows).text
    page_info = BeautifulSoup(html_page, 'lxml')
    shows = page_info.find_all("tr")

    for show in shows:
        titleColumn = show.find('td', class_="titleColumn")
        ratingColumn = show.find('td', class_="ratingColumn")

        if titleColumn == None:
            continue
        title = titleColumn.a
        year = titleColumn.span
        rank = titleColumn.div
        rating = ratingColumn.strong

        if rating != None:
            popular_movies_list.append(
                {"Rank": rank.text, "Name": title.text, "Rating": rating.text, "Year": year.text})


def getPopularShows():
    popular_shows = "https://www.imdb.com/chart/tvmeter"
    html_page = requests.get(popular_shows).text
    page_info = BeautifulSoup(html_page, 'lxml')
    shows = page_info.find_all("tr")
    for show in shows:
        titleColumn = show.find('td', class_="titleColumn")
        ratingColumn = show.find('td', class_="ratingColumn")

        if titleColumn == None:
            continue
        title = titleColumn.a
        year = titleColumn.span
        rank = titleColumn.div
        rating = ratingColumn.strong

        if rating != None:
            popular_shows_list.append(
                {"Rank": rank.text, "Name": title.text, "Rating": rating.text, "Year": year.text})


print("Loading ...")
print("Fetching popular shows ....")
getPopularShows()
print("Fetching popular movies ....")
getPopularMovies()
print("Fetching top rated movies ....")
getTopMovies()
print("Fetching top rated shows ....")
getTopShows()

flag = 1
while flag:
    print("============================================")
    print("Please Select what from below to see list")
    print("1. Top Rated Movies")
    print("2. Top Rated TV Shows")
    print("3. Popular Movies")
    print("4. Popular TV Shows")
    print()
    print("5. Exit")
    option = int(input("Enter your option: "))

    if option == 1:
        print("==================================================")
        print("TOP RATED MOVIES")
        print("==================================================")
        for data in top_movies_list:
            print()
            print("Rank: {} ".format(data["Rank"]))
            print("Title: {} ".format(data["Name"].strip()))
            print("Rating: {} ".format(data["Rating"].strip()))
            print("\n")
    if option == 2:
        print("==================================================")
        print("TOP RATED TV SHOWS")
        print("==================================================")
        for data in top_shows_list:
            print()
            print("Rank: {} ".format(data["Rank"]))
            print("Title: {} ".format(data["Name"].strip()))
            print("Rating: {} ".format(data["Rating"].strip()))
            print("\n")
    if option == 3:
        print("==================================================")
        print("POPULAR MOVIES")
        print("==================================================")
        for data in popular_movies_list:
            print()
            print("Rank: {} ".format(data["Rank"].split("(")[0]))
            print("Title: {} ".format(data["Name"].strip()))
            print("Rating: {} ".format(data["Rating"].strip()))
            print("Year: {} ".format(data["Year"].strip()))
            print("\n")
    if option == 4:
        print("==================================================")
        print("POPULAR TV")
        print("==================================================")
        for data in popular_shows_list:
            print()
            print("Rank: {} ".format(data["Rank"].split("(")[0]))
            print("Title: {} ".format(data["Name"].strip()))
            print("Rating: {} ".format(data["Rating"].strip()))
            print("Year: {} ".format(data["Year"].strip()))
            print("\n")

    if option == 5:
        flag = 0
    if option > 5 or option < 1:
        print("Please choose valid option")
