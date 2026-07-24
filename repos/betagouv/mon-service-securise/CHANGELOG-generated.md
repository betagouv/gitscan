## Changelog : mon-service-securise (30 derniers jours, au 20 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des risques, notamment avec l'intégration de référentiels externes (AE2690, ISO2700X, ReCyf) et l'introduction des Risques V2. L'interface utilisateur a été modernisée avec l'utilisation de composants DSFR et des corrections ont été apportées pour améliorer l'expérience utilisateur et la stabilité de l'application. Des améliorations de la sécurité et des corrections de bugs ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de la gestion des référentiels externes (AE2690, ISO2700X, ReCyf) et affichage des mesures associées.
- Introduction des Risques V2 avec la possibilité de surcharger la gravité d'un risque.
- Ajout d'une page publique répertoriant toutes les mesures du référentiel V2.
- Amélioration de l'affichage des mesures spécifiques et des risques dans les tableaux.
- Ajout d'un toggle pour afficher ou masquer les référentiels externes.
- Implémentation d'une première version du PDF "Annexes" en Typst.
- Ajout d'une notification de nouveauté pour les référentiels externes et les risques V2.
- Possibilité d'insérer un service V1 depuis la console admin.
- Ajout d'une indication de fichier généré lors de la sélection des vecteurs et des matrices.
- Ajout d'un champ de consentement pour le pixel de suivi et d'un webhook associé.

### Évolutions techniques
- Conversion de nombreux modèles métier en Typescript (PartiesPrenantes, ActeurHomologation, etc.).
- Refonte de l'interface utilisateur avec l'utilisation de composants DSFR.
- Amélioration de la gestion des erreurs et des validations.
- Mise à jour de nombreuses dépendances (Express, ESLint, Playwright, etc.).
- Optimisation de l'affichage des données et des performances.
- Suppression de code obsolète et simplification de l'architecture.
- Ajout de tests unitaires et d'intégration.
- Amélioration du système de logs et de monitoring.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités.
- Correction de nombreuses coquilles et typos.
- Amélioration de la cohérence de l'interface utilisateur.
- Suppression de configurations et de variables inutilisées.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Amélioration du système de suivi des événements (Matomo).
