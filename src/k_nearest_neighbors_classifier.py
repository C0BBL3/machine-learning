class KNearestNeighborsClassifier:
    def __init__(self, k=5):
        self.k = k

    def fit(self, dataframe, dependent_variable):
        self.data_dict = {key: value for key, value in dataframe.data_dict.items(
        ) if key != dependent_variable}
        self.dependent_variable = dataframe.data_dict[dependent_variable]

    def compute_distances(self, observations):
        temp_1 = []
        for i, distance in enumerate(self.dependent_variable):
            temp_2 = 0
            for portion in self.data_dict.keys():
                temp_2 += (self.data_dict[portion][i] - observations[portion]) ** 2
            temp_1.append([temp_2 ** 0.5, distance])
        return temp_1
        #return [[sum([(self.data_dict[portion][i] - observations[portion]) ** 2 for portion in self.data_dict.keys()]) ** 0.5, distance] for i, distance in enumerate(self.dependent_variable)]

    def nearest_neighbors(self, observations):
        return self.simple_sort(self.compute_distances(observations))

    def compute_average_distances(self, observations):
        distances = self.compute_distances(observations)
        average_distances = {}
        while len(distances) > 0:
            current_distances = [
                distance for distance in distances if distances[0][1] == distance[1]]
            average_distances[distances[0][1]] = (
                sum([distance[0] for distance in current_distances]) / len(current_distances))
            distances = [
                distance for distance in distances if distance not in current_distances]
        return average_distances

    def classify(self, observations,i):
        print(self.nearest_neighbors(observations)[:5])
        k_nearest_neighbors = [neighbor[1]
                               for neighbor in self.nearest_neighbors(observations)[:self.k]]
        count_of_types = dict.fromkeys(k_nearest_neighbors, 0)
        average_distances = self.compute_average_distances(observations)
        for neighbor in k_nearest_neighbors:
            count_of_types[neighbor] += 1
        classification = [None, 0]
        for _type_, count in count_of_types.items():
            if count > classification[1]:
                classification = [_type_, count]
            elif count == classification[1] and classification[1] > 0:
                if average_distances[_type_] < average_distances[classification[0]]:
                    classification = [_type_, count]

        return classification[0]

    def simple_sort(self, distances):
        sorted_list, copy_list = [], [i for i in distances]
        while len(copy_list) > 0:
            sorted_list.append(self.min_distance(copy_list))
            copy_list.remove(self.min_distance(copy_list))
        return sorted_list

    def min_distance(self, distances):
        min_distance = distances[0]
        for distance in distances[1:]:
            if distance < min_distance:
                min_distance = distance
        return min_distance
