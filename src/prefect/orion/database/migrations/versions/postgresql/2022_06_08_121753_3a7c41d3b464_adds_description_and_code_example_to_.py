"""Adds description and code example to block type

Revision ID: 3a7c41d3b464
Revises: 77ebcc9cf355
Create Date: 2022-06-08 12:17:53.241415

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "3a7c41d3b464"
down_revision = "77ebcc9cf355"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("block_type", sa.Column("description", sa.String(), nullable=True))
    op.add_column("block_type", sa.Column("code_example", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("block_type", "code_example")
    op.drop_column("block_type", "description")
    # ### end Alembic commands ###
