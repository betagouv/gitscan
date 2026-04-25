## Changelog : anssi-portail (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des guides (ajout, suppression, mise à jour), l'ajout d'une fonctionnalité d'abonnement à une newsletter, et l'amélioration de l'expérience utilisateur du simulateur NIS2. Des corrections de sécurité et des optimisations diverses ont également été apportées.

### Évolutions fonctionnelles
- **Gestion des guides :**
    - Ajout d'une interface pour ajouter des documents aux guides.
    - Possibilité de supprimer des documents associés à un guide.
    - Amélioration de l'affichage et de la gestion des guides dans l'interface d'administration.
    - Récupération des anciens documents associés aux guides.
- **Simulateur NIS2 :**
    - Ajout de nouvelles étapes au simulateur pour une évaluation plus complète.
    - Intégration d'une fonctionnalité de téléchargement de la documentation.
    - Possibilité de sélectionner la langue du contenu du simulateur (français et anglais).
    - Amélioration de l'expérience utilisateur avec des corrections d'affichage et de navigation.
- **Newsletter :**
    - Ajout d'un formulaire d'abonnement à une newsletter.
    - Confirmation d'abonnement après soumission du formulaire.
    - Intégration avec Brevo pour la gestion des abonnés.
- **Comparateur :**
    - Suppression de la date de publication dans le comparateur.
- **Statistiques :**
    - Mise à jour de la page des statistiques.
    - Mise à jour de la fiche RC.

### Évolutions techniques
- **Sécurité :**
    - Mise à jour de plusieurs dépendances pour corriger des vulnérabilités (fast-xml-parser, yaml, picomatch, lodash).
    - Ajout de la Content Security Policy (CSP) pour Sentry.
- **Infrastructure :**
    - Mise à jour de la version de Node.js et des outils de build (vite).
    - Utilisation de Svelte 5 pour le composant bouton.
- **Architecture :**
    - Refactorisation du code pour améliorer la modularité et la maintenabilité.
    - Utilisation de Cellar pour la gestion des guides.
    - Extraction de la logique métier dans des classes dédiées.
- **Tests :**
    - Ajout de tests unitaires et d'intégration.
- **Divers :**
    - Amélioration de la gestion des assets.
    - Optimisation des performances.

### Autres changements
- Documentation mise à jour pour la nouvelle version de la demande de diagnostic.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de commentaires et de documentation au code.
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Suppression de code inutile et nettoyage du codebase.
- Mise à jour des dépendances de développement.
