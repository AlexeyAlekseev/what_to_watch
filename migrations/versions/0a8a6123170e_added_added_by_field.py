"""added added_by field

Revision ID: 0a8a6123170e
Revises: 
Create Date: 2024-10-22 16:42:35.791962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a8a6123170e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('opinion', schema=None) as batch_op:
        batch_op.add_column(sa.Column('added_by', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('opinion', schema=None) as batch_op:
        batch_op.drop_column('added_by')

    # ### end Alembic commands ###
