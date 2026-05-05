## Changelog : gallene-sdk (30 derniers jours, au 29 avril 2026)

### Résumé
Ce changelog reflète les débuts du développement du SDK Gallene. Les efforts se sont concentrés sur la mise en place de l'infrastructure initiale, l'implémentation de la connexion à l'API Gallene, et la gestion des tokens d'authentification.  Des tests unitaires sont en cours d'élaboration pour assurer la robustesse du SDK.

### Évolutions fonctionnelles
- Implémentation de la connexion à l'API Gallene avec gestion des tokens d'authentification.
- Ajout de la gestion des erreurs avec la classe `GaleneError`.
- Possibilité de spécifier les permissions sous forme de liste.

### Évolutions techniques
- Initialisation du projet avec un premier commit.
- Création du package pour appeler le SDK.
- Implémentation de `signal_client.py` et tests associés.
- Suppression du wrapper `galene-api-wrapper`.
- Ajout de nouvelles dépendances : `websockets` et `aiortc`.
- Utilisation de `respx` pour les tests (mock des requêtes HTTP).
- Mise en place d'une structure de tests avec `pytest`.

### Autres changements
- Ajout des fichiers initiaux du projet depuis un dépôt privé.
- Modifications diverses pour la configuration et l'organisation du code.
