#### Guía rápida

Este directorio contiene notas adicionales sobre los conceptos de prueba
utilizados en este proyecto. Cada archivo fuente y test incluye docstrings
explicativos.

# Principios SOLID explicados con los tests en este proyecto

### DIP (dependency inversion principle)

Esto se puede ver en `conftest` y sobretodo en la clase `PaymentService` porque aca se inyecta mediante constructor el tipo de gateway de pago que se usara `gateway` y se hara un `charge` para cobrar al usuario

```py
class PaymentService:
    """Ejemplo de servicio con dependencias inyectadas"""
    def __init__(
        self,
        gateway: PaymentGatewayInterface,
        payment_repo: PaymentRepositoryInterface,
        user_repo: UserRepositoryInterface,
    ):
        self.gateway = gateway
        self.payment_repo = payment_repo
        self.user_repo = user_repo

    def process_payment(self, username: str, amount: Decimal) -> bool:
        user = self.user_repo.get(username)
        result = self.gateway.charge(user.id, amount)
        if not result.success:
            return False
        self.payment_repo.record(user.id, amount)
        user.debit(amount)
        return True
```

En `confest`, el servicio se integra en el constructor de la siguiente manera:

```py
@pytest.fixture
def fake_gateway_success():
    return DummyGateway(should_succeed=True)

@pytest.fixture
def fake_gateway_fail():
    return DummyGateway(should_succeed=False)

@pytest.fixture
def payment_service(fake_gateway_success, payment_repo, user_repo):
    return PaymentService(fake_gateway_success, payment_repo, user_repo)
```

Utilizando 2 gateways para fail y success, de esta manera el test depende del fixture fake_gateway y no un tipo especifico


### SRP (single responsibility principle)

Esto significa que cada fixture en conftest tenga una responsabilidad bien definida, en `conftest`:

```py
@pytest.fixture
def user_repo():
    return InMemoryUserRepository()

@pytest.fixture
def payment_repo():
    return InMemoryPaymentRepository()
```

Aca cada fixture usa un repositorio y estan separados, cada repositorio es en funcionalidad similar a una lista o a un diccionario, de tal manera que cada uno puede ser integrado para el fixture de `payment_service` siendo inyectados en el constructor de este.

### OCP (open closed principle)

Esto es usado en los test, en los casos de parametrize, donde cada parametro es un input para el test donde se aplica el decorador. Si se altera el test que usa `parametrize`

```py
@pytest.mark.parametrize("times,delay", [(1,0),(2,0),(3,0.01)])
def test_retry_decorator(times, delay):
    calls = []
    @retry(times=times, delay=delay)
    def flaky():
        calls.append(1)
        if len(calls) < times:
            raise RuntimeError("fail")
        return "ok"
    assert flaky() == "ok"
    assert len(calls) == times
```

Esto se puede extender usando `[(1,0),(2,0),(3,0.01), (5, 0.099)]` y testeando el mismo decorador.

### LSP (Liskov subsitution principle)

La idea es que los subtipos pueda ser sustituidos por sus tipos, en este case se ve en el py `gateway`, donde:

```py

class DummyGateway(PaymentGatewayInterface):
    def __init__(self, should_succeed: bool = True):
        self.should_succeed = should_succeed

    def charge(self, user_id: str, amount: Decimal):
        return SimpleNamespace(success=self.should_succeed)
```

DummyGateway es una subclase de `PaymentGatewayInterface` y esta interfaz es usada para realizar inyeccion en `PaymentService` y cargar al usuario.


### ISP (interface segregation principle)

Para el `PaymentService` se usa el metodo `charge` y este es usado para cargar al usuario de tal manera que este servcio no define este metodo sino viene de su dependencia `gateway`. De igual manera en los repos usados en fixture se crean interfaces (similares a ABC?) para que cada repo usada en fixture tenga los metodos bien definidos:

```py
class UserRepositoryInterface:
    def add(self, user: User): ...
    def get(self, username: str) -> User: ...

class InMemoryUserRepository(UserRepositoryInterface):
def __init__(self):
    self._store: Dict[str, User] = {}

def add(self, user: User):
    if user.username in self._store:
        raise KeyError(user.username)
    self._store[user.username] = user

def get(self, username: str) -> User:
    return self._store[username]
    ```