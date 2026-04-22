## Changelog : sylvasan (30 derniers jours, au 17 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur mobile et web, notamment en permettant la sauvegarde de brouillons d'enquêtes, l'affichage des réponses, et la création d'enquêtes. Des améliorations significatives ont également été apportées à la gestion des données et à l'infrastructure du projet.

### Évolutions fonctionnelles
- **Gestion des enquêtes :**
    - Possibilité de sauvegarder plusieurs brouillons par enquête [#173](https://github.com/betagouv/sylvasan/pull/173).
    - Affichage des réponses aux enquêtes sur le web [#139](https://github.com/betagouv/sylvasan/pull/139).
    - Création d'enquêtes depuis l'interface web [#108](https://github.com/betagouv/sylvasan/pull/108).
    - Ajout d'un aperçu de la carte pour les enquêtes [#5ab5dfa](https://github.com/betagouv/sylvasan/commit/5ab5dfa).
- **Application mobile :**
    - L'application mobile récupère et cache les enquêtes hors ligne [#d352bb3](https://github.com/betagouv/sylvasan/commit/d352bb3).
    - Ajout d'un "pull-down to refresh" pour actualiser les données [#982c950](https://github.com/betagouv/sylvasan/commit/982c950).
- **Formulaires :**
    - Ajout de nouveaux types de champs dans les formulaires : radio, textarea, switch, date [#2490090](https://github.com/betagouv/sylvasan/commit/2490090).
    - Amélioration de la validation des champs de formulaire.
    - Ajout d'un aperçu des champs lors de la création de formulaires.

### Évolutions techniques
- **Infrastructure :**
    - Mise à jour de nombreuses dépendances (Django, React, Vue.js, Capacitor, Ionic, PostgreSQL, Sentry, tailwindcss, vite) pour bénéficier des dernières corrections et améliorations de sécurité.
    - Refactor de la liste d'enquêtes.
    - Mise à jour de la configuration Vite.
- **Architecture :**
    - Passage à une barre d'onglets (tab bar) pour la navigation principale [#157](https://github.com/betagouv/sylvasan/pull/157).
    - Refactor du composant SurveyRenderer pour le partage entre le web et le mobile.
    - Ajout de types globaux pour améliorer la cohérence du code.
- **Tests :**
    - Ajout de tests pour les nouvelles fonctionnalités.
    - Correction de bugs dans les tests mobiles.

### Autres changements
- Ajout d'icônes dans les boutons.
- Ajout de la validation pour les titres de page.
- Ajout d'une ADR (Architectural Decision Record) expliquant la décision d'utiliser des fichiers types TypeScript.
- Amélioration de la documentation.
- Correction de divers bugs et améliorations de la performance.
