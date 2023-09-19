from hello import app

def test_add():
    with app.test_client() as client:
        response = client.get('add/4/2')
        assert response.get_data(as_text=True) == '6'

def test_sub():
    with app.test_client() as client:
        response = client.get('sub/4/2')
        assert response.get_data(as_text=True) == '2'

def test_mul():
    with app.test_client() as client:
        response = client.get('mul/4/2')
        assert response.get_data(as_text=True) == '8'