## Changelog : accounts (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la qualité du code, la sécurité et la simplification de la gestion des dépendances et de l'environnement de développement. Des corrections de style et des mises à jour de l'infrastructure ont également été apportées pour optimiser le projet.

### Évolutions techniques
- Mise à jour de la version de Python à 3.14.5 [#2a6bcfe](https://github.com/suitenumerique/accounts/commit/2a6bcfe).
- Utilisation de groupes de dépendances pour l'environnement de développement [#09a3420](https://github.com/suitenumerique/accounts/commit/09a3420).
- Utilisation de dépendances verrouillées pour les workflows backend afin d'assurer la reproductibilité [#049214e](https://github.com/suitenumerique/accounts/commit/049214e).
- Simplification de la gestion des versions dans les images Docker en utilisant `ARG` [#42f9a15](https://github.com/suitenumerique/accounts/commit/42f9a15).
- Utilisation de la même version d' `uv` lors de la construction des images Docker [#e7dc62d](https://github.com/suitenumerique/accounts/commit/e7dc62d).
- Suppression du script lié à un sous-module git non utilisé [#5595967](https://github.com/suitenumerique/accounts/commit/5595967).
- Suppression du fichier `setup.py` devenu inutile [#680189f](https://github.com/suitenumerique/accounts/commit/680189f).
- Amélioration de la configuration de l'action `setup-python` dans Crowdin [#923f370](https://github.com/suitenumerique/accounts/commit/923f370).
- Restriction de l'exposition des services Docker à l'extérieur [#44d4fa0](https://github.com/suitenumerique/accounts/commit/44d4fa0).

### Autres changements
- Application des règles de formatage `ruff` (Pyflakes et pyupgrade) pour améliorer la qualité du code [#b162579](https://github.com/suitenumerique/accounts/commit/b162579), [#07829c4](https://github.com/suitenumerique/accounts/commit/07829c4).
- Corrections de plusieurs erreurs shellcheck dans les scripts shell [#e855913](https://github.com/suitenumerique/accounts/commit/e855913), [#3298808](https://github.com/suitenumerique/accounts/commit/3298808), [#fc8e216](https://github.com/suitenumerique/accounts/commit/fc8e216), [#1bdf822](https://github.com/suitenumerique/accounts/commit/1bdf822), [#df96aa1](https://github.com/suitenumerique/accounts/commit/df96aa1).
- Amélioration de la gestion des arguments optionnels dans les scripts binaires [#b53ab39](https://github.com/suitenumerique/accounts/commit/b53ab39).
- Correction du script `generate-readme.sh` pour qu'il fonctionne depuis n'importe quel répertoire [#3298808](https://github.com/suitenumerique/accounts/commit/3298808).
- Mise à jour de l'adresse e-mail du projet dans la documentation [#233dea5](https://github.com/suitenumerique/accounts/commit/233dea5).
- Reformattage du tableau des services dans le fichier README [#56b1d78](https://github.com/suitenumerique/accounts/commit/56b1d78).
- Utilisation des identifiants corrects dans le README [#1886da2](https://github.com/suitenumerique/accounts/commit/1886da2).
