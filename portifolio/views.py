from flask import Blueprint, render_template
# import numpy as np
# import matploatlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap

views = Blueprint('views', __name__)

@views.route('/')
def base():
    return render_template("base.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/experiences')
def experiences():
    return render_template("experiences.html")

@views.route('/education')
def education():
    return render_template("education.html")
# def map():
#     austin = (-97.75, 30.25)
#     hawaii = (-157.8, 21.3)
#     washington = (-77.01, 38.90)
#     chicago = (-87.68, 41.83)
#     losangeles = (-118.25, 34.05)
    
#     m = Basemap(projection='merc', llcrnrlat=10,urcrnrlat=50,llcrnrlon=-160,urcrnrlon=-60)

#     m.drawcoastlines()
#     m.fillcontinents(color='lightgray', lake_color='lightblue')
#     m.drawparallels(np.arange(-90.,91.,30.))
#     m.drawmeridians(np.arange(-180.,181.,60.))
#     m.drawmapboundary(fill_color='aqua')

#     m.drawcountries()

#     x,y = m(*zip(*[hawaii, austin, washington, chicago, losangeles]))

#     m.plot(x,y, marker='o', markersize=6, markerfacecolor='red', linewidth=0)

#     plt.title("Mercator Projection")
#     plt.show()

@views.route('/skills')
def skills():
    return render_template("skills.html")

@views.route('/portifolio')
def portifolio():
    return render_template("portifolio.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")