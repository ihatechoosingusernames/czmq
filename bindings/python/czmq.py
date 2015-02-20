################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Please refer to the README for information about making permanent changes.  #
################################################################################

from ctypes import *
from ctypes.util import find_library

libpath = find_library("czmq")
if not libpath:
    raise ImportError("Unable to find czmq C library")
lib = cdll.LoadLibrary(libpath)

class zhash_t(Structure):
    pass # Empty - only for type checking
zhash_p = POINTER(zhash_t)

class zlist_t(Structure):
    pass # Empty - only for type checking
zlist_p = POINTER(zlist_t)

class zframe_t(Structure):
    pass # Empty - only for type checking
zframe_p = POINTER(zframe_t)


# zhash
zhash_free_fn = CFUNCTYPE(None, c_void_p)
zhash_foreach_fn = CFUNCTYPE(c_int, c_char_p, c_void_p, c_void_p)
lib.zhash_new.restype = zhash_p
lib.zhash_new.argtypes = []
lib.zhash_destroy.restype = None
lib.zhash_destroy.argtypes = [POINTER(zhash_p)]
lib.zhash_insert.restype = c_int
lib.zhash_insert.argtypes = [zhash_p, c_char_p, c_void_p]
lib.zhash_update.restype = None
lib.zhash_update.argtypes = [zhash_p, c_char_p, c_void_p]
lib.zhash_delete.restype = None
lib.zhash_delete.argtypes = [zhash_p, c_char_p]
lib.zhash_lookup.restype = c_void_p
lib.zhash_lookup.argtypes = [zhash_p, c_char_p]
lib.zhash_rename.restype = c_int
lib.zhash_rename.argtypes = [zhash_p, c_char_p, c_char_p]
lib.zhash_freefn.restype = c_void_p
lib.zhash_freefn.argtypes = [zhash_p, c_char_p, zhash_free_fn]
lib.zhash_size.restype = c_size_t
lib.zhash_size.argtypes = [zhash_p]
lib.zhash_dup.restype = zhash_p
lib.zhash_dup.argtypes = [zhash_p]
lib.zhash_keys.restype = zlist_p
lib.zhash_keys.argtypes = [zhash_p]
lib.zhash_first.restype = c_void_p
lib.zhash_first.argtypes = [zhash_p]
lib.zhash_next.restype = c_void_p
lib.zhash_next.argtypes = [zhash_p]
lib.zhash_cursor.restype = c_char_p
lib.zhash_cursor.argtypes = [zhash_p]
lib.zhash_comment.restype = None
lib.zhash_comment.argtypes = [zhash_p, c_char_p]
lib.zhash_pack.restype = zframe_p
lib.zhash_pack.argtypes = [zhash_p]
lib.zhash_unpack.restype = zhash_p
lib.zhash_unpack.argtypes = [zframe_p]
lib.zhash_save.restype = c_int
lib.zhash_save.argtypes = [zhash_p, c_char_p]
lib.zhash_load.restype = c_int
lib.zhash_load.argtypes = [zhash_p, c_char_p]
lib.zhash_refresh.restype = c_int
lib.zhash_refresh.argtypes = [zhash_p]
lib.zhash_autofree.restype = None
lib.zhash_autofree.argtypes = [zhash_p]
lib.zhash_foreach.restype = c_int
lib.zhash_foreach.argtypes = [zhash_p, zhash_foreach_fn, c_void_p]
lib.zhash_test.restype = None
lib.zhash_test.argtypes = [c_int]

class Zhash(object):
    """generic type-free hash container (simple)"""

    def __init__(self, *args):
        """Create a new, empty hash container"""
        if len(args) == 1 and isinstance(args[0], zhash_p):
            self._as_parameter_ = args[0] # Conversion from raw type to binding
        else:
            self._as_parameter_ = lib.zhash_new(*args) # Creation of new raw type

    def __del__(self):
        """Destroy a hash container and all items in it"""
        lib.zhash_destroy(byref(self._as_parameter_))

    def insert(self, key, item):
        """Insert item into hash table with specified key and item.
If key is already present returns -1 and leaves existing item unchanged
Returns 0 on success."""
        return lib.zhash_insert(self._as_parameter_, key, item)

    def update(self, key, item):
        """Update item into hash table with specified key and item.
If key is already present, destroys old item and inserts new one.
Use free_fn method to ensure deallocator is properly called on item."""
        return lib.zhash_update(self._as_parameter_, key, item)

    def delete(self, key):
        """Remove an item specified by key from the hash table. If there was no such
item, this function does nothing."""
        return lib.zhash_delete(self._as_parameter_, key)

    def lookup(self, key):
        """Return the item at the specified key, or null"""
        return lib.zhash_lookup(self._as_parameter_, key)

    def rename(self, old_key, new_key):
        """Reindexes an item from an old key to a new key. If there was no such
item, does nothing. Returns 0 if successful, else -1."""
        return lib.zhash_rename(self._as_parameter_, old_key, new_key)

    def freefn(self, key, free_fn):
        """Set a free function for the specified hash table item. When the item is
destroyed, the free function, if any, is called on that item.
Use this when hash items are dynamically allocated, to ensure that
you don't have memory leaks. You can pass 'free' or NULL as a free_fn.
Returns the item, or NULL if there is no such item."""
        return lib.zhash_freefn(self._as_parameter_, key, free_fn)

    def size(self):
        """Return the number of keys/items in the hash table"""
        return lib.zhash_size(self._as_parameter_)

    def dup(self):
        """Make copy of hash table; if supplied table is null, returns null.
Does not copy items themselves. Rebuilds new table so may be slow on
very large tables. NOTE: only works with item values that are strings
since there's no other way to know how to duplicate the item value."""
        return lib.zhash_dup(self._as_parameter_)

    def keys(self):
        """Return keys for items in table"""
        return lib.zhash_keys(self._as_parameter_)

    def first(self):
        """Simple iterator; returns first item in hash table, in no given order,
or NULL if the table is empty. This method is simpler to use than the
foreach() method, which is deprecated. To access the key for this item
use zhash_cursor(). NOTE: do NOT modify the table while iterating."""
        return lib.zhash_first(self._as_parameter_)

    def next(self):
        """Simple iterator; returns next item in hash table, in no given order,
or NULL if the last item was already returned. Use this together with
zhash_first() to process all items in a hash table. If you need the
items in sorted order, use zhash_keys() and then zlist_sort(). To
access the key for this item use zhash_cursor(). NOTE: do NOT modify
the table while iterating."""
        return lib.zhash_next(self._as_parameter_)

    def cursor(self):
        """After a successful first/next method, returns the key for the item that
was returned. This is a constant string that you may not modify or
deallocate, and which lasts as long as the item in the hash. After an
unsuccessful first/next, returns NULL."""
        return lib.zhash_cursor(self._as_parameter_)

    def comment(self, format, *args):
        """Add a comment to hash table before saving to disk. You can add as many
comment lines as you like. These comment lines are discarded when loading
the file. If you use a null format, all comments are deleted."""
        return lib.zhash_comment(self._as_parameter_, format, *args)

    def pack(self):
        """Serialize hash table to a binary frame that can be sent in a message.
The packed format is compatible with the 'dictionary' type defined in
http://rfc.zeromq.org/spec:35/FILEMQ, and implemented by zproto:

   ; A list of name/value pairs
   dictionary      = dict-count *( dict-name dict-value )
   dict-count      = number-4
   dict-value      = longstr
   dict-name       = string

   ; Strings are always length + text contents
   longstr         = number-4 *VCHAR
   string          = number-1 *VCHAR

   ; Numbers are unsigned integers in network byte order
   number-1        = 1OCTET
   number-4        = 4OCTET

Comments are not included in the packed data. Item values MUST be
strings."""
        return lib.zhash_pack(self._as_parameter_)

    @staticmethod
    def unpack(frame):
        """Unpack binary frame into a new hash table. Packed data must follow format
defined by zhash_pack. Hash table is set to autofree. An empty frame
unpacks to an empty hash table."""
        return lib.zhash_unpack(frame)

    def save(self, filename):
        """Save hash table to a text file in name=value format. Hash values must be
printable strings; keys may not contain '=' character. Returns 0 if OK,
else -1 if a file error occurred."""
        return lib.zhash_save(self._as_parameter_, filename)

    def load(self, filename):
        """Load hash table from a text file in name=value format; hash table must
already exist. Hash values must printable strings; keys may not contain
'=' character. Returns 0 if OK, else -1 if a file was not readable."""
        return lib.zhash_load(self._as_parameter_, filename)

    def refresh(self):
        """When a hash table was loaded from a file by zhash_load, this method will
reload the file if it has been modified since, and is "stable", i.e. not
still changing. Returns 0 if OK, -1 if there was an error reloading the 
file."""
        return lib.zhash_refresh(self._as_parameter_)

    def autofree(self):
        """Set hash for automatic value destruction"""
        return lib.zhash_autofree(self._as_parameter_)

    def foreach(self, callback, argument):
        """DEPRECATED as clumsy -- use zhash_first/_next instead
Apply function to each item in the hash table. Items are iterated in no
defined order. Stops if callback function returns non-zero and returns
final return code from callback function (zero = success).
Callback function for zhash_foreach method"""
        return lib.zhash_foreach(self._as_parameter_, callback, argument)

    @staticmethod
    def test(verbose):
        """Self test of this class"""
        return lib.zhash_test(verbose)

################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Please refer to the README for information about making permanent changes.  #
################################################################################