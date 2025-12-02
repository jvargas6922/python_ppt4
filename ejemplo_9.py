"""
¿En qué consistirá la Demo?
Aplicar for y while en una situación más avanzada, combinando validaciones y lógica condicional.
1. Simular un cajero automático que solicite un PIN al usuario.(listo)
    a. Permitir hasta 3 intentos antes de bloquear el acceso. (listo)
2. Configurar variables iniciales
    a. Almacenar un PIN correcto (ejemplo: pin_correcto = "1234"). (listo)
3. Usar un ciclo while para validar intentos
    a. Permitir al usuario ingresar el PIN. (listo)
    b. Reducir el número de intentos después de cada intento fallido. (listo)
    c. Bloquear el acceso tras 3 intentos incorrectos. (listo)
4. Usar break para finalizar el ciclo
    a. Si el usuario ingresa el PIN correcto, terminar el ciclo. (listo)
    b. Mostrar un mensaje de bienvenida si el PIN es correcto. (listo)
5. Ejecutar y Validar.
"""

# logica
"""
Entrada:
 - Definir el PIN correcto.
 - intentos = 3
 - ingrese credenciales
Proceso:
- Validar las credenciales
Salida:
- Mostrar mensaje segun caso que se le presente al usuario.(Correcto o Incorrecto)
"""

intentos = 3
intento = 1
password_correcto = 1234
while intentos > 0:
# while intento >= intentos:
    password = int(input("Ingrese su PIN (nota son solo 4 digitos): "))
    if password == password_correcto:
        print("Bienvenido al cajero automático")
        break
    else:
        print("PIN incorrecto, intente de nuevo")
        intentos -= 1
if intentos == 0:
    print("Cuenta bloqueada, por favor contacte a su banco.")