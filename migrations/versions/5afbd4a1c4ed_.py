"""empty message

Revision ID: 5afbd4a1c4ed
Revises: 
Create Date: 2022-05-24 13:36:04.381724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5afbd4a1c4ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('sci_name', sa.String(length=100), nullable=False),
    sa.Column('size', sa.String(length=50), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('diet', sa.String(length=250), nullable=True),
    sa.Column('habitat', sa.String(length=250), nullable=True),
    sa.Column('lifespan', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.Column('inventory', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('sci_name')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('api_token', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('followers',
    sa.Column('follower_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=255), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('followers')
    op.drop_table('user')
    op.drop_table('animal')
    # ### end Alembic commands ###
