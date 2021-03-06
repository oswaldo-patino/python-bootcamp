"""Initial migration

Revision ID: 3c7106c8417c
Revises: 
Create Date: 2021-12-22 16:32:14.754087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c7106c8417c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column('views', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entry', 'views')
    # ### end Alembic commands ###
