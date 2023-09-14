"""v5

Revision ID: fd93389c3c36
Revises: 513c81bc28ec
Create Date: 2023-09-14 21:38:38.902997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd93389c3c36'
down_revision = '513c81bc28ec'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('role', sa.Integer(), nullable=False, server_default='1'),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('phone', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'patients',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('message', sa.String(), nullable=True),
        sa.Column('fall_detection', sa.Boolean(), nullable=True),
        sa.Column('urine_detection', sa.Boolean(), nullable=True),
        sa.Column('ecg', sa.String(), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    pass
