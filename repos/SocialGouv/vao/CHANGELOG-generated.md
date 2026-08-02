## Changelog : vao (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur la gestion du "premier agrément" pour les structures d'accueil, avec l'ajout de nouvelles étapes, de la gestion des compléments d'information et des améliorations de l'expérience utilisateur. Des corrections d'accessibilité (RGAA) et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la page d'accueil du premier agrément DREETS [#1501](https://github.com/SocialGouv/vao/issues/1501).
- Implémentation de la gestion des demandes de compléments d'information pour le premier agrément DREETS [#1492](https://github.com/SocialGouv/vao/issues/1492).
- Ajout de la confirmation de complétude du premier agrément DREETS [#1498](https://github.com/SocialGouv/vao/issues/1498).
- Gestion du refus du premier agrément DREETS, incluant l'envoi d'un email [#1495](https://github.com/SocialGouv/vao/issues/1495) et [#1497](https://github.com/SocialGouv/vao/issues/1497).
- Modification du premier agrément OVA suite à une demande de compléments [#1493](https://github.com/SocialGouv/vao/issues/1493).
- Prise en charge du premier agrément dans le back-office [#1487](https://github.com/SocialGouv/vao/issues/1487).
- Amélioration de l'affichage des documents dans l'onglet "Mon agrément" [#1490](https://github.com/SocialGouv/vao/issues/1490).
- Ajout de la page de bienvenue pour le premier agrément [#1471](https://github.com/SocialGouv/vao/issues/1471).
- Implémentation des étapes 1 et 4 du processus de premier agrément OVA [#1463](https://github.com/SocialGouv/vao/issues/1463) et [#1472](https://github.com/SocialGouv/vao/issues/1472).
- Ajout du fusager (assistant de navigation) pour le premier agrément, incluant les étapes de reliquat et de suivi [#1470](https://github.com/SocialGouv/vao/issues/1470), [#1475](https://github.com/SocialGouv/vao/issues/1475) et [#1476](https://github.com/SocialGouv/vao/issues/1476).
- Amélioration de l'accessibilité (RGAA) de plusieurs pages et composants, notamment la page de mot de passe oublié [#1488](https://github.com/SocialGouv/vao/issues/1488), la page de login [#1474](https://github.com/SocialGouv/vao/issues/1474), les étapes de renouvellement [#1478](https://github.com/SocialGouv/vao/issues/1478) et la hiérarchie des vacances [#1486](https://github.com/SocialGouv/vao/issues/1486).

### Évolutions techniques
- Optimisation des performances de la base de données en ajoutant des index pour corriger les timeouts en production [#1489](https://github.com/SocialGouv/vao/issues/1489).
- Migration de la construction des images Docker de buildkit-service vers buildkit-operator [#1464](https://github.com/SocialGouv/vao/issues/1464).

### Autres changements
- Corrections de wording et améliorations de l'accessibilité sur plusieurs pages et formulaires.
- Ajustements de texte pour l'ajout de la mention du casier judiciaire français [#1499](https://github.com/SocialGouv/vao/issues/1499).
- Amélioration du wording de l'étape 4 de la mise à jour [#1477](https://github.com/SocialGouv/vao/issues/1477).
- Ajout du fusager pour l'hébergement DF RGAA [#1476](https://github.com/SocialGouv/vao/issues/1476).
- Ajout du fusager pour le suivi de mon agrément [#1473](https://github.com/SocialGouv/vao/issues/1473).
