"""
Migration to add schema column to instances and executions and finish cases model.

Revision ID: c2db9409cb5f
Revises: d1b5be1f0549
Create Date: 2021-05-25 09:37:52.872493

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "c2db9409cb5f"
down_revision = "d1b5be1f0549"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("cases", sa.Column("schema", sa.String(length=256), nullable=True))
    op.add_column(
        "cases",
        sa.Column("solution", postgresql.JSON(astext_type=sa.TEXT()), nullable=True),
    )
    op.add_column(
        "cases", sa.Column("solution_hash", sa.String(length=256), nullable=True)
    )

    op.execute("UPDATE cases SET solution_hash = ''")

    with op.batch_alter_table("cases") as batch_op:
        batch_op.alter_column("solution_hash", nullable=False)

    op.add_column(
        "executions", sa.Column("schema", sa.String(length=256), nullable=True)
    )

    # op.drop_column("executions", "dag_name")
    with op.batch_alter_table("executions") as batch_op:
        batch_op.drop_column("dag_name")

    op.add_column(
        "instances", sa.Column("schema", sa.String(length=256), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("instances", "schema")
    op.add_column(
        "executions", sa.Column("dag_name", sa.VARCHAR(length=256), nullable=True)
    )
    op.drop_column("executions", "schema")
    op.drop_column("cases", "solution_hash")
    op.drop_column("cases", "solution")
    op.drop_column("cases", "schema")
    # ### end Alembic commands ###
