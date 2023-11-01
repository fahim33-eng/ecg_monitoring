"""Delete Test Table

Revision ID: bc3701f3505c
Revises: 97ce4d18a51a
Create Date: 2023-10-26 02:26:06.929073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc3701f3505c'
down_revision = '97ce4d18a51a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table('test_tables_2')


def downgrade() -> None:
    pass
