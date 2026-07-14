## Changelog : api-engagement (30 derniers jours, au 2026-07-13)

### Résumé
Cette version apporte des améliorations de sécurité, notamment concernant la gestion des accès et la prévention d'attaques, ainsi que des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur. Des optimisations ont été apportées à la recherche de missions et à la gestion des règles de diffusion. L'intégration avec des services tiers (Brevo, PostHog) a également été améliorée et de nouvelles fonctionnalités de suivi ont été ajoutées.

### Évolutions fonctionnelles
- Ajout de la possibilité pour un diffuseur de diffuser ses propres missions. [#1258](https://github.com/betagouv/api-engagement/issues/1258)
- Ajout de pages légales et de liens dans le footer de la plateforme. [#1246](https://github.com/betagouv/api-engagement/issues/1246)
- Amélioration des filtres de recherche de missions sur mobile. [#1234](https://github.com/betagouv/api-engagement/issues/1234)
- Ajout de badges de compensation sur la plateforme. [#1173](https://github.com/betagouv/api-engagement/issues/1173)
- Ajout d'un filtre pour les dispositifs de missions sur la plateforme. [#1211](https://github.com/betagouv/api-engagement/issues/1211)
- Intégration de Demarches Simplifiées pour l'envoi de newsletters. [#1209](https://github.com/betagouv/api-engagement/issues/1209)
- Ajout de la possibilité de s'inscrire à une newsletter. [#1209](https://github.com/betagouv/api-engagement/issues/1209)
- Ajout de l'événement "page view" pour le suivi de l'activité utilisateur. [#1235](https://github.com/betagouv/api-engagement/issues/1235)
- Ajout d'un paramètre `engine` à l'endpoint `/match` pour affiner la recherche de missions. [#1239](https://github.com/betagouv/api-engagement/issues/1239)

### Évolutions techniques
- Correction d'une vulnérabilité de prise de contrôle de compte sur l'endpoint d'inscription. [#1253](https://github.com/betagouv/api-engagement/issues/1253)
- Amélioration de la sécurité du prompt d'enrichissement des missions. [#1141](https://github.com/betagouv/api-engagement/issues/1141)
- Ajout d'index pour accélérer les requêtes sur les clics "my organization". [#1229](https://github.com/betagouv/api-engagement/issues/1229)
- Refactorisation de la gestion des règles de diffusion des publishers. [#1187](https://github.com/betagouv/api-engagement/issues/1187)
- Mise à jour de Typesense pour améliorer les performances de recherche. [#1200](https://github.com/betagouv/api-engagement/issues/1200)
- Suppression de l'ancien workflow Claude.
- Mise à jour des dépendances Docker et des actions CI/CD.
- Refactorisation de la logique de filtrage des missions sur la plateforme. [#1215](https://github.com/betagouv/api-engagement/issues/1215)
- Suppression des tables `publisher_diffusion` et adaptation du code. [#1206](https://github.com/betagouv/api-engagement/issues/1206)

### Autres changements
- Ajout de contrôles d'accès pour les modérateurs sur les routes de recherche de modération. [#1261](https://github.com/betagouv/api-engagement/issues/1261)
- Correction de l'utilisation de l'ID de la plateforme pour les statistiques d'emails des missions. [#1257](https://github.com/betagouv/api-engagement/issues/1257)
- Ajout de propriétés UTM aux événements envoyés au service de suivi. [#1255](https://github.com/betagouv/api-engagement/issues/1255)
- Activation du suivi sur toutes les étapes du quiz. [#1254](https://github.com/betagouv/api-engagement/issues/1254)
- Correction de l'affichage du fond d'écran en mode sombre. [#1249](https://github.com/betagouv/api-engagement/issues/1249)
- Mise à jour des URLs de Notion dans le script de génération du changelog.
- Ajout de l'ID de liste Brevo pour la plateforme engagement. [#1245](https://github.com/betagouv/api-engagement/issues/1245)
- Correction d'un bug lié à l'image de repli des missions par email. [#1190](https://github.com/betagouv/api-engagement/issues/1190)
- Amélioration de la documentation sur les règles de diffusion. [#1177](https://github.com/betagouv/api-engagement/issues/1177)
- Correction de l'affichage des filtres radio des missions sur mobile. [#1234](https://github.com/betagouv/api-engagement/issues/1234)
- Désactivation du suivi pour les utilisateurs internes. [#1236](https://github.com/betagouv/api-engagement/issues/1236)
- Suppression de l'exclusion du publisher dans la migration analytics.
- Mise à jour de la version de l'API (v4) et définition de la version actuelle du prompt dans l'environnement. [#1248](https://github.com/betagouv/api-engagement/issues/1248)
