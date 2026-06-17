## Changelog : tacct-legacy-nextjs (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, le projet a progressé significativement avec la mise en place de l'infrastructure de base Next.js et Prisma, l'intégration de l'authentification via ProConnect, et le début du développement des fonctionnalités principales, notamment la gestion des stratégies et le chiffrement des données sensibles. Des améliorations esthétiques ont également été apportées à l'interface utilisateur.

### Évolutions fonctionnelles
- Implémentation de l'authentification via ProConnect, permettant l'interopérabilité des comptes utilisateurs. [#3ad9335](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/3ad9335)
- Création des premières pages de l'application, posant les bases de l'interface utilisateur. [#eee3543](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/eee3543)
- Développement des pages dédiées à la gestion des stratégies. [#caebcd0](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/caebcd0)
- Ajout d'un chiffrement/déchiffrement pour les données sensibles, améliorant la sécurité des informations. [#b34862e](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/b34862e)
- Correction de l'affichage du nombre d'impacts. [#bdca5f3](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/bdca5f3)
- Ajout d'un helper menu pour l'administration. [#70f6824](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/70f6824)
- Correction d'un problème de redirection pour le dossier public. [#9dbd1c2](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/9dbd1c2)

### Évolutions techniques
- Initialisation du projet Next.js avec Prisma et ProConnect (Phase 0). [#38e2d47](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/38e2d47)
- Génération du schéma Prisma pour faciliter l'interaction avec la base de données. [#5660ca3](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/5660ca3) et [#28e5648](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/28e5648)
- Mise à jour de la version de pnpm. [#0786597](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/0786597)
- Utilisation de chemins relatifs pour les imports, améliorant la portabilité du code. [#2754683](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/2754683)
- Obtention de l'origine du serveur public. [#9e9f134](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/9e9f134)

### Autres changements
- Amélioration du style de l'interface utilisateur sur différentes pages. [#97c82b3](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/97c82b3) et [#f99b602](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/f99b602)
- Nettoyage du fichier README. [#b9afc81](https://github.com/incubateur-ademe/tacct-legacy-nextjs/commit/b9afc81)
