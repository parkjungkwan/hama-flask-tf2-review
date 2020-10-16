from com_sba_api.item.item_api import ItemApi, ItemsApi
from com_sba_api.user.user_api import UserApi, UsersApi
from com_sba_api.article.article_api import ArticleApi, ArticlesApi

def initialize_routes(api):
    api.add_resource(ItemApi, '/api/item/<string:id>')
    api.add_resource(ItemsApi,'/api/items')
    api.add_resource(UserApi, '/api/user/<string:id>')
    api.add_resource(UserRegister, '/api/user/register')
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(ArticlesApi, '/api/store/<string:name>')