## Changelog : sylvasan (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, les évolutions de SylvaSan se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de l'authentification via DSF, de nouvelles fonctionnalités pour la création d'enquêtes (champs conditionnels, autocomplétion, cartes), et la gestion des vocabulaires. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **Authentification DSF :** Implémentation de la connexion via DSF (DSF-ref), permettant aux utilisateurs de s'authentifier plus facilement. [#261](https://github.com/betagouv/sylvasan/pull/261)
- **Champs conditionnels :** Ajout de la possibilité de rendre l'affichage des champs conditionnel en fonction de valeurs d'autres champs. Cela permet de créer des enquêtes plus dynamiques et adaptées aux besoins. [#261](https://github.com/betagouv/sylvasan/pull/261)
- **Champ carte :** Intégration d'un nouveau type de champ permettant d'afficher une carte. Disponible sur le web et l'application mobile. [#226](https://github.com/betagouv/sylvasan/pull/226), [#208](https://github.com/betagouv/sylvasan/pull/208)
- **Champ autocomplétion :** Ajout d'un nouveau type de champ avec autocomplétion pour faciliter la saisie de données. [#209](https://github.com/betagouv/sylvasan/pull/209)
- **Gestion des vocabulaires :** Amélioration de la gestion des vocabulaires, avec l'ajout de nouveaux vocabulaires et la possibilité de les utiliser dans les enquêtes. [#207](https://github.com/betagouv/sylvasan/pull/207), [#208](https://github.com/betagouv/sylvasan/pull/208)
- **Page "Mon Compte" :** Ajout d'une page "Mon Compte" dans l'application web, affichant la source du compte utilisateur. [#228](https://github.com/betagouv/sylvasan/pull/228)
- **Affichage des données carto :** Affichage des données cartographiques dans le résumé.

### Évolutions techniques
- **Mises à jour de dépendances :** De nombreuses dépendances ont été mises à jour (Django, React, Vue.js, PostgreSQL, Python, npm, ruff, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performances.
- **Refactoring OAuth :** Amélioration de l'implémentation de l'authentification OAuth2.
- **Configuration DB DSF :** La configuration de la base de données DSF est maintenant facultative.
- **Pre-commit Ruff :** Mise à jour de la configuration de pre-commit pour utiliser la dernière version de Ruff.
- **Suppression de l'authentification par dump :** Suppression de l'authentification par dump.

### Autres changements
- Ajout des claims DSF dans le modèle de l'utilisateur.
- Ajout d'un toast d'erreur en cas d'erreur d'identification DSF.
- Amélioration de la gestion des erreurs et des états dans l'application mobile et web.
- Correction de bugs d'affichage et de positionnement.
- Ajout de tests pour la connexion OAuth.
- Mise à jour de la documentation.
- Suppression de props dépréciées dans TypeScript.
- Ajout de métadonnées pour les nouveaux champs.
- Amélioration de la synchronisation des pôles DSF.
