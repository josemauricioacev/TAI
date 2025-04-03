<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\userController;

Route::get('/', [userController::class, 'inicio'])->name('usuario.inicio');

Route::post('/addUser', [userController::class, 'store'])->name('usuario.store');

Route::get('/usuarios', [userController::class, 'index'])->name('usuario.index');
