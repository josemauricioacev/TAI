<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Consulta de Usuarios</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .editando input {
            background-color: #ffffcc;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center text-primary">Consulta de Usuarios - FastAPI</h1>

        @if(session('success'))
            <div class="alert alert-success">{{ session('success') }}</div>
        @elseif(session('error'))
            <div class="alert alert-danger">{{ session('error') }}</div>
        @endif

        <table class="table table-striped mt-4">
            <thead class="table-dark">
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Edad</th>
                    <th>Correo</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                @foreach($usuarios as $usuario)
                <tr id="fila-{{ $usuario['id'] }}">
                    <form action="{{ route('usuario.update', $usuario['id']) }}" method="POST">
                        @csrf
                        @method('PUT')
                        <td>{{ $usuario['id'] }}</td>
                        <td>
                            <input type="text" name="name" value="{{ $usuario['name'] }}" class="form-control" disabled>
                        </td>
                        <td>
                            <input type="number" name="age" value="{{ $usuario['age'] }}" class="form-control" disabled>
                        </td>
                        <td>
                            <input type="email" name="email" value="{{ $usuario['email'] }}" class="form-control" disabled>
                        </td>
                        <td>
                            <button type="button" class="btn btn-warning btn-sm" onclick="habilitarEdicion({{ $usuario['id'] }})" id="btn-edit-{{ $usuario['id'] }}">Editar</button>
                            <button type="submit" class="btn btn-success btn-sm d-none" id="btn-save-{{ $usuario['id'] }}">Guardar</button>
                        </td>
                    </form>

                    <form action="{{ route('usuario.destroy', $usuario['id']) }}" method="POST" class="d-inline">
                        @csrf
                        @method('DELETE')
                        <td>
                            <button type="submit" class="btn btn-danger btn-sm">Eliminar</button>
                        </td>
                    </form>
                </tr>
                @endforeach
            </tbody>
        </table>

        <a href="{{ route('usuario.inicio') }}" class="btn btn-primary mt-3">Registrar nuevo usuario</a>
    </div>

    <script>
        function habilitarEdicion(id) {
            const fila = document.getElementById(`fila-${id}`);
            const inputs = fila.querySelectorAll('input');
            const btnEdit = document.getElementById(`btn-edit-${id}`);
            const btnSave = document.getElementById(`btn-save-${id}`);

            inputs.forEach(input => {
                input.disabled = false;
                input.classList.add('editando');
            });

            btnEdit.classList.add('d-none');
            btnSave.classList.remove('d-none');
        }
    </script>
</body>
</html>
