## Changelog : ami-notifications-api (30 derniers jours, au 2026-04-29)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment autour de la gestion des préférences de l'utilisateur et de l'affichage des informations, ainsi que par des travaux importants sur la gestion des agents et des accès. Des corrections de bugs et des optimisations de performance ont également été apportées. Enfin, des travaux ont été réalisés pour améliorer la robustesse et la maintenabilité du code.

### Évolutions fonctionnelles
- **Gestion des préférences utilisateur :** Ajout de la gestion des zones de vacances scolaires pour personnaliser l'affichage de l'agenda. L'utilisateur peut désormais sélectionner ses zones préférées et les adresses associées. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Amélioration de l'interface utilisateur :**
    - Correction du comportement de défilement sur la page d'adresse, notamment lors de la focalisation sur le champ de saisie. [#568](https://github.com/numerique-gouv/ami-notifications-api/issues/568)
    - Ajout d'en-têtes fixes pour une meilleure navigation. [#568](https://github.com/numerique-gouv/ami-notifications-api/issues/568)
    - Centrage vertical du bouton FranceConnect. [#515](https://github.com/numerique-gouv/ami-notifications-api/issues/515)
    - Amélioration de l'affichage des notifications planifiées et correction des en-têtes POST. [#782](https://github.com/numerique-gouv/ami-notifications-api/issues/782)
- **Gestion des agents et des accès :**
    - Ajout d'une page de gestion des accès pour les administrateurs, permettant de gérer les agents et leurs rôles. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
    - Création d'un modèle Agent et implémentation des rôles d'agent et d'administrateur. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
    - Ajout d'un audit des actions réalisées par les agents. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- **Confirmation de déconnexion :** Ajout d'une modal de confirmation lors de la déconnexion. [#753](https://github.com/numerique-gouv/ami-notifications-api/issues/753)
- **Affichage de l'agenda :** L'agenda n'est plus accessible qu'aux utilisateurs connectés. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)

### Évolutions techniques
- **Réplication de la base de données :** Ajout de commandes et de tests pour la réplication de la base de données. [#791](https://github.com/numerique-gouv/ami-notifications-api/issues/791)
- **Cache HTTP :** Ajout de cache pour les requêtes GET avec `httpx`. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Refactoring API :** Déplacement des endpoints agenda et follow-p sous `/api/v1`. [#762](https://github.com/numerique-gouv/ami-notifications-api/issues/762)
- **Configuration :** Migration des variables d'environnement vers les fichiers de configuration Django. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- **Linting :** Correction de plusieurs avertissements de linting dans le code frontend. [#792](https://github.com/numerique-gouv/ami-notifications-api/issues/792)
- **Amélioration des logs :** Ajout des headers dans les logs d'erreurs d'API Part.
- **Suppression de code obsolète :** Suppression de `django-admin` et simplification des commandes pour les notifications planifiées. [#795](https://github.com/numerique-gouv/ami-notifications-api/issues/795) et [#786](https://github.com/numerique-gouv/ami-notifications-api/issues/786)

### Autres changements
- Mise à jour de plusieurs dépendances : `python-dotenv`, `lxml`, `uvicorn`, `pytest`, `cryptography`, `pygments`, `@sveltejs/kit`, `uuid`.
- Correction de l'URL `SECTOR_IDENTIFIER_URL` dans les paramètres. [#747](https://github.com/numerique-gouv/ami-notifications-api/issues/747)
- Ajout d'emojis pour les vacances scolaires. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- Correction d'un bug empêchant l'affichage correct des zones. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
