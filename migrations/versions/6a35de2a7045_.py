"""empty message

Revision ID: 6a35de2a7045
Revises: 64f4b809a456
Create Date: 2022-11-07 11:40:03.168592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a35de2a7045'
down_revision = '64f4b809a456'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cyclist',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('bike', sa.Column('cyclist_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'bike', 'cyclist', ['cyclist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bike', type_='foreignkey')
    op.drop_column('bike', 'cyclist_id')
    op.drop_table('cyclist')
    # ### end Alembic commands ###
