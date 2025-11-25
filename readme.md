UltraSimple 🚀
Un langage naturel minimaliste en français

      __    _ __      __  _                 
     / /   (_) /___  / /_(_)___  ____  _____
    / /   / / __/ /_/ / / / __ \/ __ \/ ___/
   / /___/ / /_/ __  / / / /_/ / /_/ (__  ) 
  /_____/_/\__/_/ /_/_/_/ .___/ .___/____/  
                       /_/   /_/            

UltraSimple v1.3 - Langage naturel en français 🚀

🌍 Présentation
UltraSimple est un langage multi-os de programmation minimaliste et francophone, pensé pour :
apprendre la logique de code sans barrière de langue,
écrire des scripts courts en français clair,
s’amuser avec une mini-IA intégrée qui répond dans la console,
partager une vision d’accessibilité numérique et de fraternité digitale 🤝.
C’est un projet open-source pour inspirer, expérimenter et prouver que la programmation peut être accessible, ludique et humaine.

⚡ Fonctionnalités principales
✅ Instructions en français : affiche, si, tant_que, repet, fonction
✅ Concaténation automatique de texte et nombres
✅ Boucles et conditions intuitives
✅ Mini IA locale 🤖 qui répond à certaines phrases
✅ REPL coloré interactif en console
✅ Exécution de fichiers .us directement
✅ Commandes intégrées : aide, credits, version
✅ Pause avec attends 2;

🛠️ Installation
Cloner le repo et installer les dépendances :
git clone https://github.com/FraterniteDigitale/UltraSimple.git
cd UltraSimple
pip install -r requirements.txt

🚀 Utilisation
Mode interactif (REPL)
python3 ultrasimple.py
Exemple :
>>> x = 5;
>>> affiche "x = " + x;
x = 5
>>> si x > 3 alors { affiche "Grand !" } sinon { affiche "Petit !" }
Grand !

Mode script
Crée un fichier hello.us :
affiche "Bonjour le monde !";
ia "comment ça va ?";
repet 3 fois { affiche "UltraSimple 💚"; }
Lance-le :
python3 ultrasimple.py hello.us

📖 Scénario d’utilisation
Imagine une classe de collégiens qui découvrent la logique de code.
Au lieu de se perdre dans print(), while ou {}, ils écrivent :
nom = "Alice";
affiche "Salut " + nom;
si 10 > 3 alors { affiche "Le monde est grand !" } sinon { affiche "Petit !" }
👉 Ils comprennent immédiatement, sans traduction.

🔮 Vision & Impact
UltraSimple vise à :
Démocratiser la programmation en français,
Offrir une porte d’entrée simple vers l’algorithmique,
Inspirer la création de langages natifs pour d’autres langues (wolof, arabe, créole, etc.),
Fédérer une communauté éducative et créative autour d’un outil accessible,
Mettre en avant une fraternité digitale : le code comme langage universel mais adapté à chaque culture.

🚧 Améliorations possibles
Ajout de structures de données (listes, dictionnaires)
Support des fichiers d’import (import utils;)
Interface graphique simple pour exécuter .us
Plus de réponses intelligentes IA locale
Export direct vers Python ou WebAssembly
Intégration éducative (exercices, tutoriels interactifs)

✨ Exemple complet
Fichier jeu.us :
affiche "Bienvenue dans le mini-jeu UltraSimple !";
nom = "Paavo";
affiche "Ton héros est " + nom;

points = 0;
repet 3 fois {
    ia "bonjour";
    points = points + 10;
    affiche "Score actuel: " + points;
}

si points >= 30 alors {
    affiche "Bravo " + nom + " 🎉";
} sinon {
    affiche "Dommage " + nom;
}

Résultat attendu :
Bienvenue dans le mini-jeu UltraSimple !
Ton héros est Paavo
🤖 IA: Bonjour à toi aussi, humain !
Score actuel: 10
🤖 IA: Bonjour à toi aussi, humain !
Score actuel: 20
🤖 IA: Bonjour à toi aussi, humain !
Score actuel: 30
Bravo Paavo 🎉

📜 Licence
MIT License – usage libre, open-source.
👤 Auteur
Fraternité Digitale
💡 Une initiative collective pour un numérique plus humain, accessible et fraternel.
📧 Contact: PS08010@proton.me
🌐 GitHub : FraternitéDigitale
