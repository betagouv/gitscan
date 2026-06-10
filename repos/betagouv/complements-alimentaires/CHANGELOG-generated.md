## Changelog : complements-alimentaires (30 derniers jours, au 01 juin 2026)

### Résumé
Ce changelog couvre une période d'amélioration continue du projet, avec un accent particulier sur l'expérience utilisateur dans la gestion des décisions de visa. Des corrections et des améliorations ont été apportées à l'interface, notamment pour la persistance des décisions et la visibilité des informations.  De nombreuses mises à jour de dépendances ont également été intégrées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Amélioration de l'interface de modification de la décision de visa : pré-remplissage des valeurs et persistance de la décision lors de la navigation. [#2947](https://github.com/betagouv/complements-alimentaires/issues/2947)
- Correction d'un bug empêchant la visibilité du délai de réponse. [#2945](https://github.com/betagouv/complements-alimentaires/issues/2945)
- Adaptation de la grille de colonnes dans VisaValidationSegment pour une meilleure réactivité.
- Suppression des champs relatifs aux plantes pour les types de produits qui ne sont pas des plantes. [#2921](https://github.com/betagouv/complements-alimentaires/issues/2921) et [#2908](https://github.com/betagouv/complements-alimentaires/issues/2908)

### Évolutions techniques
- Mise à jour de nombreuses dépendances frontend (React, Vue.js, TypeScript, webpack, postcss, etc.) et backend (Django, Python, PostgreSQL, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Suppression de l'utilisation de `ipdb` et ajout de dépendances manquantes. [#2932](https://github.com/betagouv/complements-alimentaires/issues/2932)
- Amélioration de l'audit du code pour identifier les composants utilisant `v-for` qui devraient utiliser des listes HTML.

### Autres changements
- Ajustements de marges et d'espacement dans l'interface utilisateur.
- Renommage et refactorisation de composants liés au formulaire de modification de la décision de visa.
- Mise à jour de la documentation et de la configuration du projet.
