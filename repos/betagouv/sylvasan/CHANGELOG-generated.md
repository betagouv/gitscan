## Changelog : sylvasan (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, SylvaSan a bénéficié d'améliorations significatives en termes de gestion des images, d'authentification, et de fonctionnalités d'exportation et de filtrage des données. L'application a également été renforcée sur le plan de la sécurité et de la stabilité grâce à des mises à jour de dépendances. De nouvelles fonctionnalités comme le champ carte et les conditions d'affichage de champs ont été ajoutées, améliorant la flexibilité et la puissance de l'outil.

### Évolutions fonctionnelles
- **Authentification :** Implémentation de la connexion via OAuth2 avec DSF, permettant une authentification simplifiée et sécurisée. [#244](https://github.com/betagouv/sylvasan/pull/244)
- **Gestion des images :** Ajout d'un champ image avec galérie de visualisation, compression et stockage optimisé. Possibilité de supprimer une observation avec des images non sauvegardées. [#283](https://github.com/betagouv/sylvasan/pull/283), [#284](https://github.com/betagouv/sylvasan/pull/284), [#285](https://github.com/betagouv/sylvasan/pull/285), [#286](https://github.com/betagouv/sylvasan/pull/286)
- **Export des données :** Ajout de la fonctionnalité d'export des réponses avec un nombre de réponses affiché. [#262](https://github.com/betagouv/sylvasan/pull/262), [#263](https://github.com/betagouv/sylvasan/pull/263)
- **Filtrage :** Ajout d'un filtre par enquête dans l'interface utilisateur et le backend. [#287](https://github.com/betagouv/sylvasan/pull/287)
- **Champ carte :** Intégration d'un champ carte dans l'application web et mobile. [#226](https://github.com/betagouv/sylvasan/pull/226)
- **Conditions d'affichage :** Ajout de la possibilité de définir des conditions d'affichage pour les champs, rendant les formulaires plus dynamiques et adaptatifs. [#261](https://github.com/betagouv/sylvasan/pull/261)
- **Autocomplete :** Amélioration de l'autocomplétion pour ignorer les accents et les caractères spéciaux, et fermeture avec la touche Échap. [#262](https://github.com/betagouv/sylvasan/pull/262)

### Évolutions techniques
- **Django Storages :** Intégration de Django Storages pour une gestion plus flexible du stockage des fichiers. [#285](https://github.com/betagouv/sylvasan/pull/285)
- **Mises à jour de dépendances :** Mises à jour régulières des dépendances (Django, React, Vue.js, PostgreSQL, npm, Python, Ruff) pour assurer la sécurité et la stabilité de l'application.
- **Refactoring :** Restructuration de pages et composants web, ajout d'ADR (Architecture Decision Records) pour documenter les choix techniques.
- **Tests :** Ajout de tests pour la connexion OAuth.
- **Pre-commit :** Mise à jour du fichier pre-commit.

### Autres changements
- Ajout de la page "Mon compte" avec l'affichage de la source du compte DSF.
- Ajout de la synchronisation des pôles DSF.
- Amélioration de l'affichage des labels pour les vocabulaires web.
- Ajout de vocabulaires additionnels.
- Correction de bugs et amélioration de l'expérience utilisateur.
- Ajout d'informations sur la source du compte dans la page "Mon compte".
- Affichage des données cartographiques dans le résumé.
- Suppression de l'authentification par dump.
- Ajout de spinners et désactivation des boutons pendant les opérations.
- Ajout de l'affichage de la latitude et longitude.
