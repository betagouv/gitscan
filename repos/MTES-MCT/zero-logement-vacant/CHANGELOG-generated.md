## Changelog : zero-logement-vacant (30 derniers jours, au 05 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'importation des données LOVAC 2026, l'optimisation des performances, et l'ajout de nouvelles fonctionnalités d'analyse et d'exportation de données. Des corrections de bugs et des améliorations de la qualité du code ont également été apportées.

### Évolutions fonctionnelles
- **Import LOVAC 2026:** Amélioration significative du processus d'importation des données LOVAC 2026, incluant la gestion des propriétaires, des logements et des événements associés.  De nombreuses optimisations de performance ont été implémentées pour accélérer le processus.
- **Analyse de données:** Ajout d'une nouvelle vue d'analyse avec des graphiques DSFR natifs, alimentés par l'API Metabase.
- **Export de données:** Différenciation de l'export pour les groupes et les campagnes, avec ajout de nouvelles colonnes (date de naissance du propriétaire, ville du propriétaire) et formatage amélioré.
- **Campagnes:** Possibilité de créer des liens directs vers les logements depuis les noms de campagne.
- **Tableau des destinataires de campagne:** Ajout d'une colonne "Statut de suivi" pour visualiser l'état de chaque destinataire.
- **Cartographie:** Amélioration de l'expérience utilisateur de la légende de la carte, avec un positionnement plus clair et un style DSFR.

### Évolutions techniques
- **Architecture:** Refactorisation importante pour supprimer le préfixe `/api` des routes et des appels réseau, simplifiant ainsi l'architecture.
- **Performances:** Optimisations significatives des requêtes SQL et de l'import des données LOVAC, notamment en utilisant DuckDB et des traitements par lots.
- **Tests:** Amélioration de la couverture de tests, notamment pour les tests d'intégration et les tests E2E.
- **Dépendances:** Mise à jour des dépendances du projet.
- **CI/CD:** Amélioration du pipeline CI/CD, notamment pour les tests Dagster.
- **Migration React Router:** Mise à jour vers la version 7 de React Router.
- **Refactorisation du code:** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Utilisation de TypeScript:** Amélioration de la typage et correction d'erreurs de type.

### Autres changements
- **Documentation:** Mise à jour de la documentation pour refléter les changements apportés au projet.
- **Configuration:** Mise à jour de la configuration du projet.
- **Linting:** Correction d'erreurs de linting.
- **Nettoyage du code:** Suppression de fichiers inutiles et amélioration de la structure du code.
- **Ajout de skills:** Ajout de skills pour faciliter la maintenance et le développement du projet.
- **Amélioration de la gestion des erreurs:** Ajout de gestion des erreurs plus robustes.
- **Amélioration des logs:** Ajout de logs plus informatifs.
