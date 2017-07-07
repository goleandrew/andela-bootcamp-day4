'''binary search module'''
class BinarySearch(list):
    '''BinarySearch class'''

    def __init__(self, lgt, step):


        super(BinarySearch, self).__init__()

        for item in range(1, lgt+1):
            self.append(item * step)

        self.lgt = len(self)

    def search(self, value):
        '''the search function'''
        first_item = 0
        last_item = len(self) - 1
        index_value = 0
        item_found = False

        counter = 0

        if value == self[first_item]:
            index_value = first_item
            item_found = True
        elif value == self[last_item]:
            index_value = last_item
            item_found = True

        if value not in self:
            item_found = True
            index_value = -1

        while first_item <= last_item and not item_found:
            mid_value = (first_item + last_item) // 2
            if self[mid_value] == value:
                item_found = True
                index_value = mid_value
            else:
                counter += 1  
                if value < self[mid_value]:
                    last_item = mid_value - 1
                else:
                    first_item = mid_value + 1

        return {'count': counter, 'index': index_value}
