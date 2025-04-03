<?php

namespace App\Http\Controllers;

use App\Services\FastApiService;
use Illuminate\Http\Request;

class UserController extends Controller
{
    protected $fastApi;

    public function __construct(FastApiService $fastApi)
    {
        $this->fastApi = $fastApi;
    }

    public function inicio()
    {
        return view('formulario');
    }

    public function store(Request $request)
    {
        $usuarioNuevo = $request->validate([
            'txtNombre' => 'required',
            'txtEdad' => 'required',
            'txtCorreo' => 'required',
        ]);

        $usuarioNuevo = [
            'name' => $usuarioNuevo['txtNombre'],
            'age' => $usuarioNuevo['txtEdad'],
            'email' => $usuarioNuevo['txtCorreo'],
        ];

        try {
            $this->fastApi->post('/usuarios/', $usuarioNuevo);
            return redirect()->route('usuario.inicio')->with('success', 'Usuario guardado por FASTAPI');
        } catch (\Exception $e) {
            return back()->with('error', 'No fue posible guardar');
        }
    }

    public function index()
    {
        try {
            $usuarios = $this->fastApi->get('/todosUsuarios/');
            return view('consulta', compact('usuarios'));
        } catch (\Exception $e) {
            return back()->with('error', 'No se pudo obtener la lista de usuarios');
        }
    }

    public function destroy($id)
    {
        try {
            $this->fastApi->delete("/usuarios/$id");
            return redirect()->route('usuario.index')->with('success', 'Usuario eliminado correctamente.');
        } catch (\Exception $e) {
            return back()->with('error', 'Error al eliminar el usuario.');
        }
    }

    public function update(Request $request, $id)
    {
        $usuario = $request->validate([
            'name' => 'required',
            'age' => 'required|integer',
            'email' => 'required|email'
        ]);

        try {
            $this->fastApi->put("/usuarios/$id", $usuario);
            return redirect()->route('usuario.index')->with('success', 'Usuario actualizado correctamente.');
        } catch (\Exception $e) {
            return back()->with('error', 'Error al actualizar el usuario.');
        }
    }
}
