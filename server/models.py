from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    @validates('name','phone_number')
    def author_validation(self, key, address):
        if key == 'name':
            if len(address) ==0:
                raise ValueError('Author Name must not be empty ')
            
        elif key == 'phone_number':
             if len(address) !=10:
                raise ValueError('Author phone_number  must be 10 digts ')
                 
                 



    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    @validates('title','content','category')
    def post_validation(self, key, address):
    
            
        if key == 'content':
             if len(address) < 250:
                raise ValueError('Content too short test. Less than 250 chars.')
                
      
             
        elif key == 'category':
            if address not in ['Fiction' , 'Non-Fiction']:
                raise ValueError('category has to be Fiction or Non-Fiction')
                
        return address
    

    @validates('summary')
    def validate_summary(self, key, value):
        if len(value) > 250:
            raise ValueError('Post summary cannot exceed 250 characters')
        return value


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
