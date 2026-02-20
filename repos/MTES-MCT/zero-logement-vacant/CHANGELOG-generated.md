## Changelog : zero-logement-vacant (30 derniers jours)

### Résumé
Les dernières mises à jour de l'application Zero Logement Vacant se concentrent sur l'amélioration de la gestion des logements, notamment l'édition groupée, la gestion des documents et l'ajout d'informations sur la performance énergétique des bâtiments. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de lier plusieurs documents à un logement (#1597).
- Amélioration de l'interface pour l'édition groupée des logements, avec affichage des différences et gestion des précisions (#1548).
- Ajout d'un système de suivi des événements liés aux documents (création, suppression, modification) pour une meilleure auditabilité.
- Possibilité d'ajouter et de modifier des informations sur la performance énergétique des bâtiments (DPE, GES, RNB) (#1571).
- Refonte du workflow d'upload des documents, avec une validation par extension de fichier (#1568).
- Ajout d'un script pour exporter les utilisateurs du système pour le Portail DF (#1583).
- Mise à jour des libellés et de la terminologie pour plus de clarté (ex: "édition groupée" au lieu de "mise à jour groupée").
- Ajout de la possibilité de filtrer les logements par consommation d'énergie du bâtiment.
- Ajout d'un affichage de l'ID de parcelle à la place de la référence cadastrale (#1625).
- Amélioration de la gestion des années de données pour les fichiers de données, avec l'ajout de l'option 'datafoncier-manual' (#1612).

### Évolutions techniques
- Mise à jour de plusieurs dépendances (React, Express, PostgreSQL, Docker, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Optimisation de la configuration NX pour améliorer l'efficacité du cache et les performances de build.
- Refactorisation du code pour supprimer les configurations et les dépendances inutiles.
- Migration de la bibliothèque Highland vers Web Streams pour une meilleure gestion des flux de données.
- Utilisation d'esbuild pour la compilation du serveur, améliorant ainsi la vitesse de build.
- Simplification des exports des packages API vers ESM uniquement.
- Amélioration de la gestion des tests et ajout de tests pour les nouvelles fonctionnalités.
- Ajout de tests et de configuration pour Dagster.
- Suppression des champs de précision obsolètes de la base de données et du code.

### Autres changements
- Mise à jour de la documentation avec des informations sur les nouvelles fonctionnalités et les changements d'architecture.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de fichiers de configuration pour les agents d'IA.
- Mise à jour des configurations des sources externes.
- Correction de bugs mineurs et améliorations de l'expérience utilisateur.
- Ajout de la possibilité de spécifier la version de PostgreSQL pour les environnements de revue (#1626).
- Ajout de la validation du préfixe international +33 pour les numéros de téléphone (#1623).
- Optimisation de l'import des DPE avec une logique de nouvelle tentative et de limitation du débit (#1515).
