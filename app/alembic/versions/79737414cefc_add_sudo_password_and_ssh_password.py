"""Add sudo password and ssh password

Revision ID: 79737414cefc
Revises: 38be664c28a5
Create Date: 2020-11-15 23:16:17.326127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79737414cefc'
down_revision = '38be664c28a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.drop_constraint('_port_num_server_uc', type_='unique')
        batch_op.create_unique_constraint('_port_num_server_uc', ['external_num', 'server_id'])

    with op.batch_alter_table('server', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ssh_password', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('sudo_password', sa.String(), nullable=True))
        batch_op.create_unique_constraint('_server_ansible_host_ansible_port_uc', ['ansible_host', 'ansible_port'])
        batch_op.create_unique_constraint('_server_ansible_name_uc', ['ansible_name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('server', schema=None) as batch_op:
        batch_op.drop_constraint('_server_ansible_name_uc', type_='unique')
        batch_op.drop_constraint('_server_ansible_host_ansible_port_uc', type_='unique')
        batch_op.drop_column('sudo_password')
        batch_op.drop_column('ssh_password')

    with op.batch_alter_table('port', schema=None) as batch_op:
        batch_op.drop_constraint('_port_num_server_uc', type_='unique')
        batch_op.create_unique_constraint('_port_num_server_uc', ['num', 'server_id'])

    # ### end Alembic commands ###
