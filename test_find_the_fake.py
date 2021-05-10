import react_app_page


def test_find_the_fake_01():
    driver = react_app_page.open_page()

    # Weigh bars 0, 1, 2 vs 3, 4, 5
    list_of_boxes_and_bars = [(0, 0), (1, 1), (2, 2)]
    react_app_page.fill_bowl(driver, react_app_page.LEFT, list_of_boxes_and_bars)

    list_of_boxes_and_bars = [(0, 3), (1, 4), (2, 5)]
    react_app_page.fill_bowl(driver, react_app_page.RIGHT, list_of_boxes_and_bars)

    react_app_page.click_weigh_button(driver)

    # Decide which group the fake is in and weigh two of that group
    measure_results = react_app_page.get_measure_results(driver)

    react_app_page.click_reset_button(driver)

    identified_as_fake = -1

    if measure_results == "<":  # The fake is in 0, 1, 2
        box_number = 0
        bar_number = 0
        react_app_page.fill_cell_in_grid_box(
            driver, react_app_page.LEFT, box_number, bar_number
        )

        bar_number = 1
        react_app_page.fill_cell_in_grid_box(
            driver, react_app_page.RIGHT, box_number, bar_number
        )

        react_app_page.click_weigh_button(driver)

        measure_results = react_app_page.get_measure_results(driver)

        if measure_results == "<":  # The fake is 0
            identified_as_fake = 0

        elif measure_results == ">":  # The fake is 1
            identified_as_fake = 1

        elif measure_results == "=":  # The fake is 2
            identified_as_fake = 2

    elif measure_results == ">":  # The fake is in 3, 4, 5
        box_number = 0
        bar_number = 3
        react_app_page.fill_cell_in_grid_box(
            driver, react_app_page.LEFT, box_number, bar_number
        )

        bar_number = 4
        react_app_page.fill_cell_in_grid_box(
            driver, react_app_page.RIGHT, box_number, bar_number
        )

        react_app_page.click_weigh_button(driver)

        measure_results = react_app_page.get_measure_results(driver)

        if measure_results == "<":  # The fake is 3
            identified_as_fake = 3

        elif measure_results == ">":  # The fake is 4
            identified_as_fake = 4

        elif measure_results == "=":  # The fake is 5
            identified_as_fake = 5

    elif measure_results == "=":  # The fake is in 6, 7, 8
        box_number = 0
        bar_number = 6
        react_app_page.fill_cell_in_grid_box(
            driver, react_app_page.LEFT, box_number, bar_number
        )

        bar_number = 7
        react_app_page.fill_cell_in_grid_box(
            driver, react_app_page.RIGHT, box_number, bar_number
        )

        react_app_page.click_weigh_button(driver)

        measure_results = react_app_page.get_measure_results(driver)
        if measure_results == "<":  # The fake is 6
            identified_as_fake = 6

        elif measure_results == ">":  # The fake is 7
            identified_as_fake = 7

        elif measure_results == "=":  # The fake is 8
            identified_as_fake = 8

    # Verify that the test has identified a fake bar
    assert identified_as_fake >= 0

    # Click the fake bar and verify the alert
    allert_message = react_app_page.click_gold_bar_number_and_get_message(
        driver, identified_as_fake
    )

    assert react_app_page.verify_alert_message(
        True, allert_message
    ), "Alert was {} expected {}".format(
        allert_message, react_app_page.ALLERT_MESSAGE_RIGHT
    )

    # Output
    # Alert message
    # Number of weighings
    # List of weighings
