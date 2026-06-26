## Changelog : territoires-en-transitions (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des audits de labellisation, l'import de plans d'action via l'IA, et la refactorisation de composants clés pour une meilleure maintenabilité et performance. Des corrections de sécurité et des améliorations de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Intégration des informations d'audit dans la vue tableau du référentiel, avec suppression de l'onglet "Suivi".
- Affichage du conseiller référent dans l'en-tête de la checklist d'audit.
- Possibilité de télécharger un archive des preuves d'un audit.
- Ajout d'une modale de clôture d'audit en deux étapes.
- Duplication de plans d'action et de fiches action.
- Amélioration de l'affichage des badges de statut d'audit.
- Ajout d'une action "Dupliquer l'action" dans les menus de fiche.
- Possibilité de télécharger les preuves d'une autre collectivité pour les utilisateurs ADEME.
- Amélioration de la gestion des statuts et des actions dans les audits de labellisation.
- Ajout d'une page "mesure désactivée".

### Évolutions techniques
- Refactorisation de l'infrastructure de gestion des rôles et des référentiels dans la checklist d'audit.
- Optimisation des performances du backend en différant le chargement des dépendances lourdes.
- Mise à jour de Node.js vers la version 24.18.0 pour corriger une régression.
- Amélioration de la gestion des erreurs lors du parsing de fichiers PDF avec pdfjs.
- Refactorisation du code pour utiliser des composants plus réutilisables et améliorer la lisibilité.
- Migration de tests vers Vitest pour une meilleure performance et intégration.
- Amélioration de la sécurité en bloquant des potentielles injections SQL et des IDOR.
- Mise à jour des dépendances (PostHog, Next.js, eslint-config-next).
- Amélioration de la gestion des tests e2e avec parallélisation et gestion des timeouts.
- Refactorisation de la gestion des libellés pour une meilleure centralisation et maintenabilité.
- Passage à une nouvelle implémentation de la recherche de collectivités.

### Autres changements
- Amélioration de la documentation pour les agents IA utilisant le dépôt.
- Mise à jour du schéma des préférences de la collectivité.
- Ajout d'un plan de bascule des référentiels CAE/ECI vers TE.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests unitaires et e2e pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- Mise à jour des données de test.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de code obsolète.
- Amélioration de la gestion des états et de la synchronisation des données.
