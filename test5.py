import random

def random_carriage(coupe_amount = 9):
    """Returns list of coupes in carriage

    Args:
        - coupe (int): for default 9
    
    Returns:
        - (list) all coupes in carriage
    """
    carriage = []
    coupe = {}
    for place in range(1, coupe_amount * 4 + 1):
        coupe[place] = random.choice([None, 'м', 'ж'])
        if len(coupe) == 4:
            carriage.append(coupe)
            coupe = {}
    return carriage

def print_carriage(carriage):
    """Prints carriage

    Args:
        - carriage (str)
    
    Returns:
        - (str) all sits in carriage
    """
    for index, coupe in enumerate(carriage):
        print(index + 1, ':', coupe)

def empty_coupe_list(carriage):
    """Returns all numbers of vacant coupes

    Args:
        - carriage (str)
    
    Returns:
        - (dict) numbers of vacant coupes
    """
    answer = {}
    for index, coupe in enumerate(carriage):
        if not any(coupe.values()):
            answer[index + 1] = coupe
    return answer

def empty_place_list(carriage):
    """Returns all numbers of vacant sits

    Args:
        - carriage (str)
    
    Returns:
        - (list) numbers of vacant sits
    """
    answer = []
    for coupe in carriage:
        for place in coupe:
            if not coupe[place]:
                answer.append(place)
    return answer

def empty_lh_place_list(carriage, low = True):
    """Returns all numbers of vacant low or upper sits

    Args:
        - carriage (str), low (True/False): True for default
    
    Returns:
        - (list) numbers of vacant low or upper sits
    """
    answer = []
    for coupe in carriage:
        for place in coupe:
            if not coupe[place] and place % 2 == int(low):
                answer.append(place)
        return answer

def empty_places_in_gender_coupe(carriage, gender):
    """Returns all numbers of vacant sits for gender

    Args:
        - carriage (str), gender ("ж" or "м")
    
    Returns:
        - (list) numbers of vacant sits for gender
    """
    answer = []
    for coupe in carriage:
        answer1 = []
        for place in coupe:
            if not coupe[place]:
                answer1.append(place)
            elif coupe[place] != gender:
                break
        else:
            if len(answer1) < 4:
                answer += answer1
    return answer

carriage = random_carriage()
print_carriage(carriage)
print('List of full free coupe')
print(empty_coupe_list(carriage))
print('List of free places')
print(*empty_place_list(carriage), sep = ", ")
print('List of free lower places')
print(empty_lh_place_list(carriage))
print('List of free upper places')
print(empty_lh_place_list(carriage, False))
print('List of free places in coupe with only man company')
print(empty_places_in_gender_coupe(carriage, 'м'))
print('List of free places in coupe with only woman company')
print(empty_places_in_gender_coupe(carriage, 'ж'))