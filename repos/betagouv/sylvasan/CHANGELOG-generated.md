## Changelog : sylvasan (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, SylvaSan a bénéficié d'améliorations significatives concernant la gestion des enquêtes, notamment l'ajout de brouillons multiples, un résumé des réponses envoyées, et l'intégration de nouveaux champs de type "carte" et "liste d'objets" dans le constructeur d'enquêtes. Des mises à jour de sécurité et des dépendances ont également été effectuées pour assurer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de sauvegarder plusieurs brouillons par enquête [#172](https://github.com/betagouv/sylvasan/issues/172).
- Implémentation d'un composant de résumé des réponses envoyées pour une meilleure visualisation des données [#173](https://github.com/betagouv/sylvasan/issues/173).
- Intégration d'un champ de type "carte" dans le web et le mobile, permettant d'afficher des informations géographiques [#226](https://github.com/betagouv/sylvasan/issues/226), [#227](https://github.com/betagouv/sylvasan/issues/227).
- Ajout d'un champ de type "liste d'objets" dans le constructeur d'enquêtes, offrant plus de flexibilité dans la collecte de données [#190](https://github.com/betagouv/sylvasan/issues/190).
- Ajout d'une modal/toast pour l'application mobile pour améliorer l'expérience utilisateur [#191](https://github.com/betagouv/sylvasan/issues/191).
- Intégration de nouveaux vocabulaires pour enrichir les données collectées [#189](https://github.com/betagouv/sylvasan/issues/189), [#208](https://github.com/betagouv/sylvasan/issues/208).

### Évolutions techniques
- Mise à jour de nombreuses dépendances (Django, React, Vue.js, PostgreSQL, Vite, Sentry, ruff, etc.) pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
- Amélioration de la configuration de la base de données DSF, la rendant facultative.
- Mise à jour de la sécurité avec des correctifs et des dépendances à jour [#226](https://github.com/betagouv/sylvasan/issues/226).
- Refonte de l'authentification avec DSF-ref.
- Utilisation de TypeScript 6.0.3.
- Mise à jour de Vite et Vitest.

### Autres changements
- Ajout de messages d'information sur les champs array.
- Amélioration de l'affichage des champs array dans le summary et la vue réponse.
- Correction de bugs et améliorations de la performance.
- Mise à jour de la documentation.
- Ajustements UI dans la liste d'observations.
- Suppression de props dépréciées.
- Ajout de tests unitaires.
