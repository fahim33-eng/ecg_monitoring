"""Test Revision

Revision ID: 97ce4d18a51a
Revises: 35a88f241ba9
Create Date: 2023-10-26 01:56:01.004344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97ce4d18a51a'
down_revision = '35a88f241ba9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'test_table',
        sa.Column('id', sa.Integer(), nullable=False, primary_key = True),
        sa.Column('title', sa.String(), nullable=False),  
    )


def downgrade() -> None:
    op.drop_table('test_table')
