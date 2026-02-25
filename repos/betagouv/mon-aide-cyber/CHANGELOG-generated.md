## Changelog : mon-aide-cyber (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées à MonAideCyber. Les modifications incluent des mises à jour de sécurité pour corriger des vulnérabilités, des améliorations pour le processus de devenir aidant, et des ajustements pour faciliter la mise en relation entre les demandeurs et les aidants. Des encarts de contact ont également été ajoutés pour faciliter l'assistance aux utilisateurs.

### Évolutions fonctionnelles
- Amélioration du processus "Devenir aidant" : le lien du mail de contact MAC a été remplacé par un lien vers la page des relais associatifs. (#5d80e72)
- Mise en relation aidants-demandeurs : implémentation de la récupération des aidants par SIRET et de la mise en relation pour une organisation. (#2373273, #d9c4157, #0d63da4)
- Ajout d'encarts de contact : des encarts de contact ont été ajoutés pour faciliter la communication concernant les fonctionnalités et la sécurité de MonAideCyber. (#619c732, #f1cb1d0)

### Évolutions techniques
- Mise à jour de dépendances de sécurité :
  - Axios a été mis à jour pour corriger une vulnérabilité. (#12b2f07)
  - cookie-session a été mis à jour pour corriger une vulnérabilité. (#b25c4b1)
  - lodash a été mis à jour pour corriger une vulnérabilité. (#21a98cd)
- Préparation de la migration Clever Cloud : mise à jour du bandeau de maintenance. (#b296192)

### Autres changements
- Bump de la dépendance `qs` de la version 6.14.1 à 6.14.2. (#06c8027)
