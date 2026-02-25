## Changelog : otelo (30 derniers jours)

### Résumé
Le projet Otelo a connu une période d'activité intense ces dernières semaines, avec des améliorations significatives de l'expérience utilisateur, notamment dans l'export de données, la gestion des utilisateurs et des groupes EPCI, ainsi que l'ajout de nouvelles fonctionnalités comme la visualisation des territoires voisins et l'historique des simulations. Des efforts importants ont également été consacrés à l'amélioration de la stabilité et de la performance de l'application, ainsi qu'à la mise en place d'une infrastructure de déploiement plus robuste.

### Évolutions fonctionnelles
- Ajout d'une page de retours utilisateurs (#16)
- Possibilité de supprimer un groupe EPCI (#15)
- Ajout de la fonctionnalité de territoire voisin avec un test A/B (#2, #1)
- Amélioration de l'export Excel, notamment la correction des décimales (#18)
- Ajout d'un bouton d'export des résultats de simulation (#10)
- Amélioration de l'affichage des logements secondaires (#7d3ad9c)
- Ajout d'un bandeau de feedback en haut de l'application (#3d2356f)
- Refonte de la gestion des utilisateurs (#3079a94)
- Ajout de sources de données (#4)
- Amélioration du calcul des taux de logements vacants moyens (#38a150d)
- Ajout de l'exportation en image et amélioration des textes (#e9c6bb3)
- Ajout de la possibilité de visualiser les offres potentielles RS (#f2ca409)
- Correction de l'arrondi de la taille des ménages (#457a517)

### Évolutions techniques
- Migration vers une meilleure solution d'authentification (better-auth) (#3)
- Mise en place d'un système d'historique des résultats de simulation (#10)
- Amélioration de la gestion des tests unitaires, notamment pour le moteur de calcul Excel (#4c2ef91)
- Refactoring de l'architecture pour séparer l'API et l'authentification (#3276fda)
- Optimisation du build et de la configuration pour le déploiement sur Scalingo (#cc22ce3, #ef78626, #9c07a00)
- Mise à jour de la configuration de Chromium pour l'export PDF (#997563c)
- Ajout de tests Prisma (#d473431)
- Amélioration de la gestion des migrations de la base de données (#7263272)
- Correction d'un problème de blocage de l'interface lors du défilement vers une projection de ménages (#b8bbfcd)
- Correction d'un problème de gel de la taille de page (#c52de65)
- Ajout de tests pour le calcul du logement indigne (#5f5ef12)

### Autres changements
- Ajout d'un fichier README (#e71eeb9)
- Correction de fautes de frappe et amélioration de la lisibilité du code (#515486a, #b0c7e14)
- Suppression de commandes et de fichiers inutiles (#dd5928c, #4887078)
- Mise à jour des dépendances et configuration du linting (#ea8fcd7, #29d4710, #6607b63)
- Ajout de tests pour l'API (#3482e7f)
- Suppression de la seed data (#4887078)
- Correction de problèmes de build (#5e4a880, #12ecbcc)
