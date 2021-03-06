"""empty message

Revision ID: 36ad176f32b1
Revises: 0207ab7d310e
Create Date: 2018-10-09 10:43:24.094852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36ad176f32b1'
down_revision = '0207ab7d310e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rel_table',
    sa.Column('sid', sa.Integer(), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['clas.id'], ),
    sa.ForeignKeyConstraint(['sid'], ['stus.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rel_table')
    op.drop_table('stus')
    op.drop_table('clas')
    # ### end Alembic commands ###
