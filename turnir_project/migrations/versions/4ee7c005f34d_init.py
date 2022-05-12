"""init

Revision ID: 4ee7c005f34d
Revises: 
Create Date: 2022-05-12 15:52:38.881147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ee7c005f34d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participantsDB',
    sa.Column('participant_id', sa.Integer(), nullable=False),
    sa.Column('participant_first_name', sa.String(), nullable=True),
    sa.Column('participant_last_name', sa.String(), nullable=True),
    sa.Column('activity_status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('participant_id', name=op.f('pk_participantsDB'))
    )
    op.create_table('fightsDB',
    sa.Column('fight_id', sa.Integer(), nullable=False),
    sa.Column('round_number', sa.Integer(), nullable=True),
    sa.Column('red_fighter_id', sa.Integer(), nullable=True),
    sa.Column('blue_fighter_id', sa.Integer(), nullable=True),
    sa.Column('fight_winner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blue_fighter_id'], ['participantsDB.participant_id'], name=op.f('fk_fightsDB_blue_fighter_id_participantsDB')),
    sa.ForeignKeyConstraint(['red_fighter_id'], ['participantsDB.participant_id'], name=op.f('fk_fightsDB_red_fighter_id_participantsDB')),
    sa.PrimaryKeyConstraint('fight_id', name=op.f('pk_fightsDB'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fightsDB')
    op.drop_table('participantsDB')
    # ### end Alembic commands ###
