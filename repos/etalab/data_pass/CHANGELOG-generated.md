## Changelog : data_pass (30 derniers jours, au 2026-07-13)

### Résumé
Les dernières mises à jour de data_pass se concentrent sur l'amélioration de l'expérience utilisateur, notamment pour les formulaires API Particulier et les aides de rentrée scolaire. Des corrections de sécurité ont été apportées, ainsi que des améliorations de la gestion des sessions et des clés API. Des travaux ont également été réalisés sur l'intégration avec des services externes comme HubEE et ProConnect.

### Évolutions fonctionnelles
- Ajout de la gestion des éditeurs pour les formulaires API Particulier EAJE [#1690](https://github.com/etalab/data_pass/issues/1690).
- Refonte des cadres juridiques de l'API Particulier pour une meilleure factorisation et uniformisation [#1605](https://github.com/etalab/data_pass/issues/1605).
- Ajout du scope `cnav_allocation_rentree_scolaire` pour les aides facultatives et pour la rentrée scolaire [#1676](https://github.com/etalab/data_pass/pulls/1676).
- Mise à jour de l'introduction des services CISIRH [#1685](https://github.com/etalab/data_pass/pulls/1685), [#1684](https://github.com/etalab/data_pass/pulls/1684).
- Amélioration du libellé du champ de date de transmission pour l'extraction CNOUS [#1679](https://github.com/etalab/data_pass/pulls/1679).
- Ajout de la démarche DDMariage au formulaire HubEE DILA (puis revert suite à des problèmes) [#1667](https://github.com/etalab/data_pass/pulls/1667), [#1646](https://github.com/etalab/data_pass/pulls/1646).
- Amélioration de la gestion des droits utilisateurs et de la recherche [#1610](https://github.com/etalab/data_pass/pulls/1610).
- Ajout d'une fonctionnalité de désinscription en un clic depuis un email avec token chiffré [#1606](https://github.com/etalab/data_pass/pulls/1606).
- Possibilité pour les développeurs de créer et supprimer leurs propres clés API [#1618](https://github.com/etalab/data_pass/pulls/1618).
- Amélioration de la validation et de l'affichage des erreurs pour les communes CNOUS [#1633](https://github.com/etalab/data_pass/pulls/1633), [#1626](https://github.com/etalab/data_pass/pulls/1626).
- Mise à jour des valeurs MFA_ACR_VALUES dans OmniAuth Proconnect [#1636](https://github.com/etalab/data_pass/pulls/1636).

### Évolutions techniques
- Durcissement de la session à 12 heures fixes au lieu d'un glissement 12h/24h, alignement avec ProConnect [#1657](https://github.com/etalab/data_pass/pulls/1657).
- Réduction de la durée de vie de la session à 12h idle glissant, plafonnée à 24h.
- Mise en place d'un module FeatureFlag centralisé et de sa documentation [#1625](https://github.com/etalab/data_pass/pulls/1625).
- Correction d'un bug empêchant la suppression correcte des lignes de droit utilisateur [#1634](https://github.com/etalab/data_pass/pulls/1634).
- Migration du scope TVA de VIES vers la DGFIP.
- Amélioration de la gestion des bridges HubEE.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Ajout de documentation sur la gestion de session ProConnect.
- Mise à jour de la documentation pour l'authentification Proconnect.
- Correction de l'apostrophe dans un message DILA.
- Amélioration des tests et de la configuration.
- Mises à jour de dépendances (css_parser, rubocop, yard, actions/cache, actions/checkout, docker/setup-buildx-action).
- Ajout de la possibilité d'afficher une liste de toutes les définitions d'autorisation avec une fonction de recherche.
- Amélioration des wordings des cas d'usage EAJE pour l'API particulier.
- Ajout d'un message flash informant de l'expiration de la session lors de la déconnexion forcée.
