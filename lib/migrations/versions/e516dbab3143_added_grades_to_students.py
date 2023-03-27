"""added grades to students

Revision ID: e516dbab3143
Revises: 16b1cc8ece0c
Create Date: 2023-03-27 18:44:12.493584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e516dbab3143'
down_revision = '16b1cc8ece0c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('grade', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'grade')
    # ### end Alembic commands ###
