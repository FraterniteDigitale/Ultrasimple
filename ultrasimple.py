#!/usr/bin/env python3
"""
UltraSimple v1.3 🚀
Langage naturel minimaliste en français
- multi-instructions sur une seule ligne avec ';'
- concaténation automatique texte/nombres
- fonctions, conditions, boucles, répétitions
- mini-IA locale amusante intégrée
- joli logo au lancement
- exécution de fichiers `.us`
- commandes internes: aide, credits, version
"""

import sys, time
from colorama import init, Fore, Style
from lark import Lark, Transformer, v_args, UnexpectedInput

init(autoreset=True)

grammar = r"""
    ?start: stmt+
    ?stmt: assign
         | affiche
         | si_stmt
         | tantque_stmt
         | repet_stmt
         | func_def
         | func_call
         | ia_stmt
         | attends_stmt
         | COMMENT
         | /[ \t\f\r\n]+/

    assign: IDENTIFIER "=" expr ";"
    affiche: "affiche" expr ";"
    si_stmt: "si" condition "alors" block ("sinon" block)?
    tantque_stmt: "tant_que" condition "faire" block
    repet_stmt: "repet" INT "fois" block
    attends_stmt: "attends" INT ";"

    func_def: "fonction" IDENTIFIER "(" [params] ")" block
    func_call: IDENTIFIER "(" [args] ")" ";"

    ia_stmt: "ia" STRING ";"

    params: IDENTIFIER ("," IDENTIFIER)*
    args: expr ("," expr)*

    ?block: "{" stmt* "}"
    ?condition: expr comp_op expr

    ?expr: term
         | expr "+" term   -> add
         | expr "-" term   -> sub

    ?term: factor
         | term "*" factor -> mul
         | term "/" factor -> div

    ?factor: NUMBER        -> number
           | STRING        -> string
           | IDENTIFIER    -> var
           | "(" expr ")"

    comp_op: ">" | "<" | ">=" | "<=" | "==" | "!="

    COMMENT: /\/\/[^\n]*/
    IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
    STRING: /"([^"\\]|\\.)*"/

    %import common.INT
    %import common.NUMBER
    %import common.WS
    %ignore WS
    %ignore COMMENT
"""

@v_args(inline=True)
class Execute(Transformer):
    def __init__(self):
        self.scopes = [{}]
        self.functions = {}

    def get_var(self, name):
        for scope in reversed(self.scopes):
            if name in scope: return scope[name]
        raise Exception(f"Variable '{name}' non définie")

    def set_var(self, name, value):
        self.scopes[-1][name] = value
        return value

    def number(self, n):
        s = str(n)
        return float(s) if '.' in s else int(s)

    def string(self, s): return s[1:-1]
    def var(self, name): return self.get_var(str(name))

    def add(self, a, b): return str(a) + str(b) if isinstance(a,str) or isinstance(b,str) else a+b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b): return a / b

    def assign(self, name, value): return self.set_var(str(name), value)
    def affiche(self, value): print(Fore.CYAN + str(value))

    def condition(self, a, op, b):
        op = str(op)
        return lambda: (
            a > b if op == ">" else
            a < b if op == "<" else
            a >= b if op == ">=" else
            a <= b if op == "<=" else
            a == b if op == "==" else
            a != b if op == "!=" else
            (_ for _ in ()).throw(Exception(f"Opérateur inconnu: {op}"))
        )

    def si_stmt(self, cond, block_true, block_false=None):
        if cond(): [self.transform(stmt) for stmt in block_true]
        elif block_false: [self.transform(stmt) for stmt in block_false]

    def tantque_stmt(self, cond, block):
        while cond():
            for stmt in block: self.transform(stmt)

    def repet_stmt(self, times, block):
        for _ in range(int(times)):
            for stmt in block: self.transform(stmt)

    def attends_stmt(self, delay): time.sleep(int(delay))

    def func_def(self, name, params=None, block=None):
        self.functions[str(name)] = (params or [], block or [])

    def func_call(self, name, args=None):
        name = str(name)
        if name not in self.functions: raise Exception(f"Fonction '{name}' non définie")
        params, block = self.functions[name]
        args = args or []
        if len(params) != len(args):
            raise Exception(f"Fonction '{name}' attend {len(params)} arguments, {len(args)} donnés")

        self.scopes.append(dict(zip(params, args)))
        for stmt in block: self.transform(stmt)
        self.scopes.pop()

    def params(self, *params): return [str(p) for p in params]
    def args(self, *args): return list(args)
    def block(self, *stmts): return list(stmts)

    def ia_stmt(self, text):
        phrase = str(text[1:-1]).lower()
        if "bonjour" in phrase:
            print(Fore.MAGENTA + "🤖 IA: Bonjour à toi aussi, humain !")
        elif "qui es tu" in phrase:
            print(Fore.MAGENTA + "🤖 IA: Je suis une mini-IA locale dans UltraSimple.")
        elif "comment ça va" in phrase or "ça va" in phrase:
            print(Fore.MAGENTA + "🤖 IA: Ça va très bien, merci ! Et toi ?")
        else:
            print(Fore.MAGENTA + "🤖 IA: Tu as dit -> " + phrase)

def print_logo():
    logo = r"""
      __    _ __      __  _                 
     / /   (_) /___  / /_(_)___  ____  _____
    / /   / / __/ /_/ / / / __ \/ __ \/ ___/
   / /___/ / /_/ __  / / / /_/ / /_/ (__  ) 
  /_____/_/\__/_/ /_/_/_/ .___/ .___/____/  
                       /_/   /_/            
       UltraSimple v1.3 - Langage naturel en français 🚀
    """
    print(Fore.GREEN + logo)

def run_code(code, parser):
    for part in code.split(";"):
        if part.strip():
            parser.parse(part.strip() + ";")

def repl(parser):
    print_logo()
    print(Fore.YELLOW + "Bienvenue dans UltraSimple v1.3 🤯")
    print("Tapez 'exit' pour quitter, 'aide' pour l’aide.\n")
    while True:
        try:
            code = input(Fore.WHITE + ">>> ").strip()
            if code.lower() == 'exit':
                print(Fore.YELLOW + "Au revoir 👋")
                break
            elif code.lower() == 'aide':
                print("📖 Commandes: affiche, si/sinon, tant_que, repet, fonction, ia, attends")
            elif code.lower() == 'credits':
                print("✍️  UltraSimple v1.3 - par Agent Paavo_08")
            elif code.lower() == 'version':
                print("🔖 Version 1.3")
            elif code:
                run_code(code, parser)
        except UnexpectedInput as e:
            print(Fore.RED + f"💥 Erreur de syntaxe: {e}")
        except Exception as e:
            print(Fore.RED + f"⚠️ Oups: {e}")

def main():
    parser = Lark(grammar, parser='lalr', transformer=Execute())
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            code = f.read()
            run_code(code, parser)
    else:
        repl(parser)

if __name__ == "__main__":
    main()
