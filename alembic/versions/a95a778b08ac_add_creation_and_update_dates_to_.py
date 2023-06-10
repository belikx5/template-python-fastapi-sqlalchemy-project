"""add creation and update dates to watchlist table

Revision ID: a95a778b08ac
Revises: 2d3638dd4daf
Create Date: 2023-05-28 22:26:10.090078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a95a778b08ac'
down_revision = '2d3638dd4daf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('watchlist', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('watchlist', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('watchlist', 'updated_at')
    op.drop_column('watchlist', 'created_at')
    # ### end Alembic commands ###