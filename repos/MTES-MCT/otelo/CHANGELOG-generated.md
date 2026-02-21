## Changelog : otelo (30 derniers jours)

### Résumé
Le projet Otelo a connu une période d'activité intense, avec de nombreuses améliorations et nouvelles fonctionnalités. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'une page de retours utilisateurs, l'amélioration de la gestion des utilisateurs et des groupes EPCI, ainsi que l'ajout de nouvelles fonctionnalités de simulation et d'export de données. Des améliorations techniques significatives ont également été apportées, notamment la migration vers un nouveau système d'authentification et l'optimisation du processus de build et de déploiement.

### Évolutions fonctionnelles
- Ajout d'une page de retours utilisateurs (#567219f)
- Possibilité de supprimer un groupe EPCI (#15)
- Amélioration de la gestion des utilisateurs (refonte et tri) (#3079a94)
- Ajout d'un bouton d'export des résultats de simulation (#10)
- Ajout de la fonctionnalité "territoires voisins" pour l'analyse comparative (#1, #2)
- Ajout d'un test A/B pour la fonctionnalité "territoires voisins" (#3)
- Amélioration de l'affichage des taux de logements vacants (#38a150d)
- Ajout de l'exportation des données au format image (#e9c6bb3)
- Ajout de la possibilité d'ajouter des EPCI voisins dans les statistiques exportées (#2c043b0)
- Ajout d'une bannière de feedback pour les utilisateurs (#3d2356f)
- Amélioration de la navigation dans le menu d'en-tête pour les utilisateurs connectés (#6233f97)
- Correction de l'affichage des couleurs des graphiques et des taux d'occupation (#d65871a)
- Ajout de la gestion des sources de données (#4)

### Évolutions techniques
- Migration vers un nouveau système d'authentification "better auth" (#3, #eae9833)
- Refonte du processus de build et de déploiement pour Scalingo (plusieurs commits)
- Amélioration de la gestion des dépendances et des versions (plusieurs commits)
- Ajout de tests unitaires pour le moteur de calcul basé sur Excel (#4c2ef91)
- Mise en place d'un système de gestion de l'historique des résultats de simulation (#10, #d473431)
- Optimisation du processus de migration de la base de données (#7263272)
- Utilisation de Puppeteer pour la gestion de Chromium (#9a845b5, #2418a08, #997563c)

### Autres changements
- Ajout d'un fichier README pour le projet (#e71eeb9)
- Correction de fautes de frappe et amélioration de la lisibilité du code (plusieurs commits)
- Suppression de code inutile et nettoyage du projet (plusieurs commits)
- Mise à jour de la configuration du projet (plusieurs commits)
- Ajout de tests pour le calcul des logements mal logés (#5f5ef12)
