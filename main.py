from website import create_app
#can be imoorted bc <<imoort>> is the websire package


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    
    