## Changelog : IAssistant-Direct (30 derniers jours, au 31 mai 2026)

### Résumé
Cette mise à jour majeure apporte des améliorations significatives à l'expérience utilisateur, notamment un assistant d'onboarding pour les nouveaux utilisateurs et une meilleure gestion de l'authentification. Le projet a également été renommé et bénéficie d'un accès direct pour les utilisateurs DGX, avec une session offline prolongée à 6 mois.

### Évolutions fonctionnelles
- **Onboarding utilisateur :** Ajout d'une page de bienvenue et d'un wizard d'onboarding pour guider les nouveaux utilisateurs lors du premier lancement [#1](https://github.com/IA-Generative/IAssistant-Direct/pull/1).
- **Authentification :** Correction d'un problème avec l'URL Keycloak, permettant une meilleure compatibilité avec différentes configurations.
- **Support COMU :** Amélioration du support pour les environnements COMU, avec la prise en charge de deux URLs (internet et intranet) et l'injection du content script sur comu.din.gouv.fr.
- **Renommage et accès DGX :** L'extension a été renommée en IAssistant-Direct et offre désormais un accès direct aux utilisateurs DGX.
- **Session Offline :** La durée de la session offline a été étendue à 6 mois.
- **Nouvelle image :** L'ancienne image a été remplacée par la mascotte Mirai.

### Évolutions techniques
- **Configuration :** Suppression de la nécessité de spécifier `bootstrap_url` et `relayAssistantBaseUrl` dans la configuration servie.
- **Refactoring :** Renommage du projet et ajustements associés.

### Autres changements
- Aucune information supplémentaire disponible.
