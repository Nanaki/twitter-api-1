"""Add users

Revision ID: 7cd8780ab650
Revises: 1458ecfe1734
Create Date: 2018-11-29 22:49:20.894773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cd8780ab650'
down_revision = '1458ecfe1734'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('api_key', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('tweets', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tweets', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tweets', type_='foreignkey')
    op.drop_column('tweets', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
