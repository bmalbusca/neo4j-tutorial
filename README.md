## How to:

### Comments

See this example. 

```python
"""  
 Attributes 
 [FUNCTION]: comm_line()
 [SUB-FUNCTION]: getop.getopt(ARG,OPTION,LONG OPTION)
 * [OPTION]: 'ho:'  is recognized by -h and -o. Also, ':v' is a variable used for detection
 * [LONG OPTION]: if any long option requires an argument, its name should have a suffix of '='
 [EXE]: if that tad does not exists, the program will print something like "option -a not recognized"

 Parameters
 [RETURN]: list
 [OUTPUT]: [option-t,option-o,...] ; len(output) = 5
"""
```

### Proprietary code 

See a copyright header example. 

```python
""" 26/09/2019  
  
  This file is subject to the terms and conditions defined in
  file 'LICENSE.txt', which is part of this source code package.
  
  Version:  0.1
  Company:  Burr 
  Author:   Bruno Figueiredo (email)
    
""" 
```

# Run neo4j from anywhere (MacOS)

1.  Move the unzipped folder to '/usr/local/bin' 
		``mv neo4j-community-4.1.1 /usr/local/bin/``
2. Add to your '.bashrc' file the neo4j's bin path
		``export PATH="$PATH:"/usr/local/bin/neo4j-community-4.1.1/bin""``
		``export NEO4J_HOME="us/bin/local/neo4j"``
3. Update your bash using `source ~/.bashrc`

> You can also do this at .bash_profile, but just make sure they are linked `[[ -s ~/.bashrc ]] && source ~/.bashrc `
> *Alert!* You need do specify the path to $JAVA_HOME

# How to install neo4j Python driver

1. ``pip3 install neo4j-driver`` or ``python3 -m pip install neo4j --user``
