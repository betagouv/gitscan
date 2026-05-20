## Changelog : sylvasan (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'authentification avec l'ajout de la connexion via DSF, ainsi que sur l'ajout de nouveaux champs de données (carte, listes d'objets) pour les enquêtes. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- **Authentification :** Implémentation de la connexion via DSF (DSF-ref) pour les utilisateurs, avec gestion des sources de compte et affichage d'un spinner pendant la connexion mobile. [#244](https://github.com/betagouv/sylvasan/pull/244)
- **Nouveaux champs :** Ajout d'un champ de type carte dans les formulaires, visible sur le web et l'application mobile. [#257](https://github.com/betagouv/sylvasan/pull/257), [#260](https://github.com/betagouv/sylvasan/pull/260)
- **Champs complexes :** Implémentation d'un champ permettant de gérer des listes d'objets dans le survey builder, avec affichage dans le summary et la vue de réponse. [#226](https://github.com/betagouv/sylvasan/pull/226), [#228](https://github.com/betagouv/sylvasan/pull/228)
- **Page Mon Compte :** Ajout d'une page "Mon Compte" affichant la source du compte utilisateur. [#224](https://github.com/betagouv/sylvasan/pull/224)
- **Vocabulaires :** Ajout de nouveaux vocabulaires et intégration de leur affichage dans l'application web et mobile. [#207](https://github.com/betagouv/sylvasan/pull/207), [#208](https://github.com/betagouv/sylvasan/pull/208)

### Évolutions techniques
- **Mises à jour de dépendances :** De nombreuses dépendances ont été mises à jour (Django, React, Vue.js, PostgreSQL, Vite, Sentry, ruff, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performances.
- **Refactoring :** Suppression de l'authentification par dump. [#206](https://github.com/betagouv/sylvasan/pull/206)
- **Tests :** Ajout de tests pour la connexion OAuth. [#212](https://github.com/betagouv/sylvasan/pull/212)
- **CI/CD :** Mise à jour des actions GitHub pour le CI/CD.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Configuration :** Rendre la configuration de la base de données DSF facultative.
- **Nettoyage de code :** Suppression de code inutilisé et amélioration de la lisibilité du code.
- **Metaschema :** Mise à jour du metaschema avec les derniers changements.
- **Pre-commit :** Mise à jour de la configuration pre-commit.
- **Correction de bugs :** Correction de bugs mineurs liés à l'affichage et au fonctionnement des formulaires.
