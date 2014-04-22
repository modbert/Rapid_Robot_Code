from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='')

@app.route('/detail/')
@app.route('/detail/<id>')
def detail(id=None, name=None):
    if id == '123':
        return render_template('detail.html', name='Chicken Parmesan', id='123')
    elif id == '456':
        return render_template('detail.html', name='Eggplant Parmesan', id='456')
    else:
        return render_template('detail.html', name=None, id=None)

@app.route('/save/')
@app.route('/save/<id>')
def save(id=None, name=None, success=False):
    if id == '123':
        return render_template('save.html', name='Chicken Parmesan', success=True, id='123')
    elif id == '456':
        return render_template('save.html', name='Eggplant Parmesan', success=False, id='456')
    else:
        return render_template('save.html', name=None)

@app.route('/search', methods=['GET'])
def find():
    recipes = ['Chicken Parmesan', 'Eggplant Parmesan', 'Spaghetti and Meatballs', 'Tomato Soup', 'Grilled Cheese', 'Peanut Butter & Jelly Sandwich']
    count = request.args.get('n')
    if count:
        count = int(count)
    query = request.args.get('query')
    if query == None:
        pass

    elif query == 'Parmesan' or query == 'parmesan':
        recipes = ['Chicken Parmesan', 'Eggplant Parmesan']

    newRecipes = []

    if count > len(recipes):
        count = len(recipes)

    if (not count == None):
        for i in range(count):
            newRecipes.append(recipes[i])
    else:
        newRecipes = recipes


    return render_template('search.html', list=newRecipes)


if __name__ == '__main__':
    app.run(debug=True)