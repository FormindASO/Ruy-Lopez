Le fichier `HookShellcode.c` original a été modifié pour intégrer tout un tas de DLL comprises dans `dlls.txt`.

HookShellcode.c#L269

# Compilation via Docker

```
./compile-docker
```

Produira un fichier `BlockDll.exe` prêt à l'emploi

# ToDo

- Comprendre comment transformer le powershell.exe lancé par l'outil en... autre chose.