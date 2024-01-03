"""recreate date sort index

Revision ID: 4ab856aa1a08
Revises: de5bb7dd36db
Create Date: 2024-01-02 14:09:58.205490

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '4ab856aa1a08'
down_revision: Union[str, None] = 'de5bb7dd36db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.create_index('entry_sort_ts', [sa.text('sort_date DESC')], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entries', schema=None) as batch_op:
        batch_op.drop_index('entry_sort_ts')

    # ### end Alembic commands ###