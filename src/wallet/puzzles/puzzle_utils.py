from src.util.condition_tools import ConditionOpcode


def make_create_coin_condition(puzzle_hash, amount):
    return [ConditionOpcode.CREATE_COIN, puzzle_hash, amount]


def make_assert_aggsig_condition(pubkey):
    return [ConditionOpcode.AGG_SIG, pubkey]


def make_assert_coin_consumed_condition(coin_name):
    return [ConditionOpcode.ASSERT_COIN_CONSUMED, coin_name]


def make_assert_my_coin_id_condition(coin_name):
    return [ConditionOpcode.ASSERT_MY_COIN_ID, coin_name]


def make_assert_block_index_exceeds_condition(block_index):
    return [ConditionOpcode.ASSERT_BLOCK_INDEX_EXCEEDS, block_index]


def make_assert_block_age_exceeds_condition(block_index):
    return [ConditionOpcode.ASSERT_BLOCK_AGE_EXCEEDS, block_index]


def make_assert_time_exceeds_condition(time):
    return [ConditionOpcode.ASSERT_TIME_EXCEEDS, time]
