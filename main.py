from fastapi import Depends, FastAPI, Header, HTTPException
from com_sba_api.article.article_api import ArticleApi
from com_sba_api.user.user_api import UserApi
from com_sba_api.item.item_api import ItemApi


app = FastAPI()

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

app.include_router(
    api = UserApi().get_router(),
    prefix='/users',
    tags =['users']
)
app.include_router(
    
)
    