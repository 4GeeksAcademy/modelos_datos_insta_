"""empty message

Revision ID: 9bb2caa6420b
Revises: 5cd7d931dfc2
Create Date: 2025-07-07 19:20:37.566544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bb2caa6420b'
down_revision = '5cd7d931dfc2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('like', sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(None, ['content'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('like')
        batch_op.drop_column('content')

    # ### end Alembic commands ###
