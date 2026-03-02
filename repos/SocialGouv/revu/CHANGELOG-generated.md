## Changelog : revu (30 derniers jours)

### Résumé
Les dernières mises à jour de Revu se concentrent sur la correction de bugs et l'amélioration de la stabilité de l'application. Plusieurs corrections ont été apportées pour résoudre des erreurs dans la gestion des revues de code, des problèmes de volume temporaire et des fuites d'erreurs. Une mise à jour du modèle Anthropic utilisé pour l'analyse a également été effectuée.

### Évolutions fonctionnelles
*   Correction d'une fuite d'erreurs lors des revues de code ([#276](https://github.com/SocialGouv/revu/issues/276)).
*   Correction de problèmes liés au volume temporaire utilisé par l'application ([#274](https://github.com/SocialGouv/revu/issues/274)).
*   Correction d'un problème de suggestions redondantes ([#271](https://github.com/SocialGouv/revu/issues/271)).

### Évolutions techniques
*   Mise à jour de la version du modèle Anthropic dans la configuration.
*   Migration vers pnpm pour la gestion des paquets ([#268](https://github.com/SocialGouv/revu/issues/268)).
*   Amélioration de la gestion des erreurs et du débogage.
*   Correction d'une discordance entre les lignes de début et de fin dans l'analyse du code ([#269](https://github.com/SocialGouv/revu/issues/269)).

### Autres changements
*   Correction du pre-commit TSC ([#269](https://github.com/SocialGouv/revu/issues/269)).
*   Travaux en cours sur l'intégration d'OpenAI pour les revues de code ([#274](https://github.com/SocialGouv/revu/issues/274)).
*   Mise à jour de la version de l'application (1.37.24).
