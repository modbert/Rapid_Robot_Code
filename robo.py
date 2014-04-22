from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='')

@app.route('/detail/')
@app.route('/detail/<id>')
@app.route('/detail/<id>/<param>')
def detail(id=None, name=None, param=1):

    the_name = None
    the_code = None

    if id == '1':
        the_name = 'Straight Line Code'
        pause = int(param) * 2000
        the_code = "\n"\
            +"; Drive forward for "+str(param)+" feet\n"\
            +"forward A\n"\
            +"forward B\n"\
            +"pause " + str(pause)\
            +"\nhalt A \nhalt B"
    elif id == '2':
        pause = int(param) * 2000
        the_name = 'Square Path Code'
        the_code = "\n"\
                +"symbol counter = b1\n"\
                +"    main:\n"\
                +"        ; Set Motor Speed Low\n"\
                +"        output C.5 \n"\
                +"        \n"\
                +"        doStuff:\n"\
                +"        for counter = 1 to 4\n"\
                +"            \n"\
                +"            gosub driveAndTurn\n"\
                +"            \n"\
                +"        next counter\n"\
                +"        \n"\
                +"        end\n"\
                +"\n"\
                +"    driveAndTurn:\n"\
                +"        ; Drive forward\n"\
                +"        forward A\n"\
                +"        forward B\n"\
                +"        pause "+str(pause)+"\n"\
                +"        \n"\
                +"        ; Turn right\n"\
                +"        halt A\n"\
                +"        halt B\n"\
                +"        forward A\n"\
                +"        pause 1000\n"\
                +"        halt A\n"\
                +"\n"\
                +"        return"

    elif id == '3':
        pause = int(param) * 2000
        the_name = 'Hexagon Path Code'
        the_code = "\n"\
                +"symbol counter = b1\n"\
                +"    main:\n"\
                +"        ; Set Motor Speed Low\n"\
                +"        output C.5 \n"\
                +"        \n"\
                +"        doStuff:\n"\
                +"        for counter = 1 to 6\n"\
                +"            \n"\
                +"            gosub driveAndTurn\n"\
                +"            \n"\
                +"        next counter\n"\
                +"        \n"\
                +"        end\n"\
                +"\n"\
                +"    driveAndTurn:\n"\
                +"        ; Drive forward\n"\
                +"        forward A\n"\
                +"        forward B\n"\
                +"        pause "+str(pause)+"\n"\
                +"        \n"\
                +"        ; Turn right\n"\
                +"        halt A\n"\
                +"        halt B\n"\
                +"        forward A\n"\
                +"        pause 750\n"\
                +"        halt A\n"\
                +"\n"\
                +"        return"


    return render_template('detail.html', name=the_name, code=the_code)

@app.route('/search', methods=['GET'])
def find():
    recipes = ['Straight Line Code', 'Square Path Code', 'Dancing Code', 'Hexagon Path Code', 'Indiana Jones']
    count = request.args.get('n')
    if count:
        count = int(count)
    query = request.args.get('query')
    if query == None:
        pass

    elif query == 'Path' or query == 'path':
        recipes = ['Square Path Code', 'Hexagon Path Code']

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