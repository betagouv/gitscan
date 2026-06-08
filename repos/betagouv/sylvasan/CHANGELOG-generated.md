## Changelog : sylvasan (30 derniers jours, au 06 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'authentification via DSF, l'ajout d'un nouveau champ de type carte, et l'amélioration de l'expérience utilisateur mobile. Des corrections de bugs et des optimisations ont également été apportées, notamment concernant l'export des réponses et la gestion des champs conditionnels.

### Évolutions fonctionnelles
- **Authentification DSF :** Implémentation de la connexion via OAuth2 avec DSF, tant sur le web que sur l'application mobile. [#244](https://github.com/betagouv/sylvasan/pulls/244)
- **Nouveau champ Carte :** Ajout d'un nouveau type de champ "Carte" permettant d'afficher des données géographiques. [#285](https://github.com/betagouv/sylvasan/pulls/285)
- **Export des réponses :** Amélioration de l'export des réponses, avec notamment l'ajout du nombre total de réponses. [#280](https://github.com/betagouv/sylvasan/pulls/280)
- **Filtres :** Ajout d'un filtre par enquête pour affiner les résultats. [#287](https://github.com/betagouv/sylvasan/pulls/287)
- **Champs conditionnels :** Implémentation de champs conditionnels, permettant d'afficher ou de masquer des champs en fonction de certaines conditions. [#261](https://github.com/betagouv/sylvasan/pulls/261)
- **Mon compte :** Ajout d'une page "Mon compte" avec les informations de l'utilisateur, notamment la source de son compte.
- **Autocomplete :** Amélioration de l'autocomplete pour ignorer les accents et caractères spéciaux. [#262](https://github.com/betagouv/sylvasan/pulls/262)
- **Gestion des observations :** Possibilité de supprimer une observation non sauvegardée dans le backend.

### Évolutions techniques
- **Mise à jour des dépendances :** Mise à jour de nombreuses dépendances (Django, PostgreSQL, React, Vue.js, Python, npm, ruff) pour bénéficier des dernières corrections et améliorations de sécurité.
- **Refactoring :** Restructuration des pages et composants web.
- **Amélioration des tests :** Ajout de tests pour l'authentification OAuth.
- **Configuration :** Ajout de variables d'environnement pour la configuration OAuth.
- **Stockage des images :** Utilisation de Django Storages pour la gestion du stockage des images.
- **Compression des images :** Compression de la taille des images pour optimiser les performances.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Correction de bugs :** Correction de plusieurs bugs, notamment concernant l'affichage des champs, la gestion de la session et les warnings Typescript.
- **Améliorations UI :** Ajustements de l'interface utilisateur, notamment sur mobile.
- **Synchronisation DSF :** Ajout de la synchronisation des pôles DSF.
- **Affichage des coordonnées :** Affichage des coordonnées géographiques dans le résumé.
- **Version Android :** Publication de nouvelles versions de l'application Android (0.0.8 et 0.0.10).
