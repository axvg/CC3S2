import json
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import db, app
from models.account import Account, DataValidationError
from datetime import date

ACCOUNT_DATA = {}

# fix para evitar error de context :  Working outside of application context.
@pytest.fixture(scope="module", autouse=True)
def app_context():
    with app.app_context():
        yield

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Configura la base de datos antes y después de todas las pruebas"""
    # Se ejecuta antes de todas las pruebas
    db.create_all()
    yield
    # Se ejecuta después de todas las pruebas
    db.session.close()

class TestAccountModel:
    """Modelo de Pruebas de Cuenta"""

    @classmethod
    def setup_class(cls):
        """Conectar y cargar los datos necesarios para las pruebas"""
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)
        for record in ACCOUNT_DATA:
            record["date_joined"] = date.today()
        print(f"ACCOUNT_DATA cargado: {ACCOUNT_DATA}")

    @classmethod
    def teardown_class(cls):
        """Desconectar de la base de datos"""
        pass  # Agrega cualquier acción de limpieza si es necesario

    def setup_method(self):
        """Truncar las tablas antes de cada prueba"""
        db.session.query(Account).delete()
        db.session.commit()

    def teardown_method(self):
        """Eliminar la sesión después de cada prueba"""
        db.session.remove()

    ######################################################################
    #  Casos de prueba
    ######################################################################

    def test_create_an_account(self):
        """Probar la creación de una sola cuenta"""
        data = ACCOUNT_DATA[0]  # obtener la primera cuenta
        account = Account(**data)
        account.create()
        assert len(Account.all()) == 1

    def test_create_all_accounts(self):
        """Probar la creación de múltiples cuentas"""
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        assert len(Account.all()) == len(ACCOUNT_DATA)

    def test_repr(self):
        data = ACCOUNT_DATA[0]
        account = Account(**data)
        assert repr(account) == f"<Account {repr(data['name'])}>"

    def test_to_dict(self):
        data = ACCOUNT_DATA[0]
        account = Account(**data)
        account.create()
        result = account.to_dict()

        expected_cols = ['id', 'name', 'email', 'phone_number', 'disabled', 'date_joined']
        for key in expected_cols:
            assert key in result

        assert result['name'] == data['name']
        assert result['email'] == data['email']
        assert result['phone_number'] == data.get('phone_number')
        assert result['disabled'] == data.get('disabled', False)

    def test_from_dict(self):
        account = Account()
        data = ACCOUNT_DATA[0]
        account.from_dict(data)

        assert account.name == data['name']
        assert account.email == data['email']
        assert account.phone_number == data.get('phone_number')
        assert account.disabled == data.get('disabled', False)

    def test_create_generates_id(self):
        data = ACCOUNT_DATA[0]
        account = Account(**data)
        assert account.id is None

        account.create()
        assert account.id is not None
        assert isinstance(account.id, int)

    def test_update_success(self):
        data = ACCOUNT_DATA[0]
        account = Account(**data)
        account.create()

        original_id = account.id
        account.name = "nombre2"
        account.email = "mail2@mail.com"

        account.update()

        updated_account = Account.find(original_id)
        assert updated_account.name == "nombre2"
        assert updated_account.email == "mail2@mail.com"

    def test_update_without_id_raises_error(self):
        data = ACCOUNT_DATA[0]
        account = Account(**data)
        with pytest.raises(DataValidationError) as err:
            account.update()

        assert "update sin un ID" in str(err.value)

    def test_delete(self):
        data = ACCOUNT_DATA[0]
        account = Account(**data)
        account.create()
        account_id = account.id

        assert Account.find(account_id) is not None

        account.delete()
        assert Account.find(account_id) is None
        assert len(Account.all()) == 0