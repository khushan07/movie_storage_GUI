import tkinter as tk
from tkinter import messagebox
movies = []

def add_movie():
    movie = {'name': name_entry.get(), 'director': director_entry.get(), 'year': year_entry.get()}
    movies.append(movie)
    messagebox.showinfo("Added", "Movie added!")
    name_entry.delete(0, tk.END); director_entry.delete(0, tk.END); year_entry.delete(0, tk.END)

def view_movies():
    view_window = tk.Toplevel(root)
    for movie in movies:
        tk.Label(view_window, text=f"{movie['name']} by {movie['director']} ({movie['year']})").pack()

def find_movies():
    attr, val = attribute_entry.get(), value_entry.get()
    find_window = tk.Toplevel(root)
    for movie in movies:
        if movie.get(attr) == val:
            tk.Label(find_window, text=f"{movie['name']} by {movie['director']} ({movie['year']})").pack()

root = tk.Tk(); root.title("Movie Storage")
tk.Label(root, text="Add a Movie").pack()
name_entry, director_entry, year_entry = tk.Entry(root), tk.Entry(root), tk.Entry(root)
for entry, text in zip([name_entry, director_entry, year_entry], ["Name", "Director", "Year"]):
    tk.Label(root, text=text).pack(); entry.pack()
tk.Button(root, text="Add Movie", command=add_movie).pack()
tk.Button(root, text="View All Movies", command=view_movies).pack()
tk.Label(root, text="Find Movies").pack()
attribute_entry, value_entry = tk.Entry(root), tk.Entry(root)
for entry, text in zip([attribute_entry, value_entry], ["Attribute", "Value"]):
    tk.Label(root, text=text).pack(); entry.pack()
tk.Button(root, text="Find Movies", command=find_movies).pack()

root.mainloop()
