@echo off
echo === Iniciando consolas y escritorios ===

start cmd /k "python -m frontend.consola.conso_producto.consola"
start cmd /k "python -m frontend.consola.conso_comentario.consola"
start cmd /k "python -m frontend.escritorio.escri_producto.escritorio"
start cmd /k "python -m frontend.escritorio.escri_comentario.escritorio"
start cmd /k "python -m frontend.consola.conso_barbero.consola"
start cmd /k "python -m frontend.consola.conso_barberia.consola"
start cmd /k "python -m frontend.escritorio.escri_barbero.escritorio"
start cmd /k "python -m frontend.escritorio.escri_barberia.escritorio"
