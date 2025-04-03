<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Usuarios</title>
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
         crossorigin="anonymous">
</head>

<body>
    <form action="{{ route('usuario.store') }}" method="POST">
        @csrf

        <h1 class="display-1 mt-5 text-center text-primary">Consulta de Usuarios</h1>
        <h3 class="display-3 mb-5 text-center text-danger">FastAPI</h3>

        <div class="container">
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">Id:</th>
                        <th scope="col">Nombre:</th>
                        <th scope="col">Edad:</th>
                        <th scope="col">Correo:</th>
                    </tr>
                </thead>
                <tbody>
                    @foreach($usuarios as $usuario)
                    <tr>
                        <th scope="row">{{ $usuario['id'] }}</th>
                        <td>{{ $usuario['name'] }}</td>
                        <td>{{ $usuario['age'] }}</td>
                        <td>{{ $usuario['email'] }}</td>
                    </tr>
                    @endforeach
                </tbody>
            </table>
        </div> <!-- Cierre del container -->
    </form>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
         crossorigin="anonymous"></script>
</body>

</html>
