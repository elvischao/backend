"""Rename usage

Revision ID: 091ee855e563
Revises: 514f6e1b7a72
Create Date: 2020-11-17 04:21:06.623479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '091ee855e563'
down_revision = '514f6e1b7a72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.add_column(sa.Column('download_usage', sa.Integer(), nullable=True))
        batch_op.drop_column('usage')
    op.execute('UPDATE port set download_usage=0')
    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.alter_column('download_usage', existing_type=sa.Integer(), nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usage', sa.INTEGER(), nullable=False))
        batch_op.drop_column('download_usage')

    # ### end Alembic commands ###