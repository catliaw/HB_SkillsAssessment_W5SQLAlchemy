"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette').filter_by(brand_name="Chevrolet").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year<1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.year > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded==1903).filter(Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = Model.query.options(db.joinedload('brands')).filter(Model.year == year).all()

    for model in model_info:
        print "Model name: ", model.name
        print "Brand name: ", model.brand_name
        print "Headquarters: ", model.brands.headquarters
        print


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands_list = Brand.query.options(db.joinedload('models')).all()

    for brand in brands_list:
        models_list = brand.models

        if models_list:

            print "Brand: ", brand.name
            print "Models: "

            for model in models_list:
                print "\t", model.name

            print "\n"


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# The query returns <flask_sqlalchemy.BaseQuery at 0x7fb84ab07cd0> which is
# basically a Flask SQL query object that is living in memory at 0x7fb84ab07cd0.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# An association table with a table that basically holds the primary keys of two
# different tables and no interesting information. The sole purpose of this
# table is to establish a many to many relationship between the two other tables.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):

    brands_list = Brand.query.filter(Brand.name.like("%"+mystr+"%")).all()


def get_models_between(start_year, end_year):
    
    models_list = Model.query.filter( (Model.year >= start_year) & (Model.year < end_year)).all()