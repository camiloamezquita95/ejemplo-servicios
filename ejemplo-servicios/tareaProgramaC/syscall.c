#include <fcntl.h>      /* Modos de apertura */
#include <stdlib.h>     /* Funciones de ficheros */

main ( int argc, char* argv[] )
{
   char cadena[20];	/* Depósito de los caracteres */
   int leidos;

   /* Apertura del fichero */

   int fichero = open ("fichero", O_RDONLY);

   /* Comprobación */   
   if (fichero==-1)
   {
        perror("Error al abrir fichero:");
        exit(1);
   }

   /* Coloca el puntero en la posición 1 */
   lseek(fichero,0,SEEK_SET);

   /* Lee 20 bytes */
   leidos = read(fichero, cadena,20);
   close(fichero);
   cadena[20]=0;

   /* Mensaje para ver qué se leyó */
   printf ( "Se leyeron %d bytes. La cadena leída es %s\n", 			  leidos,cadena );

   return 0;
}
