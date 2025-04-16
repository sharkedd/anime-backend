from flask import Flask
from flask_graphql import GraphQLView
from .schemas.schema import schema
app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Habilita interfaz web para probar queries
    )
)

if __name__ == '__main__':
    app.run(debug=True)
