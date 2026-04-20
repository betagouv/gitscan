## Changelog : sylvasan (30 derniers jours, au 17 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la gestion des enquêtes, notamment la création, la modification, la sauvegarde de brouillons et l'affichage des réponses. Des améliorations significatives ont également été apportées à l'application mobile, avec l'ajout de la synchronisation hors ligne et l'optimisation de l'interface utilisateur. De nombreuses mises à jour de dépendances ont été intégrées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- **Gestion des enquêtes :**
    - Possibilité de sauvegarder plusieurs brouillons par enquête [#173](https://github.com/betagouv/sylvasan/pull/173).
    - Affichage d'un résumé des réponses à la fin de chaque enquête.
    - Affichage des réponses brouillons et en attente.
    - Création d'enquêtes via l'interface web [#142](https://github.com/betagouv/sylvasan/pull/142).
    - Création d'une page pour visualiser les réponses aux enquêtes.
    - Ajout d'une fonctionnalité de liste des réponses.
- **Application mobile :**
    - Synchronisation des réponses hors ligne.
    - Amélioration de l'affichage des enquêtes sur mobile.
    - Ajout d'un "pull-down to refresh" pour actualiser les données.
    - Correction de bugs et amélioration de la stabilité.
- **Interface utilisateur :**
    - Ajout d'icônes dans les boutons.
    - Ajout d'une barre d'onglets (tab bar) pour une navigation plus intuitive [#159](https://github.com/betagouv/sylvasan/pull/159).
    - Ajout d'un aperçu de la carte.
    - Amélioration de l'affichage des champs de formulaire.

### Évolutions techniques
- **Architecture :**
    - Refactor de la liste d'enquêtes.
    - Partage de code entre le web et le mobile (en cours de stabilisation).
- **Dépendances :**
    - Mises à jour de nombreuses dépendances (Django, React, Vue.js, Capacitor, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- **Tests :**
    - Ajout de tests pour les nouvelles fonctionnalités.
    - Correction de bugs détectés par les tests.
- **CI/CD :**
    - Mise à jour des workflows CI/CD.

### Autres changements
- Ajout de documentation pour l'ADR 003 concernant le partage de fichiers TypeScript.
- Ajout de validations pour les titres de page.
- Ajout de pages dans le renderer.
- Correction de problèmes d'affichage dans les composants DsfrTabs.
- Ajout de types globaux pour améliorer la cohérence du code.
- Ajout de factories pour faciliter les tests.
- Suppression de code inutile et amélioration de la lisibilité du code.
