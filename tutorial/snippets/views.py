## Replacement of UserList and UserDetail
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides `list` and `retrieve` actions.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


## Replacement of SnippetList, SnippetDetail and SnippetHighlight
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

class SnippetViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	Additionally we also provide an extra `highlight` action.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

