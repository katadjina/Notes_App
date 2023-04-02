from website import create_app
#can be imoorted bc <<imoort>> is the websire package


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    
    # eg.  app.run(host='0.0.0.0', port=8080)
    # will run the Flask server on all available network interfaces and on port 8080
    
    