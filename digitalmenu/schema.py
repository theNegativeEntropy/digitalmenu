import graphene
import graphql_jwt

import shops.schema
import users.schema

class Query(shops.schema.Query,
            users.schema.Query,
            graphene.ObjectType
            ):
    pass


class Mutation(shops.schema.Mutation,
               users.schema.Mutation,
               graphene.ObjectType
               ):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    #delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
