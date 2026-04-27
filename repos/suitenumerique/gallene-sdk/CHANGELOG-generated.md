## Changelog : gallene-sdk (30 derniers jours, au 24 avril 2026)

### Résumé
Ce changelog reflète les débuts du développement du SDK Gallene. Les efforts se sont concentrés sur la mise en place de l'infrastructure de base, l'implémentation de la connexion à l'API Gallene, et la gestion des tokens d'authentification.  Des tests unitaires ont été ajoutés pour assurer la robustesse du code.

### Évolutions fonctionnelles
- Implémentation de la connexion à l'API Gallene via token.
- Gestion des erreurs avec la création d'une classe `GaleneError`.
- Mise en place d'une structure de base pour l'appel de l'API Gallene côté client.
- Les permissions doivent maintenant être passées sous forme de liste.

### Évolutions techniques
- Initialisation du projet et création du squelette du SDK.
- Ajout des dépendances `websockets` et `aiortc` pour la gestion des communications en temps réel.
- Suppression du wrapper `galene-api-wrapper` au profit d'une implémentation directe dans le SDK.
- Utilisation de `respx` pour les tests afin de simuler les requêtes à l'API Gallene.
- Ajout de tests unitaires pour la gestion des tokens d'accès et des exceptions.

### Autres changements
- Ajout des fichiers initiaux du projet depuis un dépôt privé.
- Création du package pour appeler le SDK.
- Ajout de `signal_client.py` et de ses tests associés.
- Modification de `__init__.py`.
