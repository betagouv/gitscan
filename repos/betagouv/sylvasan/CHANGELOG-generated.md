## Changelog : sylvasan (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, SylvaSan a bénéficié d'améliorations significatives en termes de gestion des enquêtes, notamment avec l'ajout de la gestion des brouillons, de la synchronisation hors ligne et de l'intégration de vocabulaires. L'authentification via DSF-ref a été implémentée et des corrections de sécurité ont été apportées. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de l'application.

### Évolutions fonctionnelles
- **Gestion des enquêtes :**
    - Ajout de la possibilité de sauvegarder plusieurs brouillons par enquête. [#172](https://github.com/betagouv/sylvasan/pull/172)
    - Implémentation de la synchronisation hors ligne et du stockage local des réponses. [#172](https://github.com/betagouv/sylvasan/pull/172)
    - Affichage des réponses brouillons et en attente. [#172](https://github.com/betagouv/sylvasan/pull/172)
    - Ajout d'un résumé des réponses à la fin de chaque enquête. [#173](https://github.com/betagouv/sylvasan/pull/173)
- **Vocabulaires :**
    - Intégration de nouveaux vocabulaires et affichage dans le survey builder. [#207](https://github.com/betagouv/sylvasan/pull/207), [#208](https://github.com/betagouv/sylvasan/pull/208)
    - Possibilité d'utiliser les vocabulaires depuis l'API mobile et web. [#207](https://github.com/betagouv/sylvasan/pull/207)
    - Ajout d'un modal pour consulter les vocabulaires. [#208](https://github.com/betagouv/sylvasan/pull/208)
- **Authentification :**
    - Implémentation de l'authentification via DSF-ref. [#192](https://github.com/betagouv/sylvasan/pull/192)
- **Interface utilisateur :**
    - Ajout d'une barre d'onglets (tab bar). [#159](https://github.com/betagouv/sylvasan/pull/159)
    - Ajout d'icônes aux boutons. [#171](https://github.com/betagouv/sylvasan/pull/171)
    - Ajout d'une modal pour l'application mobile. [#191](https://github.com/betagouv/sylvasan/pull/191)
    - Amélioration de l'affichage des champs array. [#190](https://github.com/betagouv/sylvasan/pull/190)

### Évolutions techniques
- **Sécurité :**
    - Corrections de sécurité. [#226](https://github.com/betagouv/sylvasan/pull/226)
- **Infrastructure :**
    - Mise à jour de nombreuses dépendances (Django, React, Vue.js, PostgreSQL, Vite, Sentry, ruff, etc.).
- **Code :**
    - Refactoring du code pour améliorer la lisibilité et la maintenabilité.
    - Mise à jour de la configuration de la base de données DSF.
    - Ajout de tests unitaires et d'intégration.

### Autres changements
- Mise à jour de la documentation.
- Amélioration des messages d'erreur et d'information.
- Correction de bugs mineurs et améliorations de l'expérience utilisateur.
- Ajout de la validation pour les titres de page.
- Suppression de warnings et de code obsolète.
- Ajout de métadonnées.
- Mise à jour du package.json.
- Ajout du champ carte sur mobile et web.
- Ajout d'un champ d'autocomplétion.
- Ajout d'un champ liste d'objets dans le survey creator.
- Ajout d'un composant Summary.
- Mise à jour de la configuration de TypeScript.
- Rollback de Vite 7.x.
- Ajout de types pour les champs array.
- Ajout de messages d'info sur les champs array.
- Ajout de styles Tailwind.
- Utilisation du FieldCard pour les champs liste d'objets.
- Amélioration de l'affichage des listes d'observations.
- Ajout d'un empty view pour les listes d'observations.
- Ajout de l'option d'utiliser le vocabulaire dans le survey builder.
- Exposition des vocabulary-sets depuis l'API.
- Affichage des vocabulaires dans le renderer.
- Changement d'URL pour l'API et du mot utilisé dans l'UI pour les vocabulaires.
