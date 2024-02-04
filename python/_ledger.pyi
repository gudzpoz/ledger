import Boost.Python
from _typeshed import Incomplete
from typing import ClassVar

ACCOUNT_EXT_AUTO_VIRTUALIZE: int
ACCOUNT_EXT_DISPLAYED: int
ACCOUNT_EXT_HAS_NON_VIRTUALS: int
ACCOUNT_EXT_HAS_UNB_VIRTUALS: int
ACCOUNT_EXT_MATCHING: int
ACCOUNT_EXT_SORT_CALC: int
ACCOUNT_EXT_TO_DISPLAY: int
ACCOUNT_EXT_VISITED: int
ACCOUNT_KNOWN: int
ACCOUNT_NORMAL: int
ACCOUNT_TEMP: int
COMMODITY_BUILTIN: int
COMMODITY_KNOWN: int
COMMODITY_NOMARKET: int
COMMODITY_PRIMARY: int
COMMODITY_STYLE_DECIMAL_COMMA: int
COMMODITY_STYLE_DEFAULTS: int
COMMODITY_STYLE_SEPARATED: int
COMMODITY_STYLE_SUFFIXED: int
COMMODITY_STYLE_THOUSANDS: int
COMMODITY_STYLE_TIME_COLON: int
COMMODITY_WALKED: int
ITEM_GENERATED: int
ITEM_NORMAL: int
ITEM_TEMP: int
NULL_VALUE: Value
POST_CALCULATED: int
POST_COST_CALCULATED: int
POST_EXT_COMPOUND: int
POST_EXT_CONSIDERED: int
POST_EXT_DIRECT_AMT: int
POST_EXT_DISPLAYED: int
POST_EXT_HANDLED: int
POST_EXT_MATCHES: int
POST_EXT_RECEIVED: int
POST_EXT_SORT_CALC: int
POST_EXT_VISITED: int
POST_MUST_BALANCE: int
POST_VIRTUAL: int
__date__: str
__version__: str
commodities: CommodityPool
session: Session

class Account(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    flags: Incomplete
    name: Incomplete
    note: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def accounts(cls, *args, **kwargs):
        """
        accounts( (object)arg1) -> object"""
    @classmethod
    def add_account(cls, *args, **kwargs):
        """
        add_account( (Account)arg1, (Account)arg2) -> None"""
    @classmethod
    def add_flags(cls, *args, **kwargs):
        """
        add_flags( (Account)arg1, (int)arg2) -> None"""
    @classmethod
    def add_post(cls, *args, **kwargs):
        """
        add_post( (Account)arg1, (Posting)arg2) -> None"""
    @classmethod
    def amount(cls, *args, **kwargs):
        """
        amount( (Account)arg1) -> Value

        amount( (Account)arg1, (object)expr) -> Value"""
    @classmethod
    def children_with_flags(cls, *args, **kwargs):
        """
        children_with_flags( (Account)arg1, (int)arg2) -> int"""
    @classmethod
    def clear_flags(cls, *args, **kwargs):
        """
        clear_flags( (Account)arg1) -> None"""
    @classmethod
    def clear_xdata(cls, *args, **kwargs):
        """
        clear_xdata( (Account)arg1) -> None"""
    @classmethod
    def drop_flags(cls, *args, **kwargs):
        """
        drop_flags( (Account)arg1, (int)arg2) -> None"""
    @classmethod
    def family_details(cls, *args, **kwargs):
        """
        family_details( (Account)arg1, (bool)arg2) -> AccountXDataDetails"""
    @classmethod
    def find_account(cls, *args, **kwargs):
        """
        find_account( (Account)arg1, (str)arg2, (bool)arg3) -> Account"""
    @classmethod
    def find_account_re(cls, *args, **kwargs):
        """
        find_account_re( (Account)arg1, (str)arg2, (bool)arg3) -> Account"""
    @classmethod
    def fullname(cls, *args, **kwargs):
        """
        fullname( (Account)arg1) -> str"""
    @classmethod
    def has_flags(cls, *args, **kwargs):
        """
        has_flags( (Account)arg1, (int)arg2) -> bool"""
    @classmethod
    def has_xdata(cls, *args, **kwargs):
        """
        has_xdata( (Account)arg1) -> bool"""
    @classmethod
    def has_xflags(cls, *args, **kwargs):
        """
        has_xflags( (Account)arg1, (int)arg2) -> bool"""
    @classmethod
    def partial_name(cls, *args, **kwargs):
        """
        partial_name( (Account)arg1, (bool)arg2) -> str"""
    @classmethod
    def posts(cls, *args, **kwargs):
        """
        posts( (object)arg1) -> object"""
    @classmethod
    def remove_account(cls, *args, **kwargs):
        """
        remove_account( (Account)arg1, (Account)arg2) -> bool"""
    @classmethod
    def remove_post(cls, *args, **kwargs):
        """
        remove_post( (Account)arg1, (Posting)arg2) -> bool"""
    @classmethod
    def self_details(cls, *args, **kwargs):
        """
        self_details( (Account)arg1, (bool)arg2) -> AccountXDataDetails"""
    @classmethod
    def total(cls, *args, **kwargs):
        """
        total( (Account)arg1) -> Value

        total( (Account)arg1, (object)expr) -> Value"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (Account)arg1) -> bool"""
    @classmethod
    def xdata(cls, *args, **kwargs):
        """
        xdata( (Account)arg1) -> AccountXData"""
    @classmethod
    def __getitem__(cls, index):
        """
        __getitem__( (Account)arg1, (int)arg2) -> Account"""
    @classmethod
    def __iter__(cls):
        """
        __iter__( (object)arg1) -> object"""
    @classmethod
    def __len__(cls) -> int:
        """
        __len__( (Account)arg1) -> int"""
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __unicode__(cls, *args, **kwargs):
        """
        __unicode__( (Account)arg1) -> object"""
    @property
    def depth(self): ...
    @property
    def parent(self): ...

class AccountXData(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    flags: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def add_flags(cls, *args, **kwargs):
        """
        add_flags( (SupportFlags16)arg1, (int)arg2) -> None"""
    @classmethod
    def clear_flags(cls, *args, **kwargs):
        """
        clear_flags( (SupportFlags16)arg1) -> None"""
    @classmethod
    def drop_flags(cls, *args, **kwargs):
        """
        drop_flags( (SupportFlags16)arg1, (int)arg2) -> None"""
    @classmethod
    def has_flags(cls, *args, **kwargs):
        """
        has_flags( (SupportFlags16)arg1, (int)arg2) -> bool"""
    @classmethod
    def __reduce__(cls): ...
    @property
    def family_details(self): ...
    @property
    def reported_posts(self): ...
    @property
    def self_details(self): ...
    @property
    def sort_values(self): ...

class AccountXDataDetails(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def update(cls, *args, **kwargs):
        """
        update( (AccountXDataDetails)arg1, (Posting)arg2, (bool)arg3) -> None"""
    @classmethod
    def __iadd__(cls, other):
        """
        __iadd__( (object)arg1, (AccountXDataDetails)arg2) -> object"""
    @classmethod
    def __reduce__(cls): ...
    @property
    def accounts_referenced(self): ...
    @property
    def calculated(self): ...
    @property
    def earliest_cleared_post(self): ...
    @property
    def earliest_post(self): ...
    @property
    def filenames(self): ...
    @property
    def gathered(self): ...
    @property
    def latest_cleared_post(self): ...
    @property
    def latest_post(self): ...
    @property
    def payees_referenced(self): ...
    @property
    def posts_cleared_count(self): ...
    @property
    def posts_count(self): ...
    @property
    def posts_last_30_count(self): ...
    @property
    def posts_last_7_count(self): ...
    @property
    def posts_this_month_count(self): ...
    @property
    def posts_virtuals_count(self): ...
    @property
    def real_total(self): ...
    @property
    def total(self): ...

class Amount(Boost.Python.instance):
    is_initialized: ClassVar[bool] = ...
    stream_fullstrings: ClassVar[bool] = ...
    __instance_size__: ClassVar[int] = ...
    commodity: Incomplete
    keep_precision: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (int)arg2) -> None

        __init__( (object)arg1, (str)arg2) -> None

        __init__( (object)arg1, (Amount)arg2) -> None"""
    @classmethod
    def abs(cls, *args, **kwargs):
        """
        abs( (Amount)arg1) -> Amount"""
    @classmethod
    def annotate(cls, *args, **kwargs):
        """
        annotate( (Amount)arg1, (Annotation)arg2) -> None"""
    @classmethod
    def clear_commodity(cls, *args, **kwargs):
        """
        clear_commodity( (Amount)arg1) -> None"""
    @classmethod
    def compare(cls, *args, **kwargs):
        """
        compare( (Amount)arg1, (Amount)amount) -> int :
            Compare two amounts for equality, returning <0, 0 or >0."""
    @classmethod
    def exact(cls, *args, **kwargs):
        """
        exact( (str)value) -> Amount :
            Construct an amount object whose display precision is always equal to its
            internal precision."""
    @classmethod
    def fits_in_long(cls, *args, **kwargs):
        """
        fits_in_long( (Amount)arg1) -> bool"""
    @classmethod
    def floored(cls, *args, **kwargs):
        """
        floored( (Amount)arg1) -> Amount"""
    @classmethod
    def has_annotation(cls, *args, **kwargs):
        """
        has_annotation( (Amount)arg1) -> bool"""
    @classmethod
    def has_commodity(cls, *args, **kwargs):
        """
        has_commodity( (Amount)arg1) -> bool"""
    @classmethod
    def in_place_floor(cls, *args, **kwargs):
        """
        in_place_floor( (Amount)arg1) -> None"""
    @classmethod
    def in_place_negate(cls, *args, **kwargs):
        """
        in_place_negate( (Amount)arg1) -> None"""
    @classmethod
    def in_place_reduce(cls, *args, **kwargs):
        """
        in_place_reduce( (Amount)arg1) -> None"""
    @classmethod
    def in_place_round(cls, *args, **kwargs):
        """
        in_place_round( (Amount)arg1) -> None"""
    @classmethod
    def in_place_truncate(cls, *args, **kwargs):
        """
        in_place_truncate( (Amount)arg1) -> None"""
    @classmethod
    def in_place_unreduce(cls, *args, **kwargs):
        """
        in_place_unreduce( (Amount)arg1) -> None"""
    @classmethod
    def in_place_unround(cls, *args, **kwargs):
        """
        in_place_unround( (Amount)arg1) -> None"""
    @classmethod
    def initialize(cls) -> None:
        """
        initialize() -> None"""
    @classmethod
    def inverted(cls, *args, **kwargs):
        """
        inverted( (Amount)arg1) -> Amount"""
    @classmethod
    def is_nonzero(cls, *args, **kwargs):
        """
        is_nonzero( (Amount)arg1) -> bool"""
    @classmethod
    def is_null(cls, *args, **kwargs):
        """
        is_null( (Amount)arg1) -> bool"""
    @classmethod
    def is_realzero(cls, *args, **kwargs):
        """
        is_realzero( (Amount)arg1) -> bool"""
    @classmethod
    def is_zero(cls, *args, **kwargs):
        """
        is_zero( (Amount)arg1) -> bool"""
    @classmethod
    def negated(cls, *args, **kwargs):
        """
        negated( (Amount)arg1) -> Amount"""
    @classmethod
    def number(cls, *args, **kwargs):
        """
        number( (Amount)arg1) -> Amount"""
    @classmethod
    def parse(cls, *args, **kwargs):
        """
        parse( (Amount)arg1, (str)arg2) -> None

        parse( (Amount)arg1, (str)arg2, (int)arg3) -> None"""
    @classmethod
    def parse_conversion(cls, *args, **kwargs):
        """
        parse_conversion( (str)arg1, (str)arg2) -> None"""
    @classmethod
    def price(cls, *args, **kwargs):
        """
        price( (Amount)arg1) -> object"""
    @classmethod
    def quantity_string(cls, *args, **kwargs):
        """
        quantity_string( (Amount)arg1) -> str"""
    @classmethod
    def reduced(cls, *args, **kwargs):
        """
        reduced( (Amount)arg1) -> Amount"""
    @classmethod
    def rounded(cls, *args, **kwargs):
        """
        rounded( (Amount)arg1) -> Amount"""
    @classmethod
    def shutdown(cls) -> None:
        """
        shutdown() -> None"""
    @classmethod
    def sign(cls, *args, **kwargs):
        """
        sign( (Amount)arg1) -> int"""
    @classmethod
    def strip_annotations(cls, *args, **kwargs):
        """
        strip_annotations( (Amount)arg1) -> Amount

        strip_annotations( (Amount)arg1, (KeepDetails)arg2) -> Amount"""
    @classmethod
    def to_double(cls, *args, **kwargs):
        """
        to_double( (Amount)arg1) -> float"""
    @classmethod
    def to_fullstring(cls, *args, **kwargs):
        """
        to_fullstring( (Amount)arg1) -> str"""
    @classmethod
    def to_long(cls, *args, **kwargs):
        """
        to_long( (Amount)arg1) -> int"""
    @classmethod
    def to_string(cls, *args, **kwargs):
        """
        to_string( (Amount)arg1) -> str"""
    @classmethod
    def truncated(cls, *args, **kwargs):
        """
        truncated( (Amount)arg1) -> Amount"""
    @classmethod
    def unreduced(cls, *args, **kwargs):
        """
        unreduced( (Amount)arg1) -> Amount"""
    @classmethod
    def unrounded(cls, *args, **kwargs):
        """
        unrounded( (Amount)arg1) -> Amount"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (Amount)arg1) -> bool"""
    @classmethod
    def value(cls, *args, **kwargs):
        """
        value( (Amount)arg1) -> object

        value( (Amount)arg1, (Commodity)in_terms_of) -> object

        value( (Amount)arg1, (Commodity)in_terms_of, (object)moment) -> object

        value( (Amount)arg1, (Commodity)in_terms_of, (object)moment) -> object"""
    @classmethod
    def with_commodity(cls, *args, **kwargs):
        """
        with_commodity( (Amount)arg1, (Commodity)arg2) -> Amount"""
    @classmethod
    def __abs__(cls):
        """
        __abs__( (Amount)arg1) -> Amount"""
    @classmethod
    def __add__(cls, other):
        """
        __add__( (Amount)arg1, (Amount)arg2) -> object

        __add__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __bool__(cls) -> bool:
        """
        __bool__( (Amount)arg1) -> object"""
    @classmethod
    def __eq__(cls, other: object) -> bool:
        """
        __eq__( (Amount)arg1, (Amount)arg2) -> object

        __eq__( (Amount)arg1, (int)arg2) -> object

        __eq__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __float__(cls) -> float:
        """
        __float__( (Amount)arg1) -> float"""
    @classmethod
    def __ge__(cls, other: object) -> bool:
        """
        __ge__( (Amount)arg1, (int)arg2) -> object

        __ge__( (Amount)arg1, (Amount)arg2) -> object

        __ge__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __gt__(cls, other: object) -> bool:
        """
        __gt__( (Amount)arg1, (int)arg2) -> object

        __gt__( (Amount)arg1, (Amount)arg2) -> object

        __gt__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __iadd__(cls, other):
        """
        __iadd__( (object)arg1, (Amount)arg2) -> object

        __iadd__( (object)arg1, (int)arg2) -> object"""
    @classmethod
    def __idiv__(cls, *args, **kwargs):
        """
        __idiv__( (object)arg1, (Amount)arg2) -> object

        __idiv__( (object)arg1, (int)arg2) -> object"""
    @classmethod
    def __imul__(cls, other):
        """
        __imul__( (object)arg1, (Amount)arg2) -> object

        __imul__( (object)arg1, (int)arg2) -> object"""
    @classmethod
    def __int__(cls) -> int:
        """
        __int__( (Amount)arg1) -> int"""
    @classmethod
    def __isub__(cls, other):
        """
        __isub__( (object)arg1, (Amount)arg2) -> object

        __isub__( (object)arg1, (int)arg2) -> object"""
    @classmethod
    def __le__(cls, other: object) -> bool:
        """
        __le__( (Amount)arg1, (Amount)arg2) -> object

        __le__( (Amount)arg1, (int)arg2) -> object

        __le__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __lt__(cls, other: object) -> bool:
        """
        __lt__( (Amount)arg1, (Amount)arg2) -> object

        __lt__( (Amount)arg1, (int)arg2) -> object

        __lt__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __mul__(cls, other):
        """
        __mul__( (Amount)arg1, (Amount)arg2) -> object

        __mul__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __ne__(cls, other: object) -> bool:
        """
        __ne__( (Amount)arg1, (Amount)arg2) -> object

        __ne__( (Amount)arg1, (int)arg2) -> object

        __ne__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __neg__(cls):
        """
        __neg__( (Amount)arg1) -> object"""
    @classmethod
    def __nonzero__(cls, *args, **kwargs):
        """
        __nonzero__( (Amount)arg1) -> bool"""
    @classmethod
    def __radd__(cls, other):
        """
        __radd__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __rmul__(cls, other):
        """
        __rmul__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __rsub__(cls, other):
        """
        __rsub__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __rtruediv__(cls, other):
        """
        __rtruediv__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __sub__(cls, other):
        """
        __sub__( (Amount)arg1, (Amount)arg2) -> object

        __sub__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __truediv__(cls, other):
        """
        __truediv__( (Amount)arg1, (Amount)arg2) -> object

        __truediv__( (Amount)arg1, (int)arg2) -> object"""
    @classmethod
    def __unicode__(cls, *args, **kwargs):
        """
        __unicode__( (Amount)arg1) -> object"""
    @property
    def annotation(self): ...
    @property
    def display_precision(self): ...
    @property
    def precision(self): ...

class AnnotatedCommodity(Commodity):
    details: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @classmethod
    def strip_annotations(cls, *args, **kwargs):
        """
        strip_annotations( (AnnotatedCommodity)arg1) -> Commodity

        strip_annotations( (AnnotatedCommodity)arg1, (KeepDetails)arg2) -> Commodity"""
    @classmethod
    def write_annotations(cls, *args, **kwargs):
        """
        write_annotations( (AnnotatedCommodity)arg1, (object)arg2, (bool)arg3) -> None"""
    @classmethod
    def __eq__(cls, other: object) -> bool:
        """
        __eq__( (AnnotatedCommodity)arg1, (AnnotatedCommodity)arg2) -> object

        __eq__( (AnnotatedCommodity)arg1, (Commodity)arg2) -> object"""
    @classmethod
    def __reduce__(cls): ...
    @property
    def referent(self): ...

class Annotation(Boost.Python.instance):
    date: Incomplete
    flags: Incomplete
    price: Incomplete
    tag: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @classmethod
    def add_flags(cls, *args, **kwargs):
        """
        add_flags( (Annotation)arg1, (int)arg2) -> None"""
    @classmethod
    def clear_flags(cls, *args, **kwargs):
        """
        clear_flags( (Annotation)arg1) -> None"""
    @classmethod
    def drop_flags(cls, *args, **kwargs):
        """
        drop_flags( (Annotation)arg1, (int)arg2) -> None"""
    @classmethod
    def has_flags(cls, *args, **kwargs):
        """
        has_flags( (Annotation)arg1, (int)arg2) -> bool"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (Annotation)arg1) -> bool"""
    @classmethod
    def __eq__(cls, other: object) -> bool:
        """
        __eq__( (Annotation)arg1, (Annotation)arg2) -> object"""
    @classmethod
    def __nonzero__(cls, *args, **kwargs):
        """
        __nonzero__( (Annotation)arg1) -> bool"""
    @classmethod
    def __reduce__(cls): ...

class AutomatedTransaction(TransactionBase):
    __instance_size__: ClassVar[int] = ...
    predicate: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (object)arg2) -> None"""
    @classmethod
    def extend_xact(cls, *args, **kwargs):
        """
        extend_xact( (AutomatedTransaction)arg1, (TransactionBase)arg2, (object)arg3) -> None"""
    @classmethod
    def __reduce__(cls): ...

class Balance(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (Balance)arg2) -> None

        __init__( (object)arg1, (Amount)arg2) -> None

        __init__( (object)arg1, (int)arg2) -> None

        __init__( (object)arg1, (str)arg2) -> None"""
    @classmethod
    def abs(cls, *args, **kwargs):
        """
        abs( (Balance)arg1) -> Balance"""
    @classmethod
    def commodity_amount(cls, *args, **kwargs):
        """
        commodity_amount( (Balance)arg1) -> object

        commodity_amount( (Balance)arg1, (Commodity)arg2) -> object"""
    @classmethod
    def commodity_count(cls, *args, **kwargs):
        """
        commodity_count( (Balance)arg1) -> int"""
    @classmethod
    def floored(cls, *args, **kwargs):
        """
        floored( (Balance)arg1) -> Balance"""
    @classmethod
    def in_place_floor(cls, *args, **kwargs):
        """
        in_place_floor( (Balance)arg1) -> None"""
    @classmethod
    def in_place_negate(cls, *args, **kwargs):
        """
        in_place_negate( (Balance)arg1) -> None"""
    @classmethod
    def in_place_reduce(cls, *args, **kwargs):
        """
        in_place_reduce( (Balance)arg1) -> None"""
    @classmethod
    def in_place_round(cls, *args, **kwargs):
        """
        in_place_round( (Balance)arg1) -> None"""
    @classmethod
    def in_place_truncate(cls, *args, **kwargs):
        """
        in_place_truncate( (Balance)arg1) -> None"""
    @classmethod
    def in_place_unreduce(cls, *args, **kwargs):
        """
        in_place_unreduce( (Balance)arg1) -> None"""
    @classmethod
    def in_place_unround(cls, *args, **kwargs):
        """
        in_place_unround( (Balance)arg1) -> None"""
    @classmethod
    def is_empty(cls, *args, **kwargs):
        """
        is_empty( (Balance)arg1) -> bool"""
    @classmethod
    def is_nonzero(cls, *args, **kwargs):
        """
        is_nonzero( (Balance)arg1) -> bool"""
    @classmethod
    def is_realzero(cls, *args, **kwargs):
        """
        is_realzero( (Balance)arg1) -> bool"""
    @classmethod
    def is_zero(cls, *args, **kwargs):
        """
        is_zero( (Balance)arg1) -> bool"""
    @classmethod
    def negated(cls, *args, **kwargs):
        """
        negated( (Balance)arg1) -> Balance"""
    @classmethod
    def number(cls, *args, **kwargs):
        """
        number( (Balance)arg1) -> Balance"""
    @classmethod
    def reduced(cls, *args, **kwargs):
        """
        reduced( (Balance)arg1) -> Balance"""
    @classmethod
    def rounded(cls, *args, **kwargs):
        """
        rounded( (Balance)arg1) -> Balance"""
    @classmethod
    def single_amount(cls, *args, **kwargs):
        """
        single_amount( (Balance)arg1) -> bool"""
    @classmethod
    def strip_annotations(cls, *args, **kwargs):
        """
        strip_annotations( (Balance)arg1) -> Balance

        strip_annotations( (Balance)arg1, (KeepDetails)arg2) -> Balance"""
    @classmethod
    def to_amount(cls, *args, **kwargs):
        """
        to_amount( (Balance)arg1) -> Amount"""
    @classmethod
    def to_string(cls, *args, **kwargs):
        """
        to_string( (Balance)arg1) -> str"""
    @classmethod
    def truncated(cls, *args, **kwargs):
        """
        truncated( (Balance)arg1) -> Balance"""
    @classmethod
    def unreduced(cls, *args, **kwargs):
        """
        unreduced( (Balance)arg1) -> Balance"""
    @classmethod
    def unrounded(cls, *args, **kwargs):
        """
        unrounded( (Balance)arg1) -> Balance"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (Balance)arg1) -> bool"""
    @classmethod
    def value(cls, *args, **kwargs):
        """
        value( (Balance)arg1) -> object

        value( (Balance)arg1, (Commodity)in_terms_of) -> object

        value( (Balance)arg1, (Commodity)in_terms_of, (object)moment) -> object

        value( (Balance)arg1, (Commodity)in_terms_of, (object)moment) -> object"""
    @classmethod
    def __abs__(cls):
        """
        __abs__( (Balance)arg1) -> Balance"""
    @classmethod
    def __add__(cls, other):
        """
        __add__( (Balance)arg1, (Balance)arg2) -> object

        __add__( (Balance)arg1, (Amount)arg2) -> object

        __add__( (Balance)arg1, (int)arg2) -> object"""
    @classmethod
    def __bool__(cls) -> bool:
        """
        __bool__( (Balance)arg1) -> object"""
    @classmethod
    def __eq__(cls, other: object) -> bool:
        """
        __eq__( (Balance)arg1, (Balance)arg2) -> object

        __eq__( (Balance)arg1, (Amount)arg2) -> object

        __eq__( (Balance)arg1, (int)arg2) -> object"""
    @classmethod
    def __getitem__(cls, index):
        """
        __getitem__( (Balance)arg1, (int)arg2) -> Amount"""
    @classmethod
    def __iadd__(cls, other):
        """
        __iadd__( (object)arg1, (Balance)arg2) -> object

        __iadd__( (object)arg1, (Amount)arg2) -> object

        __iadd__( (object)arg1, (int)arg2) -> object"""
    @classmethod
    def __idiv__(cls, *args, **kwargs):
        """
        __idiv__( (object)arg1, (Amount)arg2) -> object

        __idiv__( (object)arg1, (int)arg2) -> object"""
    @classmethod
    def __imul__(cls, other):
        """
        __imul__( (object)arg1, (Amount)arg2) -> object

        __imul__( (object)arg1, (int)arg2) -> object"""
    @classmethod
    def __isub__(cls, other):
        """
        __isub__( (object)arg1, (Balance)arg2) -> object

        __isub__( (object)arg1, (Amount)arg2) -> object

        __isub__( (object)arg1, (int)arg2) -> object"""
    @classmethod
    def __len__(cls) -> int:
        """
        __len__( (Balance)arg1) -> int"""
    @classmethod
    def __mul__(cls, other):
        """
        __mul__( (Balance)arg1, (Amount)arg2) -> object

        __mul__( (Balance)arg1, (int)arg2) -> object"""
    @classmethod
    def __ne__(cls, other: object) -> bool:
        """
        __ne__( (Balance)arg1, (Balance)arg2) -> object

        __ne__( (Balance)arg1, (Amount)arg2) -> object

        __ne__( (Balance)arg1, (int)arg2) -> object"""
    @classmethod
    def __neg__(cls):
        """
        __neg__( (Balance)arg1) -> object

        __neg__( (Balance)arg1) -> object"""
    @classmethod
    def __nonzero__(cls, *args, **kwargs):
        """
        __nonzero__( (Balance)arg1) -> bool"""
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __sub__(cls, other):
        """
        __sub__( (Balance)arg1, (Balance)arg2) -> object

        __sub__( (Balance)arg1, (Amount)arg2) -> object

        __sub__( (Balance)arg1, (int)arg2) -> object"""
    @classmethod
    def __truediv__(cls, other):
        """
        __truediv__( (Balance)arg1, (Amount)arg2) -> object

        __truediv__( (Balance)arg1, (int)arg2) -> object"""
    @classmethod
    def __unicode__(cls, *args, **kwargs):
        """
        __unicode__( (Balance)arg1) -> object"""

class Commodity(Boost.Python.instance):
    decimal_comma_by_default: ClassVar[bool] = ...
    flags: Incomplete
    larger: Incomplete
    name: Incomplete
    note: Incomplete
    precision: Incomplete
    smaller: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @classmethod
    def add_flags(cls, *args, **kwargs):
        """
        add_flags( (Commodity)arg1, (int)arg2) -> None"""
    @classmethod
    def add_price(cls, *args, **kwargs):
        """
        add_price( (Commodity)arg1, (object)arg2, (Amount)arg3) -> None

        add_price( (Commodity)arg1, (object)arg2, (Amount)arg3, (bool)arg4) -> None"""
    @classmethod
    def check_for_updated_price(cls, *args, **kwargs):
        """
        check_for_updated_price( (Commodity)arg1, (object)arg2, (object)arg3, (Commodity)arg4) -> object"""
    @classmethod
    def clear_flags(cls, *args, **kwargs):
        """
        clear_flags( (Commodity)arg1) -> None"""
    @classmethod
    def drop_flags(cls, *args, **kwargs):
        """
        drop_flags( (Commodity)arg1, (int)arg2) -> None"""
    @classmethod
    def find_price(cls, *args, **kwargs):
        """
        find_price( (Commodity)arg1, (Commodity)arg2, (object)arg3, (object)arg4) -> object"""
    @classmethod
    def has_annotation(cls, *args, **kwargs):
        """
        has_annotation( (Commodity)arg1) -> bool"""
    @classmethod
    def has_flags(cls, *args, **kwargs):
        """
        has_flags( (Commodity)arg1, (int)arg2) -> bool"""
    @classmethod
    def pool(cls, *args, **kwargs):
        """
        pool( (Commodity)arg1) -> CommodityPool"""
    @classmethod
    def remove_price(cls, *args, **kwargs):
        """
        remove_price( (Commodity)arg1, (object)arg2, (Commodity)arg3) -> None"""
    @classmethod
    def strip_annotations(cls, *args, **kwargs):
        """
        strip_annotations( (Commodity)arg1) -> Commodity

        strip_annotations( (Commodity)arg1, (KeepDetails)arg2) -> Commodity"""
    @classmethod
    def symbol_needs_quotes(cls, *args, **kwargs):
        """
        symbol_needs_quotes( (str)arg1) -> bool"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (Commodity)arg1) -> bool"""
    @classmethod
    def write_annotations(cls, *args, **kwargs):
        """
        write_annotations( (Commodity)arg1, (object)arg2, (bool)arg3) -> None"""
    @classmethod
    def __eq__(cls, other: object) -> bool:
        """
        __eq__( (Commodity)arg1, (Commodity)arg2) -> object"""
    @classmethod
    def __nonzero__(cls, *args, **kwargs):
        """
        __nonzero__( (Commodity)arg1) -> bool"""
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __unicode__(cls, *args, **kwargs):
        """
        __unicode__( (Commodity)arg1) -> object"""
    @property
    def base_symbol(self): ...
    @property
    def referent(self): ...
    @property
    def symbol(self): ...

class CommodityPool(Boost.Python.instance):
    default_commodity: Incomplete
    get_commodity_quote: Incomplete
    get_quotes: Incomplete
    keep_base: Incomplete
    price_db: Incomplete
    quote_leeway: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @classmethod
    def create(cls, *args, **kwargs):
        """
        create( (CommodityPool)arg1, (str)arg2) -> Commodity

        create( (CommodityPool)arg1, (str)arg2, (Annotation)arg3) -> Commodity"""
    @classmethod
    def exchange(cls, *args, **kwargs):
        """
        exchange( (CommodityPool)arg1, (Commodity)arg2, (Amount)arg3) -> None

        exchange( (CommodityPool)arg1, (Commodity)arg2, (Amount)arg3, (object)arg4) -> None

        exchange( (CommodityPool)arg1, (Amount)arg2, (Amount)arg3, (bool)arg4, (bool)arg5, (object)arg6, (object)arg7) -> object"""
    @classmethod
    def find(cls, *args, **kwargs):
        """
        find( (CommodityPool)arg1, (str)arg2) -> Commodity

        find( (CommodityPool)arg1, (str)arg2, (Annotation)arg3) -> Commodity"""
    @classmethod
    def find_or_create(cls, *args, **kwargs):
        """
        find_or_create( (CommodityPool)arg1, (str)arg2) -> Commodity

        find_or_create( (CommodityPool)arg1, (str)arg2, (Annotation)arg3) -> Commodity"""
    @classmethod
    def has_key(cls, *args, **kwargs):
        """
        has_key( (CommodityPool)arg1, (str)arg2) -> bool"""
    @classmethod
    def iteritems(cls, *args, **kwargs):
        """
        iteritems( (object)arg1) -> object"""
    @classmethod
    def iterkeys(cls, *args, **kwargs):
        """
        iterkeys( (object)arg1) -> object"""
    @classmethod
    def itervalues(cls, *args, **kwargs):
        """
        itervalues( (object)arg1) -> object"""
    @classmethod
    def keys(cls, *args, **kwargs):
        """
        keys( (CommodityPool)arg1) -> list"""
    @classmethod
    def parse_price_directive(cls, *args, **kwargs):
        """
        parse_price_directive( (CommodityPool)arg1, (str)arg2, (bool)arg3, (bool)arg4) -> object"""
    @classmethod
    def parse_price_expression(cls, *args, **kwargs):
        """
        parse_price_expression( (CommodityPool)arg1, (str)arg2, (bool)arg3, (object)arg4) -> Commodity"""
    @classmethod
    def __contains__(cls, other) -> bool:
        """
        __contains__( (CommodityPool)arg1, (str)arg2) -> bool"""
    @classmethod
    def __getitem__(cls, index):
        """
        __getitem__( (CommodityPool)arg1, (str)arg2) -> Commodity"""
    @classmethod
    def __iter__(cls):
        """
        __iter__( (object)arg1) -> object"""
    @classmethod
    def __reduce__(cls): ...
    @property
    def null_commodity(self): ...

class DelegatesFlags16(Boost.Python.instance):
    flags: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @classmethod
    def add_flags(cls, *args, **kwargs):
        """
        add_flags( (DelegatesFlags16)arg1, (int)arg2) -> None"""
    @classmethod
    def clear_flags(cls, *args, **kwargs):
        """
        clear_flags( (DelegatesFlags16)arg1) -> None"""
    @classmethod
    def drop_flags(cls, *args, **kwargs):
        """
        drop_flags( (DelegatesFlags16)arg1, (int)arg2) -> None"""
    @classmethod
    def has_flags(cls, *args, **kwargs):
        """
        has_flags( (DelegatesFlags16)arg1, (int)arg2) -> bool"""
    @classmethod
    def __reduce__(cls): ...

class Expr(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (str)arg2) -> None"""
    @classmethod
    def compile(cls, *args, **kwargs):
        """
        compile( (Expr)arg1, (object)arg2) -> None"""
    @classmethod
    def is_constant(cls, *args, **kwargs):
        """
        is_constant( (Expr)arg1) -> bool"""
    @classmethod
    def set_text(cls, *args, **kwargs):
        """
        set_text( (Expr)arg1, (str)arg2) -> None"""
    @classmethod
    def text(cls, *args, **kwargs):
        """
        text( (Expr)arg1) -> str"""
    @classmethod
    def __call__(cls, *args, **kwargs):
        """
        __call__( (Expr)arg1) -> Value"""
    @classmethod
    def __nonzero__(cls, *args, **kwargs):
        """
        __nonzero__( (Expr)arg1) -> bool"""
    @classmethod
    def __reduce__(cls): ...

class FileInfo(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    filename: Incomplete
    from_stream: Incomplete
    modtime: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (object)arg2) -> None"""
    @classmethod
    def __reduce__(cls): ...

class Journal(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    bucket: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def add_account(cls, *args, **kwargs):
        """
        add_account( (Journal)arg1, (Account)arg2) -> None"""
    @classmethod
    def add_xact(cls, *args, **kwargs):
        """
        add_xact( (Journal)arg1, (Transaction)arg2) -> bool"""
    @classmethod
    def auto_xacts(cls, *args, **kwargs):
        """
        auto_xacts( (object)arg1) -> object"""
    @classmethod
    def clear_xdata(cls, *args, **kwargs):
        """
        clear_xdata( (Journal)arg1) -> None"""
    @classmethod
    def expand_aliases(cls, *args, **kwargs):
        """
        expand_aliases( (Journal)arg1, (str)arg2) -> Account"""
    @classmethod
    def find_account(cls, *args, **kwargs):
        """
        find_account( (Journal)arg1, (str)arg2) -> Account

        find_account( (Journal)arg1, (str)arg2, (bool)arg3) -> Account"""
    @classmethod
    def find_account_re(cls, *args, **kwargs):
        """
        find_account_re( (Journal)arg1, (str)arg2) -> Account"""
    @classmethod
    def has_xdata(cls, *args, **kwargs):
        """
        has_xdata( (Journal)arg1) -> bool"""
    @classmethod
    def period_xacts(cls, *args, **kwargs):
        """
        period_xacts( (object)arg1) -> object"""
    @classmethod
    def query(cls, *args, **kwargs):
        """
        query( (Journal)arg1, (str)arg2) -> PostCollectorWrapper"""
    @classmethod
    def register_account(cls, *args, **kwargs):
        """
        register_account( (Journal)arg1, (str)arg2, (Posting)arg3) -> Account"""
    @classmethod
    def remove_account(cls, *args, **kwargs):
        """
        remove_account( (Journal)arg1, (Account)arg2) -> bool"""
    @classmethod
    def remove_xact(cls, *args, **kwargs):
        """
        remove_xact( (Journal)arg1, (Transaction)arg2) -> bool"""
    @classmethod
    def sources(cls, *args, **kwargs):
        """
        sources( (object)arg1) -> object"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (Journal)arg1) -> bool"""
    @classmethod
    def xacts(cls, *args, **kwargs):
        """
        xacts( (object)arg1) -> object"""
    @classmethod
    def __iter__(cls):
        """
        __iter__( (object)arg1) -> object"""
    @classmethod
    def __len__(cls) -> int:
        """
        __len__( (Journal)arg1) -> int"""
    @classmethod
    def __reduce__(cls): ...
    @property
    def master(self): ...
    @property
    def was_loaded(self): ...

class JournalItem(Boost.Python.instance):
    use_aux_date: ClassVar[bool] = ...
    aux_date: Incomplete
    date: Incomplete
    flags: Incomplete
    metadata: Incomplete
    note: Incomplete
    pos: Incomplete
    state: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @classmethod
    def add_flags(cls, *args, **kwargs):
        """
        add_flags( (SupportFlags8)arg1, (int)arg2) -> None"""
    @classmethod
    def append_note(cls, *args, **kwargs):
        """
        append_note( (JournalItem)arg1, (str)arg2, (object)arg3, (bool)arg4) -> None"""
    @classmethod
    def clear_flags(cls, *args, **kwargs):
        """
        clear_flags( (SupportFlags8)arg1) -> None"""
    @classmethod
    def copy_details(cls, *args, **kwargs):
        """
        copy_details( (JournalItem)arg1, (JournalItem)arg2) -> None"""
    @classmethod
    def drop_flags(cls, *args, **kwargs):
        """
        drop_flags( (SupportFlags8)arg1, (int)arg2) -> None"""
    @classmethod
    def get_tag(cls, *args, **kwargs):
        """
        get_tag( (JournalItem)arg1, (str)arg2) -> object

        get_tag( (JournalItem)arg1, (object)arg2) -> object

        get_tag( (JournalItem)arg1, (object)arg2, (object)arg3) -> object"""
    @classmethod
    def has_flags(cls, *args, **kwargs):
        """
        has_flags( (SupportFlags8)arg1, (int)arg2) -> bool"""
    @classmethod
    def has_tag(cls, *args, **kwargs):
        """
        has_tag( (JournalItem)arg1, (str)arg2) -> bool

        has_tag( (JournalItem)arg1, (object)arg2) -> bool

        has_tag( (JournalItem)arg1, (object)arg2, (object)arg3) -> bool"""
    @classmethod
    def lookup(cls, *args, **kwargs):
        """
        lookup( (JournalItem)arg1, (object)arg2, (str)arg3) -> object"""
    @classmethod
    def parse_tags(cls, *args, **kwargs):
        """
        parse_tags( (JournalItem)arg1, (str)arg2, (object)arg3, (bool)arg4) -> None"""
    @classmethod
    def set_tag(cls, *args, **kwargs):
        """
        set_tag( (JournalItem)arg1, (str)arg2, (object)arg3, (bool)arg4) -> object"""
    @classmethod
    def tag(cls, *args, **kwargs):
        """
        tag( (JournalItem)arg1, (str)arg2) -> object

        tag( (JournalItem)arg1, (object)arg2) -> object

        tag( (JournalItem)arg1, (object)arg2, (object)arg3) -> object"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (JournalItem)arg1) -> bool"""
    @classmethod
    def __eq__(cls, other: object) -> bool:
        """
        __eq__( (JournalItem)arg1, (JournalItem)arg2) -> object"""
    @classmethod
    def __ne__(cls, other: object) -> bool:
        """
        __ne__( (JournalItem)arg1, (JournalItem)arg2) -> object"""
    @classmethod
    def __reduce__(cls): ...

class KeepDetails(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    keep_date: Incomplete
    keep_price: Incomplete
    keep_tag: Incomplete
    only_actuals: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (bool)arg2, (bool)arg3, (bool)arg4, (bool)arg5) -> None"""
    @classmethod
    def keep_all(cls, *args, **kwargs):
        """
        keep_all( (KeepDetails)arg1) -> bool

        keep_all( (KeepDetails)arg1, (Commodity)arg2) -> bool"""
    @classmethod
    def keep_any(cls, *args, **kwargs):
        """
        keep_any( (KeepDetails)arg1) -> bool

        keep_any( (KeepDetails)arg1, (Commodity)arg2) -> bool"""
    @classmethod
    def __reduce__(cls): ...

class ParseFlags(Boost.Python.enum):
    Default: ClassVar[ParseFlags] = ...
    NoAssign: ClassVar[ParseFlags] = ...
    NoMigrate: ClassVar[ParseFlags] = ...
    NoReduce: ClassVar[ParseFlags] = ...
    OpContext: ClassVar[ParseFlags] = ...
    Partial: ClassVar[ParseFlags] = ...
    Single: ClassVar[ParseFlags] = ...
    SoftFail: ClassVar[ParseFlags] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class PeriodicTransaction(TransactionBase):
    __instance_size__: ClassVar[int] = ...
    period: Incomplete
    period_string: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (str)arg2) -> None"""
    @classmethod
    def __reduce__(cls): ...

class Position(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    beg_line: Incomplete
    beg_pos: Incomplete
    end_line: Incomplete
    end_pos: Incomplete
    pathname: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def __reduce__(cls): ...

class PostCollectorWrapper(Boost.Python.instance):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @classmethod
    def __getitem__(cls, index):
        """
        __getitem__( (PostCollectorWrapper)arg1, (int)arg2) -> Posting"""
    @classmethod
    def __iter__(cls):
        """
        __iter__( (object)arg1) -> object"""
    @classmethod
    def __len__(cls) -> int:
        """
        __len__( (PostCollectorWrapper)arg1) -> int"""
    @classmethod
    def __reduce__(cls): ...

class PostHandler(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def __reduce__(cls): ...

class Posting(JournalItem):
    __instance_size__: ClassVar[int] = ...
    account: Incomplete
    amount: Incomplete
    assigned_amount: Incomplete
    cost: Incomplete
    given_cost: Incomplete
    xact: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def clear_xdata(cls, *args, **kwargs):
        """
        clear_xdata( (Posting)arg1) -> None"""
    @classmethod
    def get_tag(cls, *args, **kwargs):
        """
        get_tag( (Posting)arg1, (str)arg2) -> object

        get_tag( (Posting)arg1, (object)arg2) -> object

        get_tag( (Posting)arg1, (object)arg2, (object)arg3) -> object"""
    @classmethod
    def has_tag(cls, *args, **kwargs):
        """
        has_tag( (Posting)arg1, (str)arg2) -> bool

        has_tag( (Posting)arg1, (object)arg2) -> bool

        has_tag( (Posting)arg1, (object)arg2, (object)arg3) -> bool"""
    @classmethod
    def has_xdata(cls, *args, **kwargs):
        """
        has_xdata( (Posting)arg1) -> bool"""
    @classmethod
    def id(cls, *args, **kwargs):
        """
        id( (Posting)arg1) -> str"""
    @classmethod
    def lookup(cls, *args, **kwargs):
        """
        lookup( (Posting)arg1, (object)arg2, (str)arg3) -> object"""
    @classmethod
    def must_balance(cls, *args, **kwargs):
        """
        must_balance( (Posting)arg1) -> bool"""
    @classmethod
    def reported_account(cls, *args, **kwargs):
        """
        reported_account( (Posting)arg1) -> Account"""
    @classmethod
    def seq(cls, *args, **kwargs):
        """
        seq( (Posting)arg1) -> int"""
    @classmethod
    def set_reported_account(cls, *args, **kwargs):
        """
        set_reported_account( (Posting)arg1, (Account)arg2) -> None"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (Posting)arg1) -> bool"""
    @classmethod
    def xdata(cls, *args, **kwargs):
        """
        xdata( (Posting)arg1) -> PostingXData"""
    @classmethod
    def __reduce__(cls): ...
    @property
    def aux_date(self): ...
    @property
    def date(self): ...

class PostingXData(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    account: Incomplete
    compound_value: Incomplete
    count: Incomplete
    date: Incomplete
    datetime: Incomplete
    flags: Incomplete
    sort_values: Incomplete
    total: Incomplete
    visited_value: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def add_flags(cls, *args, **kwargs):
        """
        add_flags( (PostingXData)arg1, (int)arg2) -> None"""
    @classmethod
    def clear_flags(cls, *args, **kwargs):
        """
        clear_flags( (PostingXData)arg1) -> None"""
    @classmethod
    def drop_flags(cls, *args, **kwargs):
        """
        drop_flags( (PostingXData)arg1, (int)arg2) -> None"""
    @classmethod
    def has_flags(cls, *args, **kwargs):
        """
        has_flags( (PostingXData)arg1, (int)arg2) -> bool"""
    @classmethod
    def __reduce__(cls): ...

class Session(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def close_journal_files(cls, *args, **kwargs):
        """
        close_journal_files( (Session)arg1) -> None"""
    @classmethod
    def error_context(cls, *args, **kwargs):
        """
        error_context( (Session)arg1) -> object"""
    @classmethod
    def journal(cls, *args, **kwargs):
        """
        journal( (Session)arg1) -> Journal"""
    @classmethod
    def read_journal(cls, *args, **kwargs):
        """
        read_journal( (Session)arg1, (object)arg2) -> Journal"""
    @classmethod
    def read_journal_files(cls, *args, **kwargs):
        """
        read_journal_files( (Session)arg1) -> Journal"""
    @classmethod
    def read_journal_from_string(cls, *args, **kwargs):
        """
        read_journal_from_string( (Session)arg1, (str)arg2) -> Journal"""
    @classmethod
    def __reduce__(cls): ...

class State(Boost.Python.enum):
    Cleared: ClassVar[State] = ...
    Pending: ClassVar[State] = ...
    Uncleared: ClassVar[State] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class SupportFlags16(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    flags: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (SupportFlags16)arg2) -> None

        __init__( (object)arg1, (int)arg2) -> None"""
    @classmethod
    def add_flags(cls, *args, **kwargs):
        """
        add_flags( (SupportFlags16)arg1, (int)arg2) -> None"""
    @classmethod
    def clear_flags(cls, *args, **kwargs):
        """
        clear_flags( (SupportFlags16)arg1) -> None"""
    @classmethod
    def drop_flags(cls, *args, **kwargs):
        """
        drop_flags( (SupportFlags16)arg1, (int)arg2) -> None"""
    @classmethod
    def has_flags(cls, *args, **kwargs):
        """
        has_flags( (SupportFlags16)arg1, (int)arg2) -> bool"""
    @classmethod
    def __reduce__(cls): ...

class SupportFlags8(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    flags: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (SupportFlags8)arg2) -> None

        __init__( (object)arg1, (int)arg2) -> None"""
    @classmethod
    def add_flags(cls, *args, **kwargs):
        """
        add_flags( (SupportFlags8)arg1, (int)arg2) -> None"""
    @classmethod
    def clear_flags(cls, *args, **kwargs):
        """
        clear_flags( (SupportFlags8)arg1) -> None"""
    @classmethod
    def drop_flags(cls, *args, **kwargs):
        """
        drop_flags( (SupportFlags8)arg1, (int)arg2) -> None"""
    @classmethod
    def has_flags(cls, *args, **kwargs):
        """
        has_flags( (SupportFlags8)arg1, (int)arg2) -> bool"""
    @classmethod
    def __reduce__(cls): ...

class Transaction(TransactionBase):
    __instance_size__: ClassVar[int] = ...
    code: Incomplete
    payee: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None"""
    @classmethod
    def add_post(cls, *args, **kwargs):
        """
        add_post( (Transaction)arg1, (Posting)arg2) -> None"""
    @classmethod
    def clear_xdata(cls, *args, **kwargs):
        """
        clear_xdata( (Transaction)arg1) -> None"""
    @classmethod
    def has_xdata(cls, *args, **kwargs):
        """
        has_xdata( (Transaction)arg1) -> bool"""
    @classmethod
    def id(cls, *args, **kwargs):
        """
        id( (Transaction)arg1) -> str"""
    @classmethod
    def lookup(cls, *args, **kwargs):
        """
        lookup( (Transaction)arg1, (object)arg2, (str)arg3) -> object"""
    @classmethod
    def magnitude(cls, *args, **kwargs):
        """
        magnitude( (Transaction)arg1) -> Value"""
    @classmethod
    def seq(cls, *args, **kwargs):
        """
        seq( (Transaction)arg1) -> int"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (Transaction)arg1) -> bool"""
    @classmethod
    def __reduce__(cls): ...

class TransactionBase(JournalItem):
    journal: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Raises an exception
        This class cannot be instantiated from Python
        """
    @classmethod
    def add_post(cls, *args, **kwargs):
        """
        add_post( (TransactionBase)arg1, (Posting)arg2) -> None"""
    @classmethod
    def finalize(cls, *args, **kwargs):
        """
        finalize( (TransactionBase)arg1) -> bool"""
    @classmethod
    def posts(cls, *args, **kwargs):
        """
        posts( (object)arg1) -> object"""
    @classmethod
    def remove_post(cls, *args, **kwargs):
        """
        remove_post( (TransactionBase)arg1, (Posting)arg2) -> bool"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (TransactionBase)arg1) -> bool"""
    @classmethod
    def __getitem__(cls, index):
        """
        __getitem__( (TransactionBase)arg1, (int)arg2) -> Posting"""
    @classmethod
    def __iter__(cls):
        """
        __iter__( (object)arg1) -> object"""
    @classmethod
    def __len__(cls) -> int:
        """
        __len__( (TransactionBase)arg1) -> int"""
    @classmethod
    def __reduce__(cls): ...

class Value(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (bool)arg2) -> None

        __init__( (object)arg1, (object)arg2) -> None

        __init__( (object)arg1, (object)arg2) -> None

        __init__( (object)arg1, (int)arg2) -> None

        __init__( (object)arg1, (float)arg2) -> None

        __init__( (object)arg1, (Amount)arg2) -> None

        __init__( (object)arg1, (Balance)arg2) -> None

        __init__( (object)arg1, (object)arg2) -> None

        __init__( (object)arg1, (str)arg2) -> None

        __init__( (object)arg1, (Value)arg2) -> None"""
    @classmethod
    def abs(cls, *args, **kwargs):
        """
        abs( (Value)arg1) -> Value"""
    @classmethod
    def annotate(cls, *args, **kwargs):
        """
        annotate( (Value)arg1, (Annotation)arg2) -> None"""
    @classmethod
    def basetype(cls, *args, **kwargs):
        """
        basetype( (Value)arg1) -> object"""
    @classmethod
    def casted(cls, *args, **kwargs):
        """
        casted( (Value)arg1, (ValueType)arg2) -> Value"""
    @classmethod
    def exchange_commodities(cls, *args, **kwargs):
        """
        exchange_commodities( (Value)arg1, (str)arg2 [, (bool)arg3]) -> Value"""
    @classmethod
    def floored(cls, *args, **kwargs):
        """
        floored( (Value)arg1) -> Value"""
    @classmethod
    def has_annotation(cls, *args, **kwargs):
        """
        has_annotation( (Value)arg1) -> bool"""
    @classmethod
    def in_place_cast(cls, *args, **kwargs):
        """
        in_place_cast( (Value)arg1, (ValueType)arg2) -> None"""
    @classmethod
    def in_place_floor(cls, *args, **kwargs):
        """
        in_place_floor( (Value)arg1) -> None"""
    @classmethod
    def in_place_negate(cls, *args, **kwargs):
        """
        in_place_negate( (Value)arg1) -> None"""
    @classmethod
    def in_place_not(cls, *args, **kwargs):
        """
        in_place_not( (Value)arg1) -> None"""
    @classmethod
    def in_place_reduce(cls, *args, **kwargs):
        """
        in_place_reduce( (Value)arg1) -> None"""
    @classmethod
    def in_place_round(cls, *args, **kwargs):
        """
        in_place_round( (Value)arg1) -> None"""
    @classmethod
    def in_place_simplify(cls, *args, **kwargs):
        """
        in_place_simplify( (Value)arg1) -> None"""
    @classmethod
    def in_place_truncate(cls, *args, **kwargs):
        """
        in_place_truncate( (Value)arg1) -> None"""
    @classmethod
    def in_place_unreduce(cls, *args, **kwargs):
        """
        in_place_unreduce( (Value)arg1) -> None"""
    @classmethod
    def in_place_unround(cls, *args, **kwargs):
        """
        in_place_unround( (Value)arg1) -> None"""
    @classmethod
    def initialize(cls) -> None:
        """
        initialize() -> None"""
    @classmethod
    def is_amount(cls, *args, **kwargs):
        """
        is_amount( (Value)arg1) -> bool

        is_amount( (Value)arg1) -> bool"""
    @classmethod
    def is_balance(cls, *args, **kwargs):
        """
        is_balance( (Value)arg1) -> bool

        is_balance( (Value)arg1) -> bool"""
    @classmethod
    def is_boolean(cls, *args, **kwargs):
        """
        is_boolean( (Value)arg1) -> bool"""
    @classmethod
    def is_date(cls, *args, **kwargs):
        """
        is_date( (Value)arg1) -> bool"""
    @classmethod
    def is_datetime(cls, *args, **kwargs):
        """
        is_datetime( (Value)arg1) -> bool"""
    @classmethod
    def is_equal_to(cls, *args, **kwargs):
        """
        is_equal_to( (Value)arg1, (Value)arg2) -> bool"""
    @classmethod
    def is_greater_than(cls, *args, **kwargs):
        """
        is_greater_than( (Value)arg1, (Value)arg2) -> bool"""
    @classmethod
    def is_less_than(cls, *args, **kwargs):
        """
        is_less_than( (Value)arg1, (Value)arg2) -> bool"""
    @classmethod
    def is_long(cls, *args, **kwargs):
        """
        is_long( (Value)arg1) -> bool"""
    @classmethod
    def is_mask(cls, *args, **kwargs):
        """
        is_mask( (Value)arg1) -> bool

        is_mask( (Value)arg1) -> bool"""
    @classmethod
    def is_nonzero(cls, *args, **kwargs):
        """
        is_nonzero( (Value)arg1) -> bool"""
    @classmethod
    def is_null(cls, *args, **kwargs):
        """
        is_null( (Value)arg1) -> bool"""
    @classmethod
    def is_realzero(cls, *args, **kwargs):
        """
        is_realzero( (Value)arg1) -> bool"""
    @classmethod
    def is_sequence(cls, *args, **kwargs):
        """
        is_sequence( (Value)arg1) -> bool"""
    @classmethod
    def is_string(cls, *args, **kwargs):
        """
        is_string( (Value)arg1) -> bool"""
    @classmethod
    def is_type(cls, *args, **kwargs):
        """
        is_type( (Value)arg1, (ValueType)arg2) -> bool"""
    @classmethod
    def is_zero(cls, *args, **kwargs):
        """
        is_zero( (Value)arg1) -> bool"""
    @classmethod
    def label(cls, *args, **kwargs):
        """
        label( (Value)arg1, (object)arg2) -> str"""
    @classmethod
    def negated(cls, *args, **kwargs):
        """
        negated( (Value)arg1) -> Value"""
    @classmethod
    def number(cls, *args, **kwargs):
        """
        number( (Value)arg1) -> Value"""
    @classmethod
    def pop_back(cls, *args, **kwargs):
        """
        pop_back( (Value)arg1) -> None"""
    @classmethod
    def push_back(cls, *args, **kwargs):
        """
        push_back( (Value)arg1, (Value)arg2) -> None"""
    @classmethod
    def reduced(cls, *args, **kwargs):
        """
        reduced( (Value)arg1) -> Value"""
    @classmethod
    def rounded(cls, *args, **kwargs):
        """
        rounded( (Value)arg1) -> Value"""
    @classmethod
    def set_boolean(cls, *args, **kwargs):
        """
        set_boolean( (Value)arg1, (bool)arg2) -> None"""
    @classmethod
    def set_date(cls, *args, **kwargs):
        """
        set_date( (Value)arg1, (object)arg2) -> None"""
    @classmethod
    def set_datetime(cls, *args, **kwargs):
        """
        set_datetime( (Value)arg1, (object)arg2) -> None"""
    @classmethod
    def set_long(cls, *args, **kwargs):
        """
        set_long( (Value)arg1, (int)arg2) -> None"""
    @classmethod
    def set_sequence(cls, *args, **kwargs):
        """
        set_sequence( (Value)arg1, (object)arg2) -> None"""
    @classmethod
    def set_string(cls, *args, **kwargs):
        """
        set_string( (Value)arg1, (str)arg2) -> None"""
    @classmethod
    def shutdown(cls) -> None:
        """
        shutdown() -> None"""
    @classmethod
    def simplified(cls, *args, **kwargs):
        """
        simplified( (Value)arg1) -> Value"""
    @classmethod
    def size(cls, *args, **kwargs):
        """
        size( (Value)arg1) -> int"""
    @classmethod
    def strip_annotations(cls, *args, **kwargs):
        """
        strip_annotations( (Value)arg1) -> Value

        strip_annotations( (Value)arg1, (KeepDetails)arg2) -> Value"""
    @classmethod
    def to_amount(cls, *args, **kwargs):
        """
        to_amount( (Value)arg1) -> Amount"""
    @classmethod
    def to_balance(cls, *args, **kwargs):
        """
        to_balance( (Value)arg1) -> Balance"""
    @classmethod
    def to_boolean(cls, *args, **kwargs):
        """
        to_boolean( (Value)arg1) -> bool"""
    @classmethod
    def to_date(cls, *args, **kwargs):
        """
        to_date( (Value)arg1) -> object"""
    @classmethod
    def to_datetime(cls, *args, **kwargs):
        """
        to_datetime( (Value)arg1) -> object"""
    @classmethod
    def to_long(cls, *args, **kwargs):
        """
        to_long( (Value)arg1) -> int"""
    @classmethod
    def to_mask(cls, *args, **kwargs):
        """
        to_mask( (Value)arg1) -> object"""
    @classmethod
    def to_sequence(cls, *args, **kwargs):
        """
        to_sequence( (Value)arg1) -> object"""
    @classmethod
    def to_string(cls, *args, **kwargs):
        """
        to_string( (Value)arg1) -> str"""
    @classmethod
    def truncated(cls, *args, **kwargs):
        """
        truncated( (Value)arg1) -> Value"""
    @classmethod
    def type(cls, *args, **kwargs):
        """
        type( (Value)arg1) -> ValueType"""
    @classmethod
    def unreduced(cls, *args, **kwargs):
        """
        unreduced( (Value)arg1) -> Value"""
    @classmethod
    def unrounded(cls, *args, **kwargs):
        """
        unrounded( (Value)arg1) -> Value"""
    @classmethod
    def valid(cls, *args, **kwargs):
        """
        valid( (Value)arg1) -> bool"""
    @classmethod
    def value(cls, *args, **kwargs):
        """
        value( (Value)arg1) -> object

        value( (Value)arg1, (Commodity)in_terms_of) -> object

        value( (Value)arg1, (Commodity)in_terms_of, (object)moment) -> object

        value( (Value)arg1, (Commodity)in_terms_of, (object)moment) -> object"""
    @classmethod
    def __abs__(cls):
        """
        __abs__( (Value)arg1) -> Value"""
    @classmethod
    def __add__(cls, other):
        """
        __add__( (Value)arg1, (Value)arg2) -> object

        __add__( (Value)arg1, (int)arg2) -> object

        __add__( (Value)arg1, (Amount)arg2) -> object

        __add__( (Value)arg1, (Balance)arg2) -> object"""
    @classmethod
    def __bool__(cls) -> bool:
        """
        __bool__( (Value)arg1) -> object"""
    @classmethod
    def __eq__(cls, other: object) -> bool:
        """
        __eq__( (Value)arg1, (Value)arg2) -> object

        __eq__( (Value)arg1, (int)arg2) -> object

        __eq__( (Value)arg1, (int)arg2) -> object

        __eq__( (Value)arg1, (Amount)arg2) -> object

        __eq__( (Value)arg1, (Amount)arg2) -> object

        __eq__( (Value)arg1, (Balance)arg2) -> object

        __eq__( (Value)arg1, (Balance)arg2) -> object"""
    @classmethod
    def __ge__(cls, other: object) -> bool:
        """
        __ge__( (Value)arg1, (int)arg2) -> object

        __ge__( (Value)arg1, (Amount)arg2) -> object

        __ge__( (Value)arg1, (Value)arg2) -> object

        __ge__( (Value)arg1, (int)arg2) -> object

        __ge__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __gt__(cls, other: object) -> bool:
        """
        __gt__( (Value)arg1, (int)arg2) -> object

        __gt__( (Value)arg1, (Amount)arg2) -> object

        __gt__( (Value)arg1, (Value)arg2) -> object

        __gt__( (Value)arg1, (int)arg2) -> object

        __gt__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __iadd__(cls, other):
        """
        __iadd__( (object)arg1, (Value)arg2) -> object

        __iadd__( (object)arg1, (int)arg2) -> object

        __iadd__( (object)arg1, (Amount)arg2) -> object

        __iadd__( (object)arg1, (Balance)arg2) -> object"""
    @classmethod
    def __idiv__(cls, *args, **kwargs):
        """
        __idiv__( (object)arg1, (Value)arg2) -> object

        __idiv__( (object)arg1, (int)arg2) -> object

        __idiv__( (object)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __imul__(cls, other):
        """
        __imul__( (object)arg1, (Value)arg2) -> object

        __imul__( (object)arg1, (int)arg2) -> object

        __imul__( (object)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __int__(cls) -> int:
        """
        __int__( (Value)arg1) -> int"""
    @classmethod
    def __isub__(cls, other):
        """
        __isub__( (object)arg1, (Value)arg2) -> object

        __isub__( (object)arg1, (int)arg2) -> object

        __isub__( (object)arg1, (Amount)arg2) -> object

        __isub__( (object)arg1, (Balance)arg2) -> object"""
    @classmethod
    def __le__(cls, other: object) -> bool:
        """
        __le__( (Value)arg1, (Value)arg2) -> object

        __le__( (Value)arg1, (int)arg2) -> object

        __le__( (Value)arg1, (Amount)arg2) -> object

        __le__( (Value)arg1, (int)arg2) -> object

        __le__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __lt__(cls, other: object) -> bool:
        """
        __lt__( (Value)arg1, (Value)arg2) -> object

        __lt__( (Value)arg1, (int)arg2) -> object

        __lt__( (Value)arg1, (Amount)arg2) -> object

        __lt__( (Value)arg1, (int)arg2) -> object

        __lt__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __mul__(cls, other):
        """
        __mul__( (Value)arg1, (Value)arg2) -> object

        __mul__( (Value)arg1, (int)arg2) -> object

        __mul__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __ne__(cls, other: object) -> bool:
        """
        __ne__( (Value)arg1, (Value)arg2) -> object

        __ne__( (Value)arg1, (int)arg2) -> object

        __ne__( (Value)arg1, (int)arg2) -> object

        __ne__( (Value)arg1, (Amount)arg2) -> object

        __ne__( (Value)arg1, (Amount)arg2) -> object

        __ne__( (Value)arg1, (Balance)arg2) -> object

        __ne__( (Value)arg1, (Balance)arg2) -> object"""
    @classmethod
    def __neg__(cls):
        """
        __neg__( (Value)arg1) -> object"""
    @classmethod
    def __nonzero__(cls, *args, **kwargs):
        """
        __nonzero__( (Value)arg1) -> bool"""
    @classmethod
    def __radd__(cls, other):
        """
        __radd__( (Value)arg1, (int)arg2) -> object

        __radd__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __rmul__(cls, other):
        """
        __rmul__( (Value)arg1, (int)arg2) -> object

        __rmul__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __rsub__(cls, other):
        """
        __rsub__( (Value)arg1, (int)arg2) -> object

        __rsub__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __rtruediv__(cls, other):
        """
        __rtruediv__( (Value)arg1, (int)arg2) -> object

        __rtruediv__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __sub__(cls, other):
        """
        __sub__( (Value)arg1, (Value)arg2) -> object

        __sub__( (Value)arg1, (int)arg2) -> object

        __sub__( (Value)arg1, (Amount)arg2) -> object

        __sub__( (Value)arg1, (Balance)arg2) -> object"""
    @classmethod
    def __truediv__(cls, other):
        """
        __truediv__( (Value)arg1, (Value)arg2) -> object

        __truediv__( (Value)arg1, (int)arg2) -> object

        __truediv__( (Value)arg1, (Amount)arg2) -> object"""
    @classmethod
    def __unicode__(cls, *args, **kwargs):
        """
        __unicode__( (Value)arg1) -> object"""
    @property
    def annotation(self): ...

class ValueType(Boost.Python.enum):
    Amount: ClassVar[ValueType] = ...
    Balance: ClassVar[ValueType] = ...
    Boolean: ClassVar[ValueType] = ...
    Date: ClassVar[ValueType] = ...
    DateTime: ClassVar[ValueType] = ...
    Integer: ClassVar[ValueType] = ...
    Scope: ClassVar[ValueType] = ...
    Sequence: ClassVar[ValueType] = ...
    String: ClassVar[ValueType] = ...
    Void: ClassVar[ValueType] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

def close_journal_files(*args, **kwargs): ...
def mask_value(*args, **kwargs): ...
def parse_date(*args, **kwargs): ...
def parse_datetime(*args, **kwargs): ...
def read_journal(*args, **kwargs): ...
def read_journal_from_string(*args, **kwargs): ...
def string_value(*args, **kwargs): ...
def times_initialize(*args, **kwargs): ...
def times_shutdown(*args, **kwargs): ...
def value_context(*args, **kwargs): ...
