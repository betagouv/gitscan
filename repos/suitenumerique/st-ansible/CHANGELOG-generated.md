## Changelog : st-ansible (30 derniers jours, au 12 juin 2026)

### Résumé
Cette mise à jour apporte des corrections et améliorations concernant le déploiement et la configuration des applications *meet* et *keycloak*. Les modifications concernent notamment la gestion des utilisateurs Docker, la configuration des ports pour les défis ACME de Caddy, et la compatibilité de Keycloak avec des configurations en cluster. Une correction a également été apportée à la commande de démarrage des workers pour l'application *messages*.

### Évolutions fonctionnelles
- Correction d'un problème d'utilisateur dans le Dockerfile de l'application *meet* [#issue](https://github.com/suitenumerique/st-ansible/issues/).
- Correction de la configuration des ports pour les défis ACME de Caddy dans *meet*, permettant une obtention de certificats SSL/TLS fonctionnelle.
- Correction de la configuration de Keycloak pour les environnements en cluster [#issue](https://github.com/suitenumerique/st-ansible/issues/).
- Correction de la commande de démarrage des workers pour l'application *messages*.

### Évolutions techniques
- Amélioration de la documentation concernant la gestion des retours en arrière (rollbacks).

### Autres changements
- Aucune information disponible.
