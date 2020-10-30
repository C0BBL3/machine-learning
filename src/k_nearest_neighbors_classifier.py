class KNearestNeighborsClassifier:
    def __init__(self, dataframe, prediction_column):
        self.data_dict = {key: value for key, value in dataframe.data_dict.items(
        ) if key != prediction_column}
        self.prediction_column = dataframe.data_dict[prediction_column]

    def compute_distances(self, observations):
        return [[sum([(self.data_dict[portion][i] - observations[portion]) ** 2 for portion in self.data_dict.keys()]) ** 0.5, distance] for i, distance in enumerate(self.prediction_column)]

    def nearest_neighbors(self, observations):
        return self.quick_sort(self.compute_distances(observations))

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

    def classify(self, observations, k=5):
        k_nearest_neighbors = [neighbor[1]
                               for neighbor in self.nearest_neighbors(observations)[:k]]
        count_of_types = dict.fromkeys(k_nearest_neighbors, 0)
        for neighbor in k_nearest_neighbors:
            count_of_types[neighbor] += 1
        max_count = [None, 0]
        for _type_, count in count_of_types.items():
            if count > max_count[1]:
                max_count = [_type_, count]
            elif count == max_count[1] and max_count[1] > 0:
                return min(
                    self.compute_average_distances(observations).keys(), 
                    key=(lambda k: self.compute_average_distances(observations)[k])
                    )
        return max_count[0]

    def quick_sort(self, distances):
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
