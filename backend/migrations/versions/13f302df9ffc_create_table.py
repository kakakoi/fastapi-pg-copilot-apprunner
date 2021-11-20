"""create table

Revision ID: 13f302df9ffc
Revises: 
Create Date: 2021-11-20 17:00:08.164286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13f302df9ffc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notes', 'name')
    # ### end Alembic commands ###
