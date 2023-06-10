"""split watchlist into 2 tables

Revision ID: bf2afe5fd878
Revises: 945ca1c52ce6
Create Date: 2023-05-25 23:12:09.729193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf2afe5fd878'
down_revision = '945ca1c52ce6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('watchlist_series',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('watchlist_id', sa.Integer(), nullable=True),
    sa.Column('series_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['series_id'], ['series.id'], ),
    sa.ForeignKeyConstraint(['watchlist_id'], ['watchlist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('watchlist_series_id_fkey', 'watchlist', type_='foreignkey')
    op.drop_column('watchlist', 'series_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('watchlist', sa.Column('series_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('watchlist_series_id_fkey', 'watchlist', 'series', ['series_id'], ['id'])
    op.drop_table('watchlist_series')
    # ### end Alembic commands ###