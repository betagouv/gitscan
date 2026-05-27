## Changelog : sylvasan (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, SylvaSan a bénéficié d'améliorations significatives en termes de sécurité et d'expérience utilisateur. L'authentification via DSF-ref est désormais possible, facilitant l'accès pour les agents de l'administration. Des fonctionnalités d'export de données ont été ajoutées, ainsi que des améliorations concernant l'affichage et la manipulation des données, notamment avec l'ajout de champs conditionnels et de cartes. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- **Authentification DSF-ref :** Implémentation de la connexion via DSF-ref pour les utilisateurs, améliorant l'accès et la sécurité. [#244](https://github.com/betagouv/sylvasan/pull/244)
- **Export des réponses :** Ajout de la possibilité d'exporter les réponses aux enquêtes, avec un nombre de réponses par défaut configurable. [#263](https://github.com/betagouv/sylvasan/pull/263), [#273](https://github.com/betagouv/sylvasan/pull/273)
- **Filtres pour les réponses :** Premiers filtres implémentés pour la page des réponses, permettant une meilleure organisation et recherche.
- **Pagination des réponses :** Ajout d'une pagination pour faciliter la consultation des réponses.
- **Champs conditionnels :** Possibilité de rendre l'affichage de certains champs conditionnel en fonction de la valeur d'autres champs. [#261](https://github.com/betagouv/sylvasan/pull/261)
- **Champ carte :** Ajout d'un nouveau type de champ "carte" pour l'intégration de données géographiques, disponible sur le web et l'application mobile. [#226](https://github.com/betagouv/sylvasan/pull/226)
- **Vocabulaires :** Intégration de nouveaux vocabulaires et amélioration de leur gestion, avec affichage dans le renderer et le survey builder. [#208](https://github.com/betagouv/sylvasan/pull/208), [#207](https://github.com/betagouv/sylvasan/pull/207)
- **Page "Mon compte" :** Ajout d'une page "Mon compte" avec l'affichage de la source du compte (DSF).
- **Autocomplete :** Amélioration de l'autocomplete avec gestion des accents et fermeture via la touche Échap. [#262](https://github.com/betagouv/sylvasan/pull/262)

### Évolutions techniques
- **Refactoring de la structure web :** Restructuration des pages et composants web, avec ajout d'un ADR (Architecture Decision Record).
- **Mises à jour de dépendances :** De nombreuses dépendances ont été mises à jour (Django, React, Vue.js, PostgreSQL, npm, Python, ruff, etc.) pour assurer la sécurité et la stabilité de la plateforme. (voir commits dependabot)
- **Amélioration de la gestion des erreurs :** Correction de bugs et amélioration de la gestion des erreurs.
- **Synchronisation des vocabulaires :** Amélioration de la synchronisation des vocabulaires.
- **Configuration OAuth :** Ajout de valeurs par défaut pour les variables d'environnement OAuth.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Configuration pre-commit :** Mise à jour de la configuration pre-commit pour Ruff.
- **Correction de warnings :** Résolution de warnings dans le code.
- **Affichage des coordonnées géographiques :** Affichage des coordonnées géographiques dans le summary.
- **Amélioration de l'UX :** Diverses améliorations de l'expérience utilisateur, notamment l'ajout de spinners et la correction de problèmes d'affichage.
