## Changelog : ami-notifications-api (30 derniers jours, au 21 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'une nouvelle section "Services" et la refonte des pages "Suivi" (anciennement "Requêtes") et "Agenda" (anciennement "Inventaire"). Des corrections et améliorations ont également été apportées à l'interface utilisateur et à la gestion des notifications.

### Évolutions fonctionnelles
- Ajout d'une section "Services" accessible depuis le menu principal, permettant d'accéder à des services avec des paramètres configurables via l'API. [#943](https://github.com/numerique-gouv/ami-notifications-api/issues/943)
- Refonte des pages "Suivi" (anciennement "Requêtes") et "Agenda" (anciennement "Inventaire") pour une meilleure cohérence et une expérience utilisateur améliorée. [#1018](https://github.com/numerique-gouv/ami-notifications-api/issues/1018)
- Amélioration de la gestion des notifications, notamment en permettant de naviguer vers la page de suivi correspondante. [#940](https://github.com/numerique-gouv/ami-notifications-api/issues/940)
- Ajout d'un sous-titre aux événements v2. [#1033](https://github.com/numerique-gouv/ami-notifications-api/issues/1033)
- Correction d'un bug empêchant la page d'accueil de s'afficher correctement après la connexion. [#1014](https://github.com/numerique-gouv/ami-notifications-api/issues/1014)
- Amélioration de l'affichage de la hauteur de la page sur Android via 17cyber. [#1013](https://github.com/numerique-gouv/ami-notifications-api/issues/1013)

### Évolutions techniques
- Mise à jour de plusieurs dépendances : Django (6.0.5 -> 6.0.6), soupsieve (2.8.3 -> 2.8.4), ujson (5.12.1 -> 5.13.0), msgpack (1.1.2 -> 1.2.1), pyjwt (2.12.0 -> 2.13.0), dompurify (3.4.5 -> 3.4.11), js-yaml (4.1.1 -> 4.2.0), undici (8.1.0 -> 8.5.0), cryptography (46.0.7 -> 48.0.1), ws (8.20.1 -> 8.21.0).
- Correction d'un problème avec la sérialisation OTVJWTTokenSerializer. [#1070](https://github.com/numerique-gouv/ami-notifications-api/issues/1070)
- Refactorisation de la navigation principale (main-nav) pour améliorer les styles et l'accessibilité (RGAA). [#1037](https://github.com/numerique-gouv/ami-notifications-api/issues/1037)
- Amélioration des styles des boutons (RGAA). [#927](https://github.com/numerique-gouv/ami-notifications-api/issues/927)
- Implémentation de la vue "authorize" pour ami-fi. [#992](https://github.com/numerique-gouv/ami-notifications-api/issues/992)

### Autres changements
- Suppression de code inutilisé dans l'interface utilisateur. [#266](https://github.com/numerique-gouv/ami-notifications-api/issues/266)
- Diverses corrections de style et de formatage.
- Mise à jour de la documentation.
