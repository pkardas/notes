from sqlmodel import select

from src.model import OrderLine


def test_order_line_mapper_can_load_lines(session):
    session.execute(
        "INSERT INTO orderline (order_id, sku, quantity) VALUES "
        '("order1", "RED-CHAIR", 12),'
        '("order1", "RED-TABLE", 13),'
        '("order2", "BLUE-LIPSTICK", 14)'
    )
    assert session.exec(select(OrderLine)).all() == [
        OrderLine(id=1, order_id="order1", sku="RED-CHAIR", quantity=12),
        OrderLine(id=2, order_id="order1", sku="RED-TABLE", quantity=13),
        OrderLine(id=3, order_id="order2", sku="BLUE-LIPSTICK", quantity=14),
    ]


def test_order_line_mapper_can_save_lines(session):
    new_line = OrderLine(order_id="order1", sku="DECORATIVE-WIDGET", quantity=12)
    session.add(new_line)
    session.commit()
    assert list(session.execute('SELECT order_id, sku, quantity FROM "orderline"')) == [("order1", "DECORATIVE-WIDGET", 12)]
