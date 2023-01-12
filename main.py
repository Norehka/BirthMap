import tkinter as tk
from tkinter import messagebox
from kerykeion import KrInstance, MakeSvgInstance


# Function to get input from user
def get_input():
    name = name_entry.get()
    day = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())
    city = city_entry.get()
    country = country_entry.get()
    chart_type = chart_type_var.get()
    person = KrInstance(name, year, month, day, hour, minute, city, country)

    if chart_type == "Transit" or chart_type == "Composite":
        name2 = name_entry2.get()
        day2 = int(day_entry2.get())
        month2 = int(month_entry2.get())
        year2 = int(year_entry2.get())
        hour2 = int(hour_entry2.get())
        minute2 = int(minute_entry2.get())
        city2 = city_entry2.get()
        country2 = country_entry2.get()
        person2 = KrInstance(name2, year2, month2, day2, hour2, minute2, city2, country2)
        svg = MakeSvgInstance(person, chart_type=chart_type, second_obj=person2)
    else:
        svg = MakeSvgInstance(person, chart_type=chart_type)
    svg.makeSVG()
    messagebox.showinfo("Chart generated", f"{chart_type} Chart has been generated successfully")


# Create a Tkinter window
root = tk.Tk()
root.title("Natal Chart Generator")

# Create labels and entry widgets for user input
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

day_label = tk.Label(root, text="Day:")
day_label.grid(row=1, column=0)

day_entry = tk.Entry(root)
day_entry.grid(row=1, column=1)

month_label = tk.Label(root, text="Month:")
month_label.grid(row=2, column=0)

month_entry = tk.Entry(root)
month_entry.grid(row=2, column=1)

year_label = tk.Label(root, text="Year:")
year_label.grid(row=3, column=0)

year_entry = tk.Entry(root)
year_entry.grid(row=3, column=1)

hour_label = tk.Label(root, text="Hour:")
hour_label.grid(row=4, column=0)

hour_entry = tk.Entry(root)
hour_entry.grid(row=4, column=1)

minute_label = tk.Label(root, text="Minute:")
minute_label.grid(row=5, column=0)

minute_entry = tk.Entry(root)
minute_entry.grid(row=5, column=1)

city_label = tk.Label(root, text="City:")
city_label.grid(row=6, column=0)

city_entry = tk.Entry(root)
city_entry.grid(row=6, column=1)

country_label = tk.Label(root, text="Country:")
country_label.grid(row=7, column=0)

country_entry = tk.Entry(root)
country_entry.grid(row=7, column=1)

chart_type_var = tk.StringVar(root)
chart_type_var.set("Natal") # default value
chart_type_label = tk.Label(root, text="Chart Type:")
chart_type_label.grid(row=9, column=0)
chart_type_dropdown = tk.OptionMenu(root, chart_type_var, "Natal", "Composite", "Transit")
chart_type_dropdown.grid(row=9, column=1)

#2nd
# Create new labels and entry widgets for second person's details
name_label2 = tk.Label(root, text="Name:")
name_label2.grid(row=10, column=0)

name_entry2 = tk.Entry(root)
name_entry2.grid(row=10, column=1)

day_label2 = tk.Label(root, text="Day:")
day_label2.grid(row=11, column=0)

day_entry2 = tk.Entry(root)
day_entry2.grid(row=11, column=1)

month_label2 = tk.Label(root, text="Month:")
month_label2.grid(row=12, column=0)

month_entry2 = tk.Entry(root)
month_entry2.grid(row=12, column=1)

year_label2 = tk.Label(root, text="Year:")
year_label2.grid(row=13, column=0)

year_entry2 = tk.Entry(root)
year_entry2.grid(row=13, column=1)

hour_label2 = tk.Label(root, text="Hour:")
hour_label2.grid(row=14, column=0)

hour_entry2 = tk.Entry(root)
hour_entry2.grid(row=14, column=1)

minute_label2 = tk.Label(root, text="Minute:")
minute_label2.grid(row=15, column=0)

minute_entry2 = tk.Entry(root)
minute_entry2.grid(row=15, column=1)

city_label2 = tk.Label(root, text="City:")
city_label2.grid(row=16, column=0)

city_entry2 = tk.Entry(root)
city_entry2.grid(row=16, column=1)

country_label2 = tk.Label(root, text="Country:")
country_label2.grid(row=17, column=0)

country_entry2 = tk.Entry(root)
country_entry2.grid(row=17, column=1)

def chart_type_changed(*args):
    chart_type = chart_type_var.get()
    if chart_type == "Transit" or chart_type == "Composite":
        name_label2.grid()
        name_entry2.grid()
        day_label2.grid()
        day_entry2.grid()
        month_label2.grid()
        month_entry2.grid()
        year_label2.grid()
        year_entry2.grid()
        hour_label2.grid()
        hour_entry2.grid()
        minute_label2.grid()
        minute_entry2.grid()
        city_label2.grid()
        city_entry2.grid()
        country_label2.grid()
        country_entry2.grid()
    else:
        name_label2.grid_remove()
        name_entry2.grid_remove()
        day_label2.grid_remove()
        day_entry2.grid_remove()
        month_label2.grid_remove()
        month_entry2.grid_remove()
        year_label2.grid_remove()
        year_entry2.grid_remove()
        hour_label2.grid_remove()
        hour_entry2.grid_remove()
        minute_label2.grid_remove()
        minute_entry2.grid_remove()
        city_label2.grid_remove()
        city_entry2.grid_remove()
        country_label2.grid_remove()
        country_entry2.grid_remove()
chart_type_var.trace("w", chart_type_changed)



# Create a submit button
submit_button = tk.Button(root, text="Submit", command=get_input)
submit_button.grid(row=8, column=0, columnspan=2)


root.mainloop()
