## Changelog : waf-base (30 derniers jours, au 16 novembre 2026)

### Résumé
Ce mois-ci marque le lancement opérationnel de l'image de base du WAF. Le projet dispose désormais de ses outils de commande principaux, de ses processus d'automatisation (CI/CD) et de correctifs initiaux pour stabiliser le provisionnement et l'accès réseau.

### Évolutions fonctionnelles
- Introduction des commandes `wafgen check` et `wafgen run` pour la gestion du WAF [#1](https://github.com/incubateur-ademe/waf-base/issues/1).
- Correction d'un problème de refus de connexion lié au firewall Scalingo [#4](https://github.com/incubateur-ademe/waf-base/issues/4).

### Évolutions techniques
- Mise en place de l'image de base, des workflows de CI/CD et du processus de release [#1](https://github.com/incubateur-ademe/waf-base/issues/1).
- Extension des capacités de provisionnement avec le support de l'image `waf-ops` et du mode "jumeau -1" [#5](https://github.com/incubateur-ademe/waf-base/issues/5).
- Fiabilisation du provisionnement via la correction des variables partagées vides et des références conditionnelles [#6](https://github.com/incubateur-ademe/waf-base/issues/6).
- Ajustement du processus de linting pour reconstruire la base depuis les sources afin de contourner les restrictions d'accès au registre GHCR [#2](https://github.com/incubateur-ademe/waf-base/issues/2).

### Autres changements
- Création de la documentation initiale (README).
- Mise à jour de l'inventaire concernant le service `waf-pilote` [#3](https://github.com/incubateur-ademe/waf-base/issues/3).
