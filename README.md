# Bibliotik

Run bibliotik.py with python3.
An index file will be created on first execution 
(this will take a couple of minutes). 
Once that's finished, you can press any key to start.
You will see something like this:
```
Welcome to Bibliotik!
Search for:
```

Enter your search terms (case and order insensitive):
```
Search for: iliad robert fagles
0 1991 Homer - The Iliad[Transl Robert Fagles][Penguin Classics]_Rcl.azw3
1 1991 Homer - The Iliad[Transl Robert Fagles][Penguin Classics]_Rcl.pdf
2 An Iliad (Overlook) - Homer, (transl. Robert Fagles), (adapts.) Lisa Peterson, Denis O'Hare (retail).epub
```

Now enter the file numbers you wish to download,
or 'a' for all (this step uses `wget`):
```
Enter file #(s) to download: 0 1
1991 Homer - The I 100%[===============>]   1.45M  1.97MB/s    in 0.7s    
1991 Homer - The I 100%[===============>]   9.20M  5.65MB/s    in 1.6s 

Done!

Press ENTER to continue
```

Press `ENTER` to start all over again! Or `C-d` to exit.
