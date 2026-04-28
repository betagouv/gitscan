## Changelog : sylvasan (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en permettant la sauvegarde de brouillons de réponses aux enquêtes, en affichant les réponses individuelles et en améliorant la création de formulaires. Des efforts importants ont également été consacrés à la sécurité et à la maintenance technique, avec des mises à jour de dépendances et l'intégration d'une authentification via DSF-Ref.

### Évolutions fonctionnelles
- **Gestion des réponses :** Possibilité de sauvegarder plusieurs brouillons de réponses par enquête. [#172](https://github.com/betagouv/sylvasan/pull/172)
- **Visualisation des réponses :** Affichage des réponses aux enquêtes dans l'interface web. [#139](https://github.com/betagouv/sylvasan/pull/139)
- **Détails des enquêtes et réponses :** Création de pages individuelles pour afficher les détails des enquêtes et des réponses. [#141](https://github.com/betagouv/sylvasan/pull/141), [#158](https://github.com/betagouv/sylvasan/pull/158), [#140](https://github.com/betagouv/sylvasan/pull/140)
- **Création de formulaires :** Amélioration de l'éditeur de formulaire avec l'ajout de nouveaux types de champs (radio, texte, switch, select, date) et la possibilité de gérer l'ordre des champs. [#142](https://github.com/betagouv/sylvasan/pull/142)
- **Authentification :** Intégration de l'authentification via DSF-Ref. [#192](https://github.com/betagouv/sylvasan/pull/192)
- **Interface mobile :** Ajout d'une modal/toast pour l'application mobile. [#191](https://github.com/betagouv/sylvasan/pull/191)
- **Tableau de bord :** Affichage conditionnel des actions en fonction du rôle de l'utilisateur.

### Évolutions techniques
- **Refactoring :** Refactor de la liste d'enquêtes et du composant SurveySummary.
- **Typescript :** Partage des fichiers de types TypeScript.
- **Vite :** Mise à jour de Vite et des plugins associés.
- **Dépendances :** Mises à jour de nombreuses dépendances (Django, React, Vue.js, PostgreSQL, Capacitor, Sentry, TailwindCSS, Vite, etc.).
- **CI/CD :** Mise à jour des actions GitHub.
- **Sécurité :** Mise à jour des dépendances de sécurité.

### Autres changements
- Ajout d'icônes aux boutons.
- Ajout d'une documentation concernant le partage de fichiers TypeScript (ADR-003).
- Amélioration de l'affichage des champs array dans le summary et la vue réponse.
- Correction de bugs et améliorations de l'interface utilisateur.
- Ajout de tests unitaires et d'intégration.
- Suppression de code inutilisé et nettoyage du code.
