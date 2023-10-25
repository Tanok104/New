from .pages.product_page import PageObject


def test_guest_can_add_product_to_cart(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link)
    page.open()
    page.add_to_card()
    page.solve_quiz_and_get_code()
    page.should_be_thing_in_basket(page.get_name())
    page.should_be_the_same_prise(page.return_prise())



