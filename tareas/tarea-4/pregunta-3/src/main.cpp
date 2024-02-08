#include "main.h"

using namespace std;

int main(int argc, char *argv[])
{
  if (argc != 2)
  {
    cout << "Uso: " << argv[0] << " <tamaño>" << endl;
    return EXIT_FAILURE;
  }

  int size = atoi(argv[1]);
  string input;

  // Crear los arreglos y sus tablas de inicializacion (O(1))
  int *T = new int[size];
  int *a = new int[size];
  int *b = new int[size];
  int ctr = -1;

  // Lambda para revisar si la posicion i esta inicializada (O(1))
  auto isInit = [&](int i) -> bool
  {
    if (!(0 <= b[i] && b[i] <= ctr))
      return false;

    return a[b[i]] == i;
  };

  cout << "Bienvenido al CLI para probar el proceso de inicializacion virtual de arreglos." << endl
       << endl
       << "Comandos disponibles:" << endl
       << "  - 'ASIGNAR POS VAL' para asignar el valor VAL en la posicion POS." << endl
       << "  - 'CONSULTAR POS' para cosultar POS." << endl
       << "  - 'LIMPIAR' para limpiar la tabla." << endl
       << "  - 'SALIR' para salir." << endl
       << endl;

  while (true)
  {

    cout << endl
         << "> Introduzca un comando: ";
    cin >> input;

    //--------------------- Comando SALIR (O(1))
    if (input == "SALIR")
      break;

    //--------------------- Comando LIMPIAR (O(1))
    if (input == "LIMPIAR")
      ctr = -1;

    //--------------------- Comando ASIGNAR (O(1))
    if (input == "ASIGNAR")
    {
      int i, val;
      cin >> i >> val;

      if (i < 0 || i >= size)
      {
        cout << "Error: Posicion invalida." << endl;
        continue;
      }

      if (!isInit(i))
      {
        ctr++;
        a[ctr] = i;
        b[i] = ctr;
      }
      T[i] = val;

      cout << "Asignando " << val << " en la posicion " << i << " ..." << endl;
    }

    //--------------------- Comando CONSULTAR (O(1))
    if (input == "CONSULTAR")
    {
      int i;
      cin >> i;

      if (i < 0 || i >= size)
      {
        cout << "Error: Posicion invalida." << endl;
        continue;
      }

      if (!isInit(i))
      {
        cout << "Posicion no inicializada." << endl;
        continue;
      }

      cout << "Posicion " << i << " inicializada, y contiene " << T[i] << "." << endl;
    }
  }

  return EXIT_SUCCESS;
}