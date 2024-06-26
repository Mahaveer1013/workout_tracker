"""Initial migration

Revision ID: 000f4bdb099f
Revises: 
Create Date: 2024-05-01 14:43:39.067201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '000f4bdb099f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('email', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('password', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('date', sa.DateTime(timezone=True), nullable=True))
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.create_unique_constraint(None, ['email'])

    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DateTime(timezone=True), nullable=True))
        batch_op.add_column(sa.Column('username', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('workout_data', sa.JSON(), nullable=True))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('workout_data')
        batch_op.drop_column('username')
        batch_op.drop_column('date')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('date')
        batch_op.drop_column('password')
        batch_op.drop_column('email')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
