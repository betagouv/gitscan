## Changelog : simple-border-gateway (30 derniers jours, au 07/10/2026)

### Résumé
Les récentes évolutions se sont concentrées sur le renforcement de la sécurité des échanges, l'amélioration de la fiabilité de la configuration et l'optimisation des performances globales, notamment lors du routage des requêtes et du processus de déploiement.

### Évolutions fonctionnelles
- **Sécurité et conformité** : Renforcement de la gestion HTTP via l'interdiction des redirections, l'ajout de timeouts sur le client HTTP, la validation de l'en-tête `X-Matrix` et le nettoyage de l'en-tête `Host`. Une meilleure distinction des erreurs lors de la lecture du corps des requêtes a également été implémentée.
- **Gestion de la configuration** : Amélioration de la robustesse grâce à une validation complète des fichiers de configuration avant tout redémarrage de service et support des méthodes HTTP en minuscules dans les fichiers de configuration.
- **Routage et Proxy** : Amélioration du support et de l'authentification des proxys amont (upstream) et correction de la confusion sur les options de commande `--inbound/outbound-only`.

### Évolutions techniques
- **Optimisation des performances** : Remplacement des expressions régulières par `matchit` pour le routage ([#16](https://github.com/tchapgouv/simple-border-gateway/pull/16)), réduction des copies de buffers lors de la vérification de signature et déportation des appels DNS bloquants vers un pool dédié. L'utilisation de `Arc` pour l'état du gateway permet également d'éviter des copies inutiles à chaque requête.
- **Architecture et code** : Refactorisation pour séparer la logique CLI des services, simplification des helpers de conversion et passage à l'édition Rust 2024.
- **CI/CD et déploiement** : Optimisation significative des temps de build, amélioration du Dockerfile et intégration du cache Docker pour les GitHub Actions.

### Autres changements
- Nettoyage du code (formatage) et correction de fautes de frappe.
