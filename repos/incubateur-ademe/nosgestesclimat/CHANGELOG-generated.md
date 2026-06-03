## Changelog : nosgestesclimat (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de la précision des données (notamment concernant le DPE et les bornes de recharge), et l'ajout de traductions pour une meilleure expérience utilisateur. Des ajustements ont également été apportés pour préparer une future fonctionnalité liée aux établissements scolaires.

### Évolutions fonctionnelles
- Correction de la valeur par défaut dans un certain contexte, évitant ainsi des comportements inattendus. [#2767](https://github.com/incubateur-ademe/nosgestesclimat/issues/2767)
- Amélioration de la gestion de la consommation électrique liée au Diagnostic de Performance Énergétique (DPE). [#2768](https://github.com/incubateur-ademe/nosgestesclimat/issues/2768)
- Suppression de l'action JVA (Juste Valeur Agricole) dans l'interface. [#2766](https://github.com/incubateur-ademe/nosgestesclimat/issues/2766)
- Suppression de la question relative au biogaz pour le chauffage. [#2765](https://github.com/incubateur-ademe/nosgestesclimat/issues/2765)
- Suppression des Véhicules d'Assistance Électrique (VAE) de la question sur les transports.
- Simplification des options de chauffage proposées.
- Ajout de scripts de test pour les "bornes" de recharge. [#2766](https://github.com/incubateur-ademe/nosgestesclimat/issues/2766)
- Amélioration de la documentation rapide (quick doc). [#2758](https://github.com/incubateur-ademe/nosgestesclimat/issues/2758)

### Évolutions techniques
- Mise à jour des données d'écobalyses réglementaires (ED-fr.publicodes). [#2738](https://github.com/incubateur-ademe/nosgestesclimat/issues/2738) et [#2759](https://github.com/incubateur-ademe/nosgestesclimat/issues/2759)
- Suppression de la langue espagnole (es) des langues supportées. [#2759](https://github.com/incubateur-ademe/nosgestesclimat/issues/2759)
- Préparation d'une fonctionnalité pour les établissements scolaires (POC). [#2740](https://github.com/incubateur-ademe/nosgestesclimat/issues/2740)
- Suppression de la librairie axios.

### Autres changements
- Ajout et correction de traductions dans plusieurs langues.
- Amélioration du wording (libellés) dans l'interface utilisateur.
- Corrections de tests et de la configuration.
- Plusieurs merges de branches de préproduction vers la branche principale.
