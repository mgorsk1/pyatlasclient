__version__ = '1.0.3'

# Set default logging handler to avoid "No handler found" warnings.
import logging
logging.getLogger('pyatlasclient').addHandler(logging.NullHandler())
