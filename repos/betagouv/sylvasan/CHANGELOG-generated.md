## Changelog : sylvasan (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment en ajoutant la gestion des champs conditionnels dans les formulaires, en améliorant l'authentification avec DSF, et en ajoutant des champs de type carte. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- **Authentification DSF :** Implémentation de la connexion via DSF (DSF-ref), avec gestion des erreurs et affichage de la source du compte utilisateur [#260](https://github.com/betagouv/sylvasan/pull/260).
- **Champs conditionnels :** Ajout de la possibilité de définir des conditions d'affichage pour les champs dans les formulaires, avec les opérateurs "contains" et "not\_contains" [#261](https://github.com/betagouv/sylvasan/pull/261).
- **Champ carte :** Intégration d'un champ de type carte dans le constructeur de formulaire et affichage des données cartographiques dans le résumé des réponses [#226](https://github.com/betagouv/sylvasan/pull/226).
- **Vocabulaires :** Ajout de la gestion de nouveaux vocabulaires et intégration dans le constructeur de formulaire et l'affichage des données [#208](https://github.com/betagouv/sylvasan/pull/208).
- **Modal mobile :** Ajout d'une modal/toast pour l'application mobile afin d'améliorer l'expérience utilisateur.
- **Champs Array :** Amélioration de l'affichage et de la gestion des champs de type array (listes d'objets) dans le constructeur de formulaire et les vues de réponse.

### Évolutions techniques
- **Mise à jour des dépendances :** De nombreuses dépendances ont été mises à jour, notamment Django, React, Vue.js, PostgreSQL, et diverses bibliothèques Python et JavaScript, pour améliorer la sécurité et la stabilité du projet.
- **Refactoring :** Amélioration de la structure du code et suppression de code obsolète.
- **Configuration DB DSF :** La configuration de la base de données DSF est maintenant facultative.
- **Pré-commit :** Mise à jour de la configuration pre-commit pour utiliser la dernière version de Ruff.

### Autres changements
- Ajout de la synchronisation des pôles DSF.
- Ajout de la page "Mon Compte" dans l'application web, affichant la source du compte utilisateur.
- Correction de bugs d'affichage et amélioration de l'interface utilisateur.
- Amélioration des tests pour l'authentification OAuth.
- Mise à jour de la documentation.
