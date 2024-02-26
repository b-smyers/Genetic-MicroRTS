
building_types = ["Base", "Barrack"]
unit_types = ["Worker", "Light", "Ranged", "Heavy"]

negation = ["", "!"]

target_players = ["Enemy", "Ally"]

policies = ["closest", "farthest", "lessHealthy", "mostHealthy", "strongest", "weakest", "random"]

directions = ["Up", "Down", "Left", "Right"]

quantities = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]

map_width = 16
map_height = 16

x_cords = [str(num) for num in range(map_width)]
y_cords = [str(num) for num in range(map_height)]

action_dir      = "./LasiFunctions/ActionFunctions"
for_action_dir  = "./LasiFunctions/ForActionFunctions"
boolean_dir     = "./LasiFunctions/BooleanFunctions"
for_boolean_dir = "./LasiFunctions/ForBooleanFunctions"

# action functions
def build_functions(file, extra_params=""):
    for t in building_types:
        for q in quantities:
            for d in directions:
                file.write(f'build({t},{q},{d}{extra_params})\n')

def train_functions(file, extra_params=""):
    for t in unit_types:
        for q in quantities:
            for d in directions:
                file.write(f'train({t},{q},{d}{extra_params})\n')

def harvest_functions(file, extra_params=""):
    for q in quantities:
        file.write(f'harvest({q}{extra_params})\n')

def attack_functions(file, extra_params=""):
    for t in unit_types:
        for p in policies:
            file.write(f'attack({t},{p}{extra_params})\n')

def moveaway_functions(file, extra_params=""):
    for t in unit_types:
        file.write(f'moveaway({t}{extra_params})\n')

def moveToUnit_functions(file, extra_params=""):
    for t in unit_types:
        for tp in target_players:
            for p in policies:
                file.write(f'moveToUnit({t},{tp},{p}{extra_params})\n')

def moveToCoord_functions(file, extra_params=""):
    for t in unit_types:
        for x in x_cords:
            for y in y_cords:
                file.write(f'moveToCoord({t},{x},{y}{extra_params})\n')

def moveOnceToCoord_functions(file, extra_params=""):
    for t in unit_types:
        for q in quantities:
            for x in x_cords:
                for y in y_cords:
                    file.write(f'moveOnceToCoord({t},{q},{x},{y}{extra_params})\n')

# boolean functions
def HaveQtdUnitsbyType(file):
    for n in negation:
        for t in unit_types:
            for q in quantities:
                file.write(f'{n}HaveQtdUnitsbyType({t},{q})\n')

def HaveQtdUnitsHarversting(file):
    for n in negation:
        for q in quantities:
            file.write(f'{n}HaveQtdUnitsHarversting({q})\n')

def HaveUnitsStrongest(file, extra_params=""):
    for n in negation:
        for t in unit_types:
            file.write(f'{n}HaveUnitsStrongest({t}{extra_params})\n')

def HaveUnitsinEnemyRange(file, extra_params=""):
    for n in negation:
        for t in unit_types:
            file.write(f'{n}HaveUnitsinEnemyRange({t}{extra_params})\n')

def HaveUnitsToDistantToEnemy(file, extra_params=""):
    for n in negation:
        for t in unit_types:
            for q in quantities:
                file.write(f'{n}HaveUnitsToDistantToEnemy({t},{q}{extra_params})\n')

def HaveQtdUnitsAttacking(file):
    for n in negation:
        for t in unit_types:
            for q in quantities:
                file.write(f'{n}HaveQtdUnitsAttacking({t},{q})\n')

def IsPlayerInPosition(file):
    for n in negation:
        for d in directions:
            file.write(f'{n}IsPlayerInPosition({d})\n')

def HaveQtdEnemiesbyType(file):
    for n in negation:
        for t in unit_types:
            for q in quantities:
                file.write(f'{n}HaveQtdEnemiesbyType({t},{q})\n')

def HaveEnemiesStrongest(file, extra_params=""):
    for n in negation:
        for t in unit_types:
            file.write(f'{n}HaveEnemiesStrongest({t}{extra_params})\n')

def HaveEnemiesinUnitsRange(file, extra_params=""):
    for n in negation:
        for t in unit_types:
            file.write(f'{n}HaveEnemiesinUnitsRange({t}{extra_params})\n')

def main():
    # action functions
    build_func_file = open(action_dir + "/BuildFunctions.txt", "w")
    build_functions(build_func_file)
    build_func_file.close()

    train_func_file = open(action_dir + "/TrainFunctions.txt", "w")
    train_functions(train_func_file)
    train_func_file.close()

    harvest_func_file = open(action_dir + "/HarvestFunctions.txt", "w")
    harvest_functions(harvest_func_file)
    harvest_func_file.close()

    attack_func_file = open(action_dir + "/AttackFunctions.txt", "w")
    attack_functions(attack_func_file)
    attack_func_file.close()

    moveaway_func_file = open(action_dir + "/MoveawayFunctions.txt", "w")
    moveaway_functions(moveaway_func_file)
    moveaway_func_file.close()

    move_to_unit_func_file = open(action_dir + "/MoveToUnitFunctions.txt", "w")
    moveToUnit_functions(move_to_unit_func_file)
    move_to_unit_func_file.close()

    move_to_coord_file = open(action_dir + "/MoveToCoordFunctions.txt", "w")
    moveToCoord_functions(move_to_coord_file)
    move_to_coord_file.close()

    move_once_to_coord_func_file = open(action_dir + "/MoveOnceToCoordFunctions.txt", "w")
    moveOnceToCoord_functions(move_once_to_coord_func_file)
    move_once_to_coord_func_file.close()

    # action functions (for loop versions)
    for_build_func_file = open(for_action_dir +"/ForBuildFunctions.txt", "w")
    build_functions(for_build_func_file, ",u")
    for_build_func_file.close()

    for_train_func_file = open(for_action_dir +"/ForTrainFunctions.txt", "w")
    train_functions(for_train_func_file, ",u")
    for_train_func_file.close()

    for_harvest_func_file = open(for_action_dir +"/ForHarvestFunctions.txt", "w")
    harvest_functions(for_harvest_func_file, ",u")
    for_harvest_func_file.close()

    for_attack_func_file = open(for_action_dir +"/ForAttackFunctions.txt", "w")
    attack_functions(for_attack_func_file, ",u")
    for_attack_func_file.close()

    for_moveaway_func_file = open(for_action_dir +"/ForMoveawayFunctions.txt", "w")
    moveaway_functions(for_moveaway_func_file, ",u")
    for_moveaway_func_file.close()

    for_move_to_unit_func_file = open(for_action_dir +"/ForMoveToUnitFunctions.txt", "w")
    moveToUnit_functions(for_move_to_unit_func_file, ",u")
    for_move_to_unit_func_file.close()

    for_move_to_coord_func_file = open(for_action_dir +"/ForMoveToCoordFunctions.txt", "w")
    moveToCoord_functions(for_move_to_coord_func_file, ",u")
    for_move_to_coord_func_file.close()

    for_move_once_to_coord = open(for_action_dir +"/ForMoveOnceToCoordFunctions.txt", "w")
    moveOnceToCoord_functions(for_move_once_to_coord, ",u")
    for_move_once_to_coord.close()


    # boolean functions
    #   ally
    has_number_of_units_func_file = open(boolean_dir + "/HaveQtdUnitsbyTypeFunctions.txt", "w")
    HaveQtdUnitsbyType(has_number_of_units_func_file)
    has_number_of_units_func_file.close()

    has_number_of_workers_harvesting_func_file = open(boolean_dir + "/HaveQtdUnitsHarverstingFunctions.txt", "w")
    HaveQtdUnitsHarversting(has_number_of_workers_harvesting_func_file)
    has_number_of_workers_harvesting_func_file.close()

    has_unit_that_kills_in_one_attack_func_file = open(boolean_dir + "/HaveUnitsStrongestFunctions.txt", "w")
    HaveUnitsStrongest(has_unit_that_kills_in_one_attack_func_file)
    has_unit_that_kills_in_one_attack_func_file.close()

    has_unit_in_opponent_range_func_file = open(boolean_dir + "/HaveUnitsinEnemyRangeFunctions.txt", "w")
    HaveUnitsinEnemyRange(has_unit_in_opponent_range_func_file)
    has_unit_in_opponent_range_func_file.close()

    has_unit_within_distance_from_opponent_func_file = open(boolean_dir + "/HaveUnitsToDistantToEnemyFunctions.txt", "w")
    HaveUnitsToDistantToEnemy(has_unit_within_distance_from_opponent_func_file)
    has_unit_within_distance_from_opponent_func_file.close()

    have_qtd_units_attacking_func_file = open(boolean_dir + "/HaveQtdUnitsAttackingFunctions.txt", "w")
    HaveQtdUnitsAttacking(have_qtd_units_attacking_func_file)
    have_qtd_units_attacking_func_file.close()

    is_player_base_in_position_func_file = open(boolean_dir + "/IsPlayerInPositionFunctions.txt", "w")
    IsPlayerInPosition(is_player_base_in_position_func_file)
    is_player_base_in_position_func_file.close()

    #   enemy
    opponent_has_number_of_units_func_file = open(boolean_dir + "/HaveQtdEnemiesbyTypeFunctions.txt", "w")
    HaveQtdEnemiesbyType(opponent_has_number_of_units_func_file)
    opponent_has_number_of_units_func_file.close()

    opponent_has_units_that_kills_unit_in_one_attack_func_file = open(boolean_dir + "/HaveEnemiesStrongestFunctions.txt", "w")
    HaveEnemiesStrongest(opponent_has_units_that_kills_unit_in_one_attack_func_file)
    opponent_has_units_that_kills_unit_in_one_attack_func_file.close()

    opponent_has_unit_in_player_range_func_file = open(boolean_dir + "/HaveEnemiesinUnitsRangeFunctions.txt", "w")
    HaveEnemiesinUnitsRange(opponent_has_unit_in_player_range_func_file)
    opponent_has_unit_in_player_range_func_file.close()

    # boolean functions (for loop versions)
    #   ally
    for_has_number_of_units_func_file = open(for_boolean_dir + "/ForHaveQtdUnitsbyTypeFunctions.txt", "w")
    HaveQtdUnitsbyType(for_has_number_of_units_func_file)
    for_has_number_of_units_func_file.close()

    for_has_number_of_workers_harvesting_func_file = open(for_boolean_dir + "/ForHaveQtdUnitsHarverstingFunctions.txt", "w")
    HaveQtdUnitsHarversting(for_has_number_of_workers_harvesting_func_file)
    for_has_number_of_workers_harvesting_func_file.close()

    for_has_unit_that_kills_in_one_attack_func_file = open(for_boolean_dir + "/ForHaveUnitsStrongestFunctions.txt", "w")
    HaveUnitsStrongest(for_has_unit_that_kills_in_one_attack_func_file, ",u")
    for_has_unit_that_kills_in_one_attack_func_file.close()

    for_has_unit_in_opponent_range_func_file = open(for_boolean_dir + "/ForHaveUnitsinEnemyRangeFunctions.txt", "w")
    HaveUnitsinEnemyRange(for_has_unit_in_opponent_range_func_file, ",u")
    for_has_unit_in_opponent_range_func_file.close()

    for_has_unit_within_distance_from_opponent_func_file = open(for_boolean_dir + "/ForHaveUnitsToDistantToEnemyFunctions.txt", "w")
    HaveUnitsToDistantToEnemy(for_has_unit_within_distance_from_opponent_func_file, ",u")
    for_has_unit_within_distance_from_opponent_func_file.close()

    for_have_qtd_units_attacking_func_file = open(for_boolean_dir + "/ForHaveQtdUnitsAttackingFunctions.txt", "w")
    HaveQtdUnitsAttacking(for_have_qtd_units_attacking_func_file)
    for_have_qtd_units_attacking_func_file.close()

    for_is_player_base_in_position_func_file = open(for_boolean_dir + "/ForIsPlayerInPositionFunctions.txt", "w")
    IsPlayerInPosition(for_is_player_base_in_position_func_file)
    for_is_player_base_in_position_func_file.close()

    #   enemy
    for_opponent_has_number_of_units_func_file = open(for_boolean_dir + "/ForHaveQtdEnemiesbyTypeFunctions.txt", "w")
    HaveQtdEnemiesbyType(for_opponent_has_number_of_units_func_file)
    for_opponent_has_number_of_units_func_file.close()

    for_opponent_has_units_that_kills_unit_in_one_attack_func_file = open(for_boolean_dir + "/ForHaveEnemiesStrongestFunctions.txt", "w")
    HaveEnemiesStrongest(for_opponent_has_units_that_kills_unit_in_one_attack_func_file, ",u")
    for_opponent_has_units_that_kills_unit_in_one_attack_func_file.close()

    for_opponent_has_unit_in_player_range_func_file = open(for_boolean_dir + "/ForHaveEnemiesinUnitsRangeFunctions.txt", "w")
    HaveEnemiesinUnitsRange(for_opponent_has_unit_in_player_range_func_file, ",u")
    for_opponent_has_unit_in_player_range_func_file.close()

   


if __name__ == "__main__":
    main()