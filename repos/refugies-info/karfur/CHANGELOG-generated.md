## Changelog : karfur (30 derniers jours, au 25 juin 2026)

### Résumé
Cette version apporte des améliorations à l'interface utilisateur, notamment sur les fiches RCO et la compatibilité mobile. Des corrections de bugs ont été implémentées pour résoudre des problèmes d'affichage, de connexion et de gestion des données. Des efforts importants ont été consacrés à l'intégration de Letta Code pour l'analyse et la validation du code, ainsi qu'à la préparation de l'intégration de nouveaux "skills" pour l'outil.

### Évolutions fonctionnelles
- Amélioration de l'affichage des adresses postales sur les fiches RCO, corrigeant un problème de coupure. [#3822](https://github.com/refugies-info/karfur/pull/3822)
- Correction d'un bug empêchant la prévisualisation des fiches. [#3823](https://github.com/refugies-info/karfur/pull/3823)
- Mise à jour des coordonnées des opérateurs sur la carte "Agir". [#3817](https://github.com/refugies-info/karfur/pull/3817)
- Mise à jour du texte sur la page "Mission et Impact". [#3824](https://github.com/refugies-info/karfur/pull/3824)
- Correction d'un problème de connexion et de réinitialisation de mot de passe. [#3814](https://github.com/refugies-info/karfur/pull/3814)
- Correction de l'affichage des accents dans le moteur de recherche. [#3769](https://github.com/refugies-info/karfur/pull/3769)
- Amélioration de la réactivité des écrans de connexion sur mobile. [#3773](https://github.com/refugies-info/karfur/pull/3773)
- Correction de l'affichage des labels de département qui se superposaient à la pop-up. [#3766](https://github.com/refugies-info/karfur/pull/3766)
- Correction d'un bug sur iOS lié à l'affichage des images. [#3783](https://github.com/refugies-info/karfur/pull/3783)

### Évolutions techniques
- Intégration de Letta Code pour l'auto-review des pull requests, incluant l'installation de l'application GitHub. [#3815](https://github.com/refugies-info/karfur/pull/3815)
- Mise en place d'un workflow CI/CD pour Letta Code.
- Préparation de l'infrastructure pour l'intégration de nouveaux "skills" (QMD, audit, rédaction, metadata) pour Letta Code.
- Suppression de configurations liées à Claude. [#3814](https://github.com/refugies-info/karfur/pull/3814)
- Mise à jour de la gestion des dépendances et correction de vulnérabilités de sécurité.
- Amélioration de la robustesse des tests et correction de problèmes liés à l'environnement de test mobile.
- Ajout de hooks Git pour la détection de secrets et la validation du code.
- Amélioration de la gestion des erreurs et des valeurs nulles dans le code.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Mise à jour des mentions légales sur le site et l'application. [#3785](https://github.com/refugies-info/karfur/pull/3785)
- Suppression d'un libellé "IA" sur les fiches RCO. [#3784](https://github.com/refugies-info/karfur/pull/3784)
- Suppression de code inutile et de logs de débogage.
- Correction de typos et amélioration de la documentation.
- Mise à jour des dépendances et des configurations.
