## Changelog : karfur (30 derniers jours, au 8 juin 2026)

### Résumé
Cette période a été marquée par des corrections de bugs et des améliorations de la robustesse de l'application, notamment concernant la gestion des doublons, l'affichage des informations et la sécurité. Des travaux ont également été réalisés pour faciliter l'exportation des données documentaires et la préparation de l'intégration avec Letta Cloud. Enfin, des mises à jour de la documentation et de la configuration ont été effectuées.

### Évolutions fonctionnelles
- Correction de l'affichage des adresses postales incomplètes sur les fiches RCO. [#3778](https://github.com/refugies-info/karfur/pull/3778)
- Amélioration de l'affichage des villes sélectionnées dans la recherche, même après un rafraîchissement de la page. [#3769](https://github.com/refugies-info/karfur/pull/3769)
- Correction de l'affichage des accents dans le moteur de recherche. [#3769](https://github.com/refugies-info/karfur/pull/3769)
- Mise à jour des mentions légales sur le site et l'application. [#3785](https://github.com/refugies-info/karfur/pull/3785)
- Suppression du badge et des éléments liés à l'ancien RCO (Référentiel Commun d'Offres) de l'interface. [#3784](https://github.com/refugies-info/karfur/pull/3784) [#3780](https://github.com/refugies-info/karfur/pull/3780)
- Correction de l'affichage des labels de département qui pouvaient masquer les pop-ups. [#3766](https://github.com/refugies-info/karfur/pull/3766)
- Amélioration de la réactivité de la page d'accueil et de la page de connexion sur mobile. [#3767](https://github.com/refugies-info/karfur/pull/3767)
- Correction de problèmes d'affichage sur mobile. [#3773](https://github.com/refugies-info/karfur/pull/3773)

### Évolutions techniques
- Implémentation d'un endpoint pour la détection de doublons d'agents. [#3754](https://github.com/refugies-info/karfur/pull/3754)
- Amélioration de la logique de scoring des doublons pour une meilleure précision. [#3754](https://github.com/refugies-info/karfur/pull/3754)
- Préparation de l'exportation des ressources documentaires pour Letta Cloud, incluant la normalisation des données. [#3788](https://github.com/refugies-info/karfur/pull/3788) [#3786](https://github.com/refugies-info/karfur/pull/3786)
- Documentation de la structure de données "agent-knowledge" pour Letta Cloud. [#3782](https://github.com/refugies-info/karfur/pull/3782)
- Correction de bugs liés à la gestion des valeurs nulles et à la sécurité.
- Ajout de scans de vulnérabilités des dépendances avec pre-push hooks. [#3779](https://github.com/refugies-info/karfur/pull/3779)
- Mise à jour des dépendances et des outils de développement.

### Autres changements
- Clarification de la documentation concernant les chemins d'exportation Letta Cloud. [#3788](https://github.com/refugies-info/karfur/pull/3788)
- Ajout d'un nouveau membre à l'équipe. [#3777](https://github.com/refugies-info/karfur/pull/3777)
- Amélioration des messages de log pour les migrations de données.
- Correction de coquilles et améliorations de la lisibilité du code.
- Ajout de tests et corrections de tests existants.
