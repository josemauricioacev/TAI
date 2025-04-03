<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\userController;

Route::get('/', [UserController::class, 'inicio'])->name('usuario.inicio');
Route::post('/usuarios', [UserController::class, 'store'])->name('usuario.store');
Route::get('/usuarios', [UserController::class, 'index'])->name('usuario.index');
Route::delete('/usuarios/{id}', [UserController::class, 'destroy'])->name('usuario.destroy');
Route::put('/usuarios/{id}', [UserController::class, 'update'])->name('usuario.update');
