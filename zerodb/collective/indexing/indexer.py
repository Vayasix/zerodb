from zope.interface import implements
from zerodb.collective.indexing.interfaces import IIndexQueueProcessor


class IPortalCatalogQueueProcessor(IIndexQueueProcessor):
    """ an index queue processor for the standard portal catalog via
        the `CatalogMultiplex` and `CMFCatalogAware` mixin classes """


class PortalCatalogProcessor(object):
    implements(IPortalCatalogQueueProcessor)

    def index(self, obj, attributes=None):
        #index(obj, attributes)
        pass

    def reindex(self, obj, attributes=None):
        #reindex(obj, attributes)
        pass

    def unindex(self, obj):
        #unindex(obj)
        pass

    def begin(self):
        pass

    def commit(self):
        pass

    def abort(self):
        pass
