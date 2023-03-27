"""update table

Revision ID: 5a8c41bf259f
Revises: 30db56df819a
Create Date: 2023-03-27 18:10:19.996424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a8c41bf259f'
down_revision = '30db56df819a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('courses', 'teacher')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('teacher', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###