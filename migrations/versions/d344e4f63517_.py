"""empty message

Revision ID: d344e4f63517
Revises: da7efabaf0d3
Create Date: 2018-05-05 15:02:45.535615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd344e4f63517'
down_revision = 'da7efabaf0d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('memoes', sa.Column('time', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('memoes', 'time')
    # ### end Alembic commands ###
