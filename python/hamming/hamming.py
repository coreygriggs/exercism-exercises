def distance(strand_one, strand_two):
    return len(strand_one) - len([partial for index, partial in enumerate(strand_one) if partial == strand_two[index]])
