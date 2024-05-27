from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.http import HttpResponseForbidden
from .repositories import UserRepository
from weather_project.settings import SECRET_KEY
import jwt
import json
import bcrypt

@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        user = UserRepository().create_user(email,username, password)

        if user:
            return JsonResponse({'message': 'User created successfully'})
        else:
            return JsonResponse({'message': 'User creation failed'}, status=400)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')

        
        user_data = UserRepository().get_user_by_email(email)

        if user_data:
            stored_password = user_data.get('password')
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                payload = {
                    'email': email,
                    'exp': datetime.utcnow() + timedelta(minutes=5)  # Token expiration time
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                return JsonResponse({'token': token})
        
        return HttpResponseForbidden('Invalid credentials')
    
@csrf_exempt
def user_delete(request):
    if request.method == 'DELETE':
        token = request.headers.get('Authorization').split(' ')[1] 

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            email = payload['email']
            user_repo = UserRepository()
            user_data = user_repo.get_user_by_email(email)
            
            if user_data:
                # Remover o usuário
                user_repo.delete_user(email)
                return JsonResponse({'message': 'User deleted successfully'})
            else:
                return HttpResponseForbidden('User not found')
        except jwt.ExpiredSignatureError:
            return HttpResponseForbidden('Token expired')
        except jwt.InvalidTokenError:
            return HttpResponseForbidden('Invalid token')

@csrf_exempt
def user_update(request):
    if request.method == 'PUT':
        token = request.headers.get('Authorization').split(' ')[1] 

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            email = payload['email']
            user_repo = UserRepository()
            user_data = user_repo.get_user_by_email(email)
            
            if user_data:
                data = json.loads(request.body.decode('utf-8'))
                new_username = data.get('username')
                new_password = data.get('password')

                if new_username:
                    user_data['username'] = new_username
                if new_password:
                    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                    user_data['password'] = hashed_password.decode('utf-8')

                # Atualizar os dados do usuário
                user_repo.update_user(email, user_data)
                return JsonResponse({'message': 'User updated successfully'})
            else:
                return HttpResponseForbidden('User not found')
        except jwt.ExpiredSignatureError:
            return HttpResponseForbidden('Token expired')
        except jwt.InvalidTokenError:
            return HttpResponseForbidden('Invalid token')
        

def user_info(request):
    if request.method == 'GET':
        token = request.headers.get('Authorization').split(' ')[1] 

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            email = payload['email']
            user_data = UserRepository().get_user_by_email(email)
            
            if user_data:
                # Converter ObjectId para string antes de serializar em JSON
                user_data['_id'] = str(user_data['_id'])
                return JsonResponse(user_data)
            else:
                return HttpResponseForbidden('User not found')
        except jwt.ExpiredSignatureError:
            return HttpResponseForbidden('Token expired')
        except jwt.InvalidTokenError:
            return HttpResponseForbidden('Invalid token')