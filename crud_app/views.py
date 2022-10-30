from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework.views import APIView
from django.http import JsonResponse

class BookAPI(APIView):
	def get(self, request):
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return JsonResponse({
			"books": serializer.data
		}, safe=False)

	def post(self, request):
		Authors = request.data.get("Authors")
		Name = request.data.get("Name")
		Category = request.data.get("Category")
		data ={
			"Authors": Authors,
			"Name": Name,
			"Category": Category
		}
		serializer = BookSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse({
				"message":"Book created successfully"
			})
		return JsonResponse({
			"message":serializer.error_messages
		})

class BookAPI_id(APIView):
	def delete(self, request, bookID):
		try:
			book = Book.objects.get(id=bookID)
		except Book.DoesNotExist as e:
			return JsonResponse({
				"message":"Book with this ID does not exist"
			})
		book.delete()
		return JsonResponse({
			"message":"Book deleted  successfully"
			})

	def patch(self, request, bookID):
		Authors = request.data.get("Authors")
		Name = request.data.get("Name")
		Category = request.data.get("Category")
		data ={
			"Authors": Authors,
			"Name": Name,
			"Category": Category
		}
		try:
			book = Book.objects.get(id=bookID)
		except Book.DoesNotExist as e:
			return JsonResponse({
				"message":"Book with this ID does not exist"
			})

		serializer = BookSerializer(instance=book, data=data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse({
		    	"message":"Book updated successfully"
			})
		return JsonResponse({
			"message":serializer.error_messages
		})