import psycopg2
from typing import List
import uvicorn
from fastapi import FastAPI,status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Book(BaseModel):
    id:int=None
    volume_id:str
    title:str
    author:str=None
    thumbnail:str=None
    state:int
    rating:int=None


app=FastAPI(debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/books",response_model=List[Book],status_code=status.HTTP_200_OK)
async def get_book():
    #connect to our database
    conn = psycopg2.connect(
        database="my_db2",user="root",password="nishant@123",host="localhost" ,port=5432
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM book ORDER BY id DESC")
    rows=cur.fetchall()

    formatted_book=[]
    for row in rows:
        formatted_book.append(
            Book(
                id=row[0],
                volume_id=row[1],
                title=row[2],
                author=row[3],
                thumbnail=row[4],
                state=row[5],
                rating=row[6],
            )
        )
    cur.close()
    conn.close()

    return formatted_book

@app.post("/books",status_code=status.HTTP_201_CREATED)
async def new_book(book:Book):
    # connect to our database
    conn = psycopg2.connect(
        database="my_db2", user="root", password="nishant@123", host="localhost", port=5432
    )
    cur = conn.cursor()
    cur.execute(
        f"INSERT  INTO book (volume_id,title,author, thumbnail,state) Values ('{book.volume_id}','{book.title}','{book.author}','{book.thumbnail}','{book.state}')"
    )
    cur.close()
    conn.commit()
    conn.close()
    return 

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
