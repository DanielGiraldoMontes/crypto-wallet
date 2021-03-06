"""empty message

Revision ID: fb9f039ee527
Revises: 3fe06cb64cb4
Create Date: 2020-02-20 22:00:55.874910

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'fb9f039ee527'
down_revision = '3fe06cb64cb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('user_transferred', sa.Integer(), nullable=False),
                    sa.Column('transferred_value', sa.Float(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['crypto_user.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_transferred'], ['crypto_user.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    # ### end Alembic commands ###
