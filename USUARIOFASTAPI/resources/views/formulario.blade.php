<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Usuarios</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
</head>

<body>
    <div class="container mt-5">
        <form action="{{ route('usuario.store') }}" method="POST">
            @csrf
            
            <h1 class="display-1 text-center text-primary">Registro de Usuario</h1>
            <h3 class="display-3 mb-5 text-center text-danger">FastAPI</h3>

            <div class="container">

            @if(session('success'))
                <div class="alert alert-success">{{ session('success') }}</div>
            @endif
            
            @if(session('error'))
                <div class="alert alert-danger">{{ session('error') }}</div>
            @endif
            
            <p class="text-center">
                <a href="{{ route('usuario.index') }}">Consultar Usuarios</a>
            </p>
            
            <div class="mb-3">
                <label for="usuario" class="form-label">Nombre:</label>
                <input type="text" name="txtNombre" class="form-control" aria-describedby="emailHelp">
            </div>
            
            <div class="mb-3">
                <label for="edad" class="form-label">Edad:</label>
                <input type="number" name="txtEdad" class="form-control" aria-describedby="emailHelp">
            </div>
            
            <div class="mb-3">
                <label for="correo" class="form-label">Correo:</label>
                <input type="text" name="txtCorreo" class="form-control" aria-describedby="emailHelp">
            </div>
            
            <button type="submit" class="btn btn-primary">Guardar</button>
        </form>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
</body>

</html>