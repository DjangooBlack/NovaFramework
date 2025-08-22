from django.urls import path

urlpatterns = [
    path("v1/", GraphQLView.as_view(graphiql=True), name="graphql_v1"),
]