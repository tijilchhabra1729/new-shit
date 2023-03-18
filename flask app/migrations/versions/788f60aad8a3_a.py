"""a

Revision ID: 788f60aad8a3
Revises: dd96c164535e
Create Date: 2023-03-16 15:14:00.448388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '788f60aad8a3'
down_revision = 'dd96c164535e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    op.drop_table('price')
    with op.batch_alter_table('sneaker', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('url', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sneaker', schema=None) as batch_op:
        batch_op.drop_column('url')
        batch_op.drop_column('price')

    op.create_table('price',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('price', sa.VARCHAR(), nullable=True),
    sa.Column('snkr', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['snkr'], ['sneaker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('snkr', sa.INTEGER(), nullable=True),
    sa.Column('link', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['snkr'], ['sneaker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
