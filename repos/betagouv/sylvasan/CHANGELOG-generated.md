## Changelog : sylvasan (30 derniers jours, au 4 mai 2026)

### Résumé
Ce mois-ci, SylvaSan a connu des améliorations significatives en termes de gestion des enquêtes et des réponses, notamment avec l'ajout de la gestion des brouillons, d'un nouveau système d'onglets pour la navigation et l'introduction de nouveaux types de champs dans le constructeur d'enquêtes. Des mises à jour de sécurité et de dépendances ont également été effectuées pour assurer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Gestion des enquêtes :**
    - Ajout de la possibilité de sauvegarder plusieurs brouillons par enquête [#158](https://github.com/betagouv/sylvasan/pull/158).
    - Implémentation d'un système de navigation par onglets pour une meilleure organisation des enquêtes et des réponses [#152](https://github.com/betagouv/sylvasan/pull/152).
    - Ajout d'un aperçu de la carte dans l'application mobile [#152](https://github.com/betagouv/sylvasan/pull/152).
    - Ajout d'un "pull-down to refresh" sur l'application mobile [#152](https://github.com/betagouv/sylvasan/pull/152).
- **Constructeur d'enquêtes :**
    - Introduction de nouveaux types de champs : radio, textarea, switch [#152](https://github.com/betagouv/sylvasan/pull/152).
    - Ajout de la validation pour les champs multiples dans le modal de création [#152](https://github.com/betagouv/sylvasan/pull/152).
    - Ajout d'un champ date [#152](https://github.com/betagouv/sylvasan/pull/152).
    - Ajout de la possibilité d'utiliser des vocabulaires dans le constructeur d'enquêtes et l'application mobile [#207](https://github.com/betagouv/sylvasan/pull/207), [#208](https://github.com/betagouv/sylvasan/pull/208).
- **Affichage des réponses :**
    - Affichage des réponses dans le deuxième onglet [#152](https://github.com/betagouv/sylvasan/pull/152).
    - Ajout d'un composant "Summary" pour afficher un résumé des réponses envoyées [#173](https://github.com/betagouv/sylvasan/pull/173).
- **Interface utilisateur :**
    - Ajout d'icônes dans les boutons [#152](https://github.com/betagouv/sylvasan/pull/152).
    - Amélioration de l'affichage des listes d'observations [#173](https://github.com/betagouv/sylvasan/pull/173).
    - Ajout d'une modal/toast pour afficher les erreurs sur l'application mobile [#191](https://github.com/betagouv/sylvasan/pull/191).

### Évolutions techniques
- **Authentification :**
    - Implémentation de l'authentification avec DSF-ref [#192](https://github.com/betagouv/sylvasan/pull/192).
    - Configuration facultative de la base de données DSF [#192](https://github.com/betagouv/sylvasan/pull/192).
- **Mises à jour de dépendances :**
    - Mises à jour de nombreuses dépendances (Django, React, Vue.js, Vite, etc.) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
- **Refactoring :**
    - Refactor de la liste d'enquêtes [#152](https://github.com/betagouv/sylvasan/pull/152).
    - Suppression de code obsolète et amélioration de la structure du code.

### Autres changements
- Ajout de la validation pour les titres de page.
- Ajout de messages d'information sur les champs array.
- Mise à jour de la documentation.
- Amélioration des tests.
- Correction de bugs mineurs.
