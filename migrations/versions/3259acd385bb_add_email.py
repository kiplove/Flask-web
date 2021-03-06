"""add email

Revision ID: 3259acd385bb
Revises: 
Create Date: 2017-03-21 22:11:20.279307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3259acd385bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('phone_num', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'phone_num')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
