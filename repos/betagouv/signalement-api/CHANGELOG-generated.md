## Changelog : signalement-api (30 derniers jours)

### Résumé
Les récentes évolutions de l'API SignalConso se concentrent sur l'amélioration de la robustesse et de la gestion des ressources, notamment en production. Des corrections ont été apportées pour gérer correctement les limites de taille des requêtes et les alertes de consommation de ressources.

### Évolutions fonctionnelles
- Correction d'un problème de limite de taille du parser de corps de requête, permettant de traiter des signalements plus volumineux. (#2015)
- Ajustement du seuil d'alerte pour les uploads de fichiers, améliorant la surveillance de l'utilisation des ressources. (#2012)

### Évolutions techniques
- Configuration de la mémoire JVM (Xmx et Xms) en production pour une meilleure gestion des ressources. (#2013)
- Suppression des logs d'erreur inutiles lors de l'absence de paiement pour Social Blade. (#2010)
- Correction de problèmes de linting et de noms de fichiers exportés. (#2017)
- Ignorer les alertes Albert lorsque la limite d'utilisation est atteinte. (#2011)

### Autres changements
- Préparation pour des tests de mémoire en production. (#2021, #2019)
