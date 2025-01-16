from .user import UserSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .autor import AutorSerializer
from .livro import (
    LivroAjustarEstoqueSerializer,
    LivroAlterarPrecoSerializer,
    LivroSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
)
from .compra import (
    CompraSerializer,
    ItensCompraSerializer,
    CompraCreateUpdateSerializer,
    CompraListSerializer,
    ItensCompraListSerializer,
    ItensCompraSerializer,
)
