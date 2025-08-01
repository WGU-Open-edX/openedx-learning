"""
This is the public API for content authoring in Learning Core.

This is the single ``api`` module that code outside of the
``openedx_learning.apps.authoring.*`` package should import from. It will
re-export the public functions from all api.py modules of all authoring apps. It
may also implement its own convenience APIs that wrap calls to multiple app
APIs.
"""
# These wildcard imports are okay because these api modules declare __all__.
# pylint: disable=wildcard-import
from ..apps.authoring.backup_restore.api import *
from ..apps.authoring.collections.api import *
from ..apps.authoring.components.api import *
from ..apps.authoring.contents.api import *
from ..apps.authoring.publishing.api import *
from ..apps.authoring.sections.api import *
from ..apps.authoring.subsections.api import *
from ..apps.authoring.units.api import *

# This was renamed after the authoring API refactoring pushed this and other
# app APIs into the openedx_learning.api.authoring module. Here I'm aliasing to
# it's previous name, to make migration a little easier.
create_next_version = create_next_component_version
