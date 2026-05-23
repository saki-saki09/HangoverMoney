from utils.storage import load_data


def filter_expenses(
    search_text="",
    category=None
):
    """
    Filter expenses by search and category.
    """

    data = load_data()

    filtered = []

    for expense in data:

        matches_search = True

        matches_category = True

        # Search check
        if search_text:

            search_text = search_text.lower()

            matches_search = (
                search_text in
                expense["note"].lower()
            )

        # Category check
        if category and category != "All":

            matches_category = (
                expense["category"] == category
            )

        if matches_search and matches_category:

            filtered.append(expense)

    return filtered