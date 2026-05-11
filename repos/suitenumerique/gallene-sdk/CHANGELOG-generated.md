## Changelog : gallene-sdk (30 derniers jours, au 29 avril 2026)

### Résumé
Ce changelog fait état des premiers développements du SDK Gallene. Les efforts se sont concentrés sur la mise en place de l'infrastructure initiale, l'implémentation de la gestion des tokens d'authentification et la création d'une base pour l'interaction avec l'API Gallene, notamment via l'ajout de nouvelles dépendances pour la gestion des websockets et de la communication en temps réel.

### Évolutions fonctionnelles
- Implémentation de la connexion à l'API Gallene avec authentification par token.
- Ajout de la gestion des permissions, qui doivent maintenant être fournies sous forme de liste.
- Création d'un package permettant d'appeler le SDK.
- Intégration de la gestion des erreurs avec l'ajout de la classe `GaleneError`.

### Évolutions techniques
- Ajout des dépendances `websockets` et `aiortc` pour supporter la communication en temps réel.
- Suppression du wrapper `galene-api-wrapper`.
- Mise en place d'une structure de tests initiale avec `pytest` et utilisation de `respx` pour le mocking des requêtes.
- Initialisation du projet et création du template SDK.
- Implémentation de la gestion de l'API côté client.

### Autres changements
- Ajout des fichiers initiaux du projet depuis un dépôt privé.
- Modifications diverses pour la gestion des clés d'authentification.
- Ajout de tests pour la gestion des tokens d'accès et des exceptions.
