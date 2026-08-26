## Changelog : dora (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois a été marqué par une refonte structurelle majeure de la gestion des services et des publics afin d'améliorer la cohérence des données. L'expérience utilisateur a été enrichie par de nouvelles capacités de recherche, des notifications Slack pour le suivi des dossiers et une optimisation de l'affichage des tableaux de bord.

### Évolutions fonctionnelles
- **Services & Structures** : 
    - Ajout de champs de mobilisation et de la possibilité de définir un nombre illimité de catégories par service [#1289].
    - Amélioration de la visibilité avec l'affichage des précisions sur les publics dans les pages de détails [#1264].
    - Intégration d'un filtrage du balisage Markdown dans les descriptions courtes [#1221].
    - Exclusion automatique des sources "data·inclusion" du formulaire Dora [#1225].
- **Recherche & Expérience Utilisateur** :
    - Optimisation de la recherche : gestion des doublons [#1228], limitation du nombre de résultats pour éviter la surcharge [#1245] et activation de la recherche via la touche Entrée [#1230].
    - Correction de la gestion des filtres pour assurer l'affichage des services "tous-publics" [#1261].
    - Amélioration de la navigation : affichage d'une erreur 404 explicite au lieu d'une redirection vers la connexion pour les services inaccessibles [#1224].
- **Orientations & Emplois** :
    - Mise en place de notifications Slack lors du passage d'une orientation en modération [#1296].
    - Ajout d'une fonctionnalité d'export des orientations pour "Les Emplois" [#1209].
- **Pilotage** :
    - Allègement de l'affichage du tableau des structures dans le tableau de bord des gestionnaires de territoire [#1229].
    - Enrichissement des statistiques avec le stockage des codes de zones géographiques (commune, département, région) [#1216].
- **Administration** : Permet désormais aux Groupes de Travail (GT) d'accéder directement à la page d'administration d'une structure [#1286].

### Évolutions techniques
- **Refonte majeure des Services** : 
    - Migration profonde de la gestion des "Publics" vers un nouveau schéma et vers le référentiel DI [#1237, #1252, #1267].
    - Simplification du modèle de données avec l'introduction d'un champ unique `kind` pour les types de services et la suppression des anciens modèles et relations M2M obsolètes [#1249, #1257, #1266].
    - Fusion algorithmique des descriptions de services pour une meilleure qualité de donnée [#1293].
- **Performance & Architecture** :
    - Parallélisation des appels API pour accélérer le chargement des pages d'édition des services et modèles [#1281].
    - Migration des champs de recherche vers un format `ArrayField` pour plus d'efficacité [#1247].
    - Partage de types communs entre les modèles de Services et de Modèles [#1265].
- **Maintenance & Sécurité** :
    - Correction des URLs de l'administration Django [#1295].
    - Ajout d'une commande de normalisation des mots de passe [#1271].
    - Renforcement de la sécurité via la protection des suppressions d'objets en cascade [#1220].

### Autres changements
- **Nettoyage du code** : Suppression de diverses commandes d'import/export et de code obsolète (inclusion numérique, anciens modèles de services) [#1260, #1278, #1285].
- **Maintenance de la base de données** : Suppression des structures orphelines [#1219] et nettoyage des fichiers de signaux en doublon [#1263].
