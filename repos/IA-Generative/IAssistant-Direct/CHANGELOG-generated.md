## Changelog : IAssistant-Direct (30 derniers jours, au 31 mai 2026)

### Résumé
Cette mise à jour majeure apporte des améliorations significatives à l'expérience utilisateur, notamment un assistant d'onboarding pour les nouveaux utilisateurs et une meilleure compatibilité avec différents environnements réseau. Le projet a également été renommé et bénéficie d'une gestion améliorée des sessions hors ligne et d'un accès direct pour les utilisateurs DGX.

### Évolutions fonctionnelles
- Ajout d'une page de bienvenue pour guider les nouveaux utilisateurs lors du premier lancement de l'extension. [#1](https://github.com/IA-Generative/IAssistant-Direct/pull/1)
- Amélioration de la compatibilité avec les environnements intranet et internet pour la communication (COMU).
- L'extension injecte maintenant le content script sur `comu.din.gouv.fr` pour une meilleure prise en charge.
- Renommage de l'extension en IAssistant-Direct.
- Implémentation d'un accès direct pour les utilisateurs DGX.
- Nouvelle mascotte Mirai remplace l'ancienne image de l'extension.

### Évolutions techniques
- Correction d'un problème avec l'URL Keycloak, permettant une configuration plus flexible.
- Suppression de la nécessité de configurer `bootstrap_url` et `relayAssistantBaseUrl` dans la configuration servie.
- Amélioration de la gestion des sessions hors ligne, avec une durée de validité de 6 mois.

### Autres changements
- Mise à jour de la version de l'extension à v1.2.3.
- Ajout d'un wizard d'onboarding pour une expérience utilisateur plus guidée.
