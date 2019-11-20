#coding: utf-8

from BinaryRelation import BinaryRelation


class SameParityBinaryRelation(BinaryRelation):
    """
    A Binary Relation which elements in an ordered pair have the same parity (divisibility by 2).
    """

    def contains_ordered_pair(self, x, y):
        """
        This method returns a boolean value indicating if both elements of a given ordered pair have the same parity.

        Arguments:
        x - The first element of the ordered pair.
        y - The second element of the ordered pair.

        Return True if the ordered pair belongs to the binary relation, otherwise, return False.
        """
        if x%2==0 and y%2==0:
            return True
        elif x%2!=0 and y%2!=0:
            return True
        else:
            return False

    def relation(self, S):
        """
        This method returns a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.

        Arguments:
        S - The input set.

        Return a set of pairs in SxS (a.k.a. S²) that belong to the binary relation.
        """
        S_S=set([(x,y)for x in S for y in S])
        resultado=set()
        for pair in S_S:
            if self.contains_ordered_pair(pair[0],pair[1]):
                resultado.add(pair)
        return resultado
