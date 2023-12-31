"""add watchlist table

Revision ID: cc2eae58a560
Revises: 2fb979a2880e
Create Date: 2023-05-25 21:29:28.139345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc2eae58a560'
down_revision = '2fb979a2880e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('watchlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('series_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['series_id'], ['series.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('watchlist')
    # ### end Alembic commands ###
