# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
                ('language', models.CharField(default=b'python', max_length=100, choices=[(b'abap', b'ABAP'), (b'ada', b'Ada'), (b'agda', b'Agda'), (b'ahk', b'autohotkey'), (b'alloy', b'Alloy'), (b'antlr', b'ANTLR'), (b'antlr-as', b'ANTLR With ActionScript Target'), (b'antlr-cpp', b'ANTLR With CPP Target'), (b'antlr-csharp', b'ANTLR With C# Target'), (b'antlr-java', b'ANTLR With Java Target'), (b'antlr-objc', b'ANTLR With ObjectiveC Target'), (b'antlr-perl', b'ANTLR With Perl Target'), (b'antlr-python', b'ANTLR With Python Target'), (b'antlr-ruby', b'ANTLR With Ruby Target'), (b'apacheconf', b'ApacheConf'), (b'apl', b'APL'), (b'applescript', b'AppleScript'), (b'as', b'ActionScript'), (b'as3', b'ActionScript 3'), (b'aspectj', b'AspectJ'), (b'aspx-cs', b'aspx-cs'), (b'aspx-vb', b'aspx-vb'), (b'asy', b'Asymptote'), (b'at', b'AmbientTalk'), (b'autoit', b'AutoIt'), (b'awk', b'Awk'), (b'basemake', b'Base Makefile'), (b'bash', b'Bash'), (b'bat', b'Batchfile'), (b'bbcode', b'BBCode'), (b'befunge', b'Befunge'), (b'blitzbasic', b'BlitzBasic'), (b'blitzmax', b'BlitzMax'), (b'boo', b'Boo'), (b'brainfuck', b'Brainfuck'), (b'bro', b'Bro'), (b'bugs', b'BUGS'), (b'c', b'C'), (b'c-objdump', b'c-objdump'), (b'ca65', b'ca65 assembler'), (b'cbmbas', b'CBM BASIC V2'), (b'ceylon', b'Ceylon'), (b'cfc', b'Coldfusion CFC'), (b'cfengine3', b'CFEngine3'), (b'cfm', b'Coldfusion HTML'), (b'cfs', b'cfstatement'), (b'chai', b'ChaiScript'), (b'chapel', b'Chapel'), (b'cheetah', b'Cheetah'), (b'cirru', b'Cirru'), (b'clay', b'Clay'), (b'clojure', b'Clojure'), (b'clojurescript', b'ClojureScript'), (b'cmake', b'CMake'), (b'cobol', b'COBOL'), (b'cobolfree', b'COBOLFree'), (b'coffee-script', b'CoffeeScript'), (b'common-lisp', b'Common Lisp'), (b'console', b'Bash Session'), (b'control', b'Debian Control file'), (b'coq', b'Coq'), (b'cpp', b'C++'), (b'cpp-objdump', b'cpp-objdump'), (b'croc', b'Croc'), (b'cryptol', b'Cryptol'), (b'csharp', b'C#'), (b'css', b'CSS'), (b'css+django', b'CSS+Django/Jinja'), (b'css+erb', b'CSS+Ruby'), (b'css+genshitext', b'CSS+Genshi Text'), (b'css+lasso', b'CSS+Lasso'), (b'css+mako', b'CSS+Mako'), (b'css+mozpreproc', b'CSS+mozpreproc'), (b'css+myghty', b'CSS+Myghty'), (b'css+php', b'CSS+PHP'), (b'css+smarty', b'CSS+Smarty'), (b'cucumber', b'Gherkin'), (b'cuda', b'CUDA'), (b'cypher', b'Cypher'), (b'cython', b'Cython'), (b'd', b'D'), (b'd-objdump', b'd-objdump'), (b'dart', b'Dart'), (b'delphi', b'Delphi'), (b'dg', b'dg'), (b'diff', b'Diff'), (b'django', b'Django/Jinja'), (b'docker', b'Docker'), (b'dpatch', b'Darcs Patch'), (b'dtd', b'DTD'), (b'duel', b'Duel'), (b'dylan', b'Dylan'), (b'dylan-console', b'Dylan session'), (b'dylan-lid', b'DylanLID'), (b'ebnf', b'EBNF'), (b'ec', b'eC'), (b'ecl', b'ECL'), (b'eiffel', b'Eiffel'), (b'elixir', b'Elixir'), (b'erb', b'ERB'), (b'erl', b'Erlang erl session'), (b'erlang', b'Erlang'), (b'evoque', b'Evoque'), (b'factor', b'Factor'), (b'fan', b'Fantom'), (b'fancy', b'Fancy'), (b'felix', b'Felix'), (b'fortran', b'Fortran'), (b'foxpro', b'FoxPro'), (b'fsharp', b'FSharp'), (b'gap', b'GAP'), (b'gas', b'GAS'), (b'genshi', b'Genshi'), (b'genshitext', b'Genshi Text'), (b'glsl', b'GLSL'), (b'gnuplot', b'Gnuplot'), (b'go', b'Go'), (b'golo', b'Golo'), (b'gooddata-cl', b'GoodData-CL'), (b'gosu', b'Gosu'), (b'groff', b'Groff'), (b'groovy', b'Groovy'), (b'gst', b'Gosu Template'), (b'haml', b'Haml'), (b'handlebars', b'Handlebars'), (b'haskell', b'Haskell'), (b'haxeml', b'Hxml'), (b'html', b'HTML'), (b'html+cheetah', b'HTML+Cheetah'), (b'html+django', b'HTML+Django/Jinja'), (b'html+evoque', b'HTML+Evoque'), (b'html+genshi', b'HTML+Genshi'), (b'html+handlebars', b'HTML+Handlebars'), (b'html+lasso', b'HTML+Lasso'), (b'html+mako', b'HTML+Mako'), (b'html+myghty', b'HTML+Myghty'), (b'html+php', b'HTML+PHP'), (b'html+smarty', b'HTML+Smarty'), (b'html+twig', b'HTML+Twig'), (b'html+velocity', b'HTML+Velocity'), (b'http', b'HTTP'), (b'hx', b'Haxe'), (b'hybris', b'Hybris'), (b'hylang', b'Hy'), (b'i6t', b'Inform 6 template'), (b'idl', b'IDL'), (b'idris', b'Idris'), (b'iex', b'Elixir iex session'), (b'igor', b'Igor'), (b'inform6', b'Inform 6'), (b'inform7', b'Inform 7'), (b'ini', b'INI'), (b'io', b'Io'), (b'ioke', b'Ioke'), (b'irc', b'IRC logs'), (b'isabelle', b'Isabelle'), (b'jade', b'Jade'), (b'jags', b'JAGS'), (b'jasmin', b'Jasmin'), (b'java', b'Java'), (b'javascript+mozpreproc', b'Javascript+mozpreproc'), (b'jlcon', b'Julia console'), (b'js', b'JavaScript'), (b'js+cheetah', b'JavaScript+Cheetah'), (b'js+django', b'JavaScript+Django/Jinja'), (b'js+erb', b'JavaScript+Ruby'), (b'js+genshitext', b'JavaScript+Genshi Text'), (b'js+lasso', b'JavaScript+Lasso'), (b'js+mako', b'JavaScript+Mako'), (b'js+myghty', b'JavaScript+Myghty'), (b'js+php', b'JavaScript+PHP'), (b'js+smarty', b'JavaScript+Smarty'), (b'json', b'JSON'), (b'jsonld', b'JSON-LD'), (b'jsp', b'Java Server Page'), (b'julia', b'Julia'), (b'kal', b'Kal'), (b'kconfig', b'Kconfig'), (b'koka', b'Koka'), (b'kotlin', b'Kotlin'), (b'lagda', b'Literate Agda'), (b'lasso', b'Lasso'), (b'lcry', b'Literate Cryptol'), (b'lean', b'Lean'), (b'lhs', b'Literate Haskell'), (b'lidr', b'Literate Idris'), (b'lighty', b'Lighttpd configuration file'), (b'limbo', b'Limbo'), (b'liquid', b'liquid'), (b'live-script', b'LiveScript'), (b'llvm', b'LLVM'), (b'logos', b'Logos'), (b'logtalk', b'Logtalk'), (b'lsl', b'LSL'), (b'lua', b'Lua'), (b'make', b'Makefile'), (b'mako', b'Mako'), (b'maql', b'MAQL'), (b'mask', b'Mask'), (b'mason', b'Mason'), (b'mathematica', b'Mathematica'), (b'matlab', b'Matlab'), (b'matlabsession', b'Matlab session'), (b'minid', b'MiniD'), (b'modelica', b'Modelica'), (b'modula2', b'Modula-2'), (b'monkey', b'Monkey'), (b'moocode', b'MOOCode'), (b'moon', b'MoonScript'), (b'mozhashpreproc', b'mozhashpreproc'), (b'mozpercentpreproc', b'mozpercentpreproc'), (b'mql', b'MQL'), (b'mscgen', b'Mscgen'), (b'mupad', b'MuPAD'), (b'mxml', b'MXML'), (b'myghty', b'Myghty'), (b'mysql', b'MySQL'), (b'nasm', b'NASM'), (b'nemerle', b'Nemerle'), (b'nesc', b'nesC'), (b'newlisp', b'NewLisp'), (b'newspeak', b'Newspeak'), (b'nginx', b'Nginx configuration file'), (b'nimrod', b'Nimrod'), (b'nit', b'Nit'), (b'nixos', b'Nix'), (b'nsis', b'NSIS'), (b'numpy', b'NumPy'), (b'objdump', b'objdump'), (b'objdump-nasm', b'objdump-nasm'), (b'objective-c', b'Objective-C'), (b'objective-c++', b'Objective-C++'), (b'objective-j', b'Objective-J'), (b'ocaml', b'OCaml'), (b'octave', b'Octave'), (b'ooc', b'Ooc'), (b'opa', b'Opa'), (b'openedge', b'OpenEdge ABL'), (b'pan', b'Pan'), (b'pawn', b'Pawn'), (b'perl', b'Perl'), (b'perl6', b'Perl6'), (b'php', b'PHP'), (b'pig', b'Pig'), (b'pike', b'Pike'), (b'plpgsql', b'PL/pgSQL'), (b'postgresql', b'PostgreSQL SQL dialect'), (b'postscript', b'PostScript'), (b'pot', b'Gettext Catalog'), (b'pov', b'POVRay'), (b'powershell', b'PowerShell'), (b'prolog', b'Prolog'), (b'properties', b'Properties'), (b'protobuf', b'Protocol Buffer'), (b'psql', b'PostgreSQL console (psql)'), (b'puppet', b'Puppet'), (b'py3tb', b'Python 3.0 Traceback'), (b'pycon', b'Python console session'), (b'pypylog', b'PyPy Log'), (b'pytb', b'Python Traceback'), (b'python', b'Python'), (b'python3', b'Python 3'), (b'qbasic', b'QBasic'), (b'qml', b'QML'), (b'racket', b'Racket'), (b'ragel', b'Ragel'), (b'ragel-c', b'Ragel in C Host'), (b'ragel-cpp', b'Ragel in CPP Host'), (b'ragel-d', b'Ragel in D Host'), (b'ragel-em', b'Embedded Ragel'), (b'ragel-java', b'Ragel in Java Host'), (b'ragel-objc', b'Ragel in Objective C Host'), (b'ragel-ruby', b'Ragel in Ruby Host'), (b'raw', b'Raw token data'), (b'rb', b'Ruby'), (b'rbcon', b'Ruby irb session'), (b'rconsole', b'RConsole'), (b'rd', b'Rd'), (b'rebol', b'REBOL'), (b'red', b'Red'), (b'redcode', b'Redcode'), (b'registry', b'reg'), (b'resource', b'ResourceBundle'), (b'rexx', b'Rexx'), (b'rhtml', b'RHTML'), (b'robotframework', b'RobotFramework'), (b'rql', b'RQL'), (b'rsl', b'RSL'), (b'rst', b'reStructuredText'), (b'rust', b'Rust'), (b'sass', b'Sass'), (b'scala', b'Scala'), (b'scaml', b'Scaml'), (b'scheme', b'Scheme'), (b'scilab', b'Scilab'), (b'scss', b'SCSS'), (b'shell-session', b'Shell Session'), (b'slim', b'Slim'), (b'smali', b'Smali'), (b'smalltalk', b'Smalltalk'), (b'smarty', b'Smarty'), (b'sml', b'Standard ML'), (b'snobol', b'Snobol'), (b'sourceslist', b'Debian Sourcelist'), (b'sp', b'SourcePawn'), (b'sparql', b'SPARQL'), (b'spec', b'RPMSpec'), (b'splus', b'S'), (b'sql', b'SQL'), (b'sqlite3', b'sqlite3con'), (b'squidconf', b'SquidConf'), (b'ssp', b'Scalate Server Page'), (b'stan', b'Stan'), (b'swift', b'Swift'), (b'swig', b'SWIG'), (b'systemverilog', b'systemverilog'), (b'tads3', b'TADS 3'), (b'tcl', b'Tcl'), (b'tcsh', b'Tcsh'), (b'tea', b'Tea'), (b'tex', b'TeX'), (b'text', b'Text only'), (b'todotxt', b'Todotxt'), (b'trac-wiki', b'MoinMoin/Trac Wiki markup'), (b'treetop', b'Treetop'), (b'ts', b'TypeScript'), (b'twig', b'Twig'), (b'urbiscript', b'UrbiScript'), (b'vala', b'Vala'), (b'vb.net', b'VB.net'), (b'vctreestatus', b'VCTreeStatus'), (b'velocity', b'Velocity'), (b'verilog', b'verilog'), (b'vgl', b'VGL'), (b'vhdl', b'vhdl'), (b'vim', b'VimL'), (b'xml', b'XML'), (b'xml+cheetah', b'XML+Cheetah'), (b'xml+django', b'XML+Django/Jinja'), (b'xml+erb', b'XML+Ruby'), (b'xml+evoque', b'XML+Evoque'), (b'xml+lasso', b'XML+Lasso'), (b'xml+mako', b'XML+Mako'), (b'xml+myghty', b'XML+Myghty'), (b'xml+php', b'XML+PHP'), (b'xml+smarty', b'XML+Smarty'), (b'xml+velocity', b'XML+Velocity'), (b'xquery', b'XQuery'), (b'xslt', b'XSLT'), (b'xtend', b'Xtend'), (b'xul+mozpreproc', b'XUL+mozpreproc'), (b'yaml', b'YAML'), (b'yaml+jinja', b'YAML+Jinja'), (b'zephir', b'Zephir')])),
                ('style', models.CharField(default=b'friendly', max_length=100, choices=[(b'autumn', b'autumn'), (b'borland', b'borland'), (b'bw', b'bw'), (b'colorful', b'colorful'), (b'default', b'default'), (b'emacs', b'emacs'), (b'friendly', b'friendly'), (b'fruity', b'fruity'), (b'igor', b'igor'), (b'manni', b'manni'), (b'monokai', b'monokai'), (b'murphy', b'murphy'), (b'native', b'native'), (b'paraiso-dark', b'paraiso-dark'), (b'paraiso-light', b'paraiso-light'), (b'pastie', b'pastie'), (b'perldoc', b'perldoc'), (b'rrt', b'rrt'), (b'tango', b'tango'), (b'trac', b'trac'), (b'vim', b'vim'), (b'vs', b'vs'), (b'xcode', b'xcode')])),
                ('highlighted', models.TextField(default=b'')),
                ('owner', models.ForeignKey(related_name='snippets', default=b'', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
