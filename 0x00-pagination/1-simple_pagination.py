def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        paginate dataset using index and returns empty list when out of range
        """
        self.dataset()
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        startEnd = index_range(page, page_size)
        try:
            return self.__dataset[startEnd[0]: startEnd[1]]
        except IndexError:
            return []
