## Changelog : complements-alimentaires (30 derniers jours)

### Résumé
Ce changelog couvre les 30 derniers jours d'évolution du projet "complements-alimentaires". Les améliorations se concentrent sur l'accessibilité (RGAA), la correction de bugs, l'ajout de fonctionnalités (gestion des entreprises mandatées, validation du type MIME des pièces jointes), et la mise à jour des dépendances. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour les liens de téléchargement et les formulaires.

### Évolutions fonctionnelles
- Ajout de la possibilité de modifier les déclarations sans entreprises mandatées (#2734).
- Validation du type MIME des pièces jointes des déclarations (#2740).
- Inclusion du SIRET et de la TVA dans l'export des données pour les SD (#2682).
- Amélioration de la validation automatique des articles 15, réduisant le temps d'attente (#2736).
- Correction des liens de téléchargement pour les déclarations et les certificats (#2723, #2664).
- Amélioration des liens de téléchargement sur les pages de résultats et de recherche d'entreprises.

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Django, pypdf, cryptography, ipython, vue-router, vueuse, core-js, prettier, packaging, django-anymail, matplotlib-inline, jmespath, sqlfluff, et autres.
- Mise à jour de PostgreSQL dans les workflows GitHub Actions (#2735).
- Ajout de Metabase dans la configuration de Content Security Policy (CSP) (#2700, #2656).
- Correction d'un problème de hot reload (#2727).
- Amélioration de la configuration CSP.

### Autres changements
- Améliorations significatives de l'accessibilité (RGAA) :
    - Corrections liées aux fieldsets et aux labels pour une meilleure navigation au clavier (#2710, #2683, #2684, #2628).
    - Ajout de balises `title` et d'attributs `autocomplete` pour améliorer l'expérience utilisateur pour les personnes utilisant des technologies d'assistance.
    - Amélioration des messages d'alerte et des notifications.
    - Amélioration de la structure des formulaires et des pages.
- Mise à jour du logo du ministère dans les certificats (#2686).
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- Corrections de titres et de textes pour une meilleure clarté.
- Ajout de tests unitaires et d'intégration.
