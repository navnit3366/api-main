"""add resource_id column

Revision ID: 782ac8fe23c8
Revises: 815ae0983ef1
Create Date: 2022-11-10 13:47:49.486491

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "782ac8fe23c8"
down_revision = "815ae0983ef1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "leaderboards",
        sa.Column("resource_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.create_index(
        op.f("ix_leaderboards_resource_id"),
        "leaderboards",
        ["resource_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_leaderboards_resource_id"), table_name="leaderboards")
    op.drop_column("leaderboards", "resource_id")
    # ### end Alembic commands ###
