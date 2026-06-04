## Changelog : sylvasan (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les évolutions de SylvaSan se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de la connexion via l'authentification DSF, l'implémentation d'un champ carte, et l'ajout de la possibilité d'exporter les réponses aux enquêtes. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **Authentification :** Implémentation de la connexion via l'authentification DSF pour le web et l'application mobile. [#244](https://github.com/betagouv/sylvasan/pulls/244)
- **Champ Carte :** Ajout d'un nouveau champ de type carte, permettant la visualisation et la saisie de données géographiques.  Implémentation sur le web et l'application mobile. [#226](https://github.com/betagouv/sylvasan/pulls/226)
- **Export de réponses :** Possibilité d'exporter les réponses aux enquêtes. [#287](https://github.com/betagouv/sylvasan/pulls/287)
- **Filtres :** Ajout d'un filtre par enquête pour affiner les résultats. [#287](https://github.com/betagouv/sylvasan/pulls/287)
- **Autocomplete :** Amélioration de l'autocomplete pour ignorer les accents et caractères spéciaux. [#262](https://github.com/betagouv/sylvasan/pulls/262)
- **Mon Compte :** Ajout d'une page "Mon Compte" affichant la source du compte utilisateur.
- **Affichage Cartographique :** Affichage des données cartographiques dans le résumé.

### Évolutions techniques
- **Django Storages :** Intégration de Django Storages pour la gestion du stockage des fichiers. [#285](https://github.com/betagouv/sylvasan/pulls/285)
- **Mise à jour des dépendances :** De nombreuses dépendances ont été mises à jour (Django, PostgreSQL, React, Vue.js, Python, npm, Django Storages, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- **Refactoring :** Restructuration des pages et composants web.
- **Tests :** Ajout de tests pour la connexion OAuth et le champ carte.
- **Pre-commit :** Mise à jour de la configuration de pre-commit avec la dernière version de ruff.

### Autres changements
- **Vocabulaires :** Synchronisation des vocabulaires DSF et ajout de vocabulaires additionnels. [#225](https://github.com/betagouv/sylvasan/pulls/225)
- **Documentation :** Mise à jour de la documentation.
- **Correction de bugs :** Correction de bugs concernant l'affichage des champs, le type de champ lors de l'édition, et la gestion de la session après un redémarrage sans connexion.
- **Améliorations UI :** Ajustements de l'interface utilisateur sur le web et l'application mobile.
- **Version Android :** Publication de nouvelles versions de l'application Android (0.0.8 et 0.0.10).
